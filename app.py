import os
import cv2
import numpy as np
from flask import Flask, request, render_template, url_for
from werkzeug.utils import secure_filename
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import img_to_array

# Initialize Flask App
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Load the Pre-trained Keras Model
# MobileNetV2 is lightweight and perfect for web apps
print("Loading model...")
model = MobileNetV2(weights='imagenet')
print("Model loaded!")

def predict_image(filepath):
    """Processes the image and returns top 3 predictions."""
    # 1. Read image using OpenCV
    image = cv2.imread(filepath)
    # Convert BGR (OpenCV default) to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Resize to 224x224 as required by MobileNetV2
    image = cv2.resize(image, (224, 224))
    
    # 2. Prepare image for TensorFlow
    img_array = img_to_array(image)
    img_array = np.expand_dims(img_array, axis=0) # Add batch dimension
    img_array = preprocess_input(img_array)
    
    # 3. Make Prediction
    preds = model.predict(img_array)
    # Decode top 3 results
    results = decode_predictions(preds, top=3)[0] 
    return results

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return 'No file uploaded'
        
        file = request.files['file']
        if file.filename == '':
            return 'No file selected'
            
        if file:
            # Secure the filename and save it
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Run the image through our model
            predictions = predict_image(filepath)
            
            # Render the results on the HTML page
            return render_template('index.html', filename=filename, predictions=predictions)
            
    return render_template('index.html')

if __name__ == '__main__':
    # Ensure the upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    # Run the app
    app.run(debug=True, port=5000)