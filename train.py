import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
import warnings
warnings.filterwarnings('ignore')

mlflow.set_tracking_uri('sqlite:///mlflow.db')

users_df = pd.read_csv('users.csv')
flights_df = pd.read_csv('flights.csv')
hotels_df = pd.read_csv('hotels.csv')

# 1. Regression
mlflow.set_experiment("Flight_Price_Regression")
with mlflow.start_run():
    features = ['flightType', 'time', 'distance', 'agency', 'from', 'to']
    X = flights_df[features]
    y = flights_df['price']
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), ['time', 'distance']),
            ('cat', OneHotEncoder(handle_unknown='ignore'), ['flightType', 'agency', 'from', 'to'])
        ])
    model = Pipeline(steps=[('preprocessor', preprocessor),
                            ('regressor', RandomForestRegressor(n_estimators=10, random_state=42))]) # reduced estimators for speed
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, "flight_price_model.joblib")
    print("Regression model saved.")

# 2. Classification
mlflow.set_experiment("Gender_Classification")
with mlflow.start_run():
    features = ['company', 'age']
    X = users_df[features].copy()
    y = users_df['gender']
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), ['age']),
            ('cat', OneHotEncoder(handle_unknown='ignore'), ['company'])
        ])
    model = Pipeline(steps=[('preprocessor', preprocessor),
                            ('classifier', RandomForestClassifier(n_estimators=10, random_state=42))])
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, "gender_classification_model.joblib")
    print("Classification model saved.")

# 3. Recommender
mlflow.set_experiment("Hotel_Recommender")
with mlflow.start_run():
    hotel_stats = hotels_df.groupby(['name', 'place']).agg(
        total_bookings=('travelCode', 'count'),
        avg_price=('price', 'mean')
    ).reset_index()
    hotel_stats['norm_bookings'] = hotel_stats['total_bookings'] / hotel_stats['total_bookings'].max()
    hotel_stats['norm_price'] = hotel_stats['avg_price'] / hotel_stats['avg_price'].max()
    hotel_stats['score'] = (hotel_stats['norm_bookings'] * 0.7) - (hotel_stats['norm_price'] * 0.3)
    recommendations = hotel_stats.sort_values(by=['place', 'score'], ascending=[True, False])
    
    recommender_dict = {}
    for place in recommendations['place'].unique():
        recommender_dict[place] = recommendations[recommendations['place'] == place].head(5)[['name', 'avg_price', 'score']].to_dict('records')
    joblib.dump(recommender_dict, "hotel_recommender.joblib")
    print("Recommender model saved.")
