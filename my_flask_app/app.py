from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the CatBoost model
model = pickle.load(open('catboost_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(request.form.get(feature)) for feature in [
        'battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g',
        'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height',
        'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g',
        'touch_screen', 'wifi'
    ]]
    
    # Convert features to numpy array
    features_array = np.array([features])
    
    # Predict using the model
    prediction = model.predict(features_array)
    
    return render_template('index.html', prediction_text=f'Predicted Price: {prediction[0]}')

if __name__ == "__main__":
    app.run(debug=True)
