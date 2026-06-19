# Travel Capstone MLOps Project

This repository contains the complete implementation for the Travel Data Capstone Project. The goal of this project is to leverage users, flights, and hotels datasets to build machine learning models and deploy them using industry-standard MLOps practices.

## Project Structure

- `ML_Modeling.ipynb`: A Colab/Jupyter Notebook containing Data Exploration, Data Preprocessing, and Model Training for the Regression, Classification, and Recommender models. It tracks experiments using MLflow locally.
- `app.py`: A Flask REST API that serves the flight price prediction regression model.
- `streamlit_app.py`: A Streamlit web application providing a user interface for the travel recommendation model and data visualization.
- `Dockerfile`: A unified Dockerfile used to containerize both the Flask API and Streamlit application.
- `kubernetes/`: Contains the `deployment.yaml` and `service.yaml` to deploy the models using Kubernetes for scalability.
- `airflow/dags/`: Contains the Apache Airflow DAG (`model_training_dag.py`) for automated workflow orchestration.
- `Jenkinsfile`: Defines the CI/CD pipeline for consistent integration and deployment.
- `requirements.txt`: Python package dependencies.

## Setup Instructions

### 1. Model Training (Colab/Local Jupyter)
1. Ensure you have the datasets (`users.csv`, `flights.csv`, `hotels.csv`) in the same directory.
2. Open `ML_Modeling.ipynb` (can be uploaded to Google Colab).
3. Run all the cells to train the models.
4. The Notebook will create local `mlflow.db` and save three joblib files (`flight_price_model.joblib`, `gender_classification_model.joblib`, `hotel_recommender.joblib`).
5. Ensure these `.joblib` files are in the main project directory.

### 2. Local Testing (Flask and Streamlit)
Install dependencies:
```bash
pip install -r requirements.txt
```

**Run Flask API:**
```bash
python app.py
# Test API
# curl -X POST -H "Content-Type: application/json" -d '{"flightType": "firstClass", "time": 1.76, "distance": 676.53, "agency": "FlyingDrops", "from": "Recife (PE)", "to": "Florianopolis (SC)"}' http://127.0.0.1:5000/predict
```

**Run Streamlit App:**
```bash
streamlit run streamlit_app.py
```

### 3. Docker Containerization
Build the Docker image:
```bash
docker build -t travel-mlops:latest .
```
Run Flask from Docker:
```bash
docker run -p 5000:5000 travel-mlops:latest
```
Run Streamlit from Docker:
```bash
docker run -p 8501:8501 travel-mlops:latest streamlit run streamlit_app.py
```

### 4. Kubernetes Deployment
Ensure you have Minikube or a K8s cluster running.
```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

### 5. Airflow and Jenkins
- **Airflow:** Copy `airflow/dags/model_training_dag.py` to your Airflow `dags` folder to schedule notebook retraining.
- **Jenkins:** Configure a Pipeline job in Jenkins pointing to this repository to execute the CI/CD process defined in the `Jenkinsfile`.
