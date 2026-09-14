import numpy as np
import cv2
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import img_to_array
import os

model = MobileNetV2(weights='imagenet')

def predict_image(filepath):
    image = cv2.imread(filepath)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    
    img_array = img_to_array(image)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    preds = model.predict(img_array)
    # Get top 5 predictions for the UI progress bars
    results = decode_predictions(preds, top=5)[0] 
    
    formatted_results = []
    for i, (imagenet_id, label, conf) in enumerate(results):
        formatted_results.append({
            "label": label.replace('_', ' ').title(),
            "confidence": round(conf * 100, 1),
            "is_top": i == 0 # Identifies the highest probability
        })
        
    return formatted_results