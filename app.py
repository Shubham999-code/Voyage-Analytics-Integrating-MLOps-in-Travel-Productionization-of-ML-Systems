from flask import Flask, request, jsonify
import joblib
import pandas as pd
import traceback

app = Flask(__name__)

# Load the model during app startup
try:
    model = joblib.load('flight_price_model.joblib')
except Exception as e:
    model = None
    print(f"Error loading model: {e}")
print(f"Initial model type: {type(model)}")

@app.route('/health', methods=['GET'])
def health_check():
    global model
    print(f"Health check called. Model type: {type(model)}")
    if model is not None:
        return jsonify({'status': 'healthy', 'model_loaded': True}), 200
    else:
        return jsonify({'status': 'unhealthy', 'model_loaded': False}), 500

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model is not loaded.'}), 500
        
    try:
        data = request.get_json()
        
        # Expected features: ['flightType', 'time', 'distance', 'agency', 'from', 'to']
        # Convert JSON request to a DataFrame (assuming one record for simplicity)
        df = pd.DataFrame([data])
        
        # Make prediction
        prediction = model.predict(df)
        
        return jsonify({'predicted_price': round(prediction[0], 2)}), 200
        
    except Exception as e:
        return jsonify({'error': str(e), 'trace': traceback.format_exc()}), 400

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
