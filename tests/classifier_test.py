import os
import cv2
import numpy as np
from model.classifier import predict_image

def test_predict_image_structure(tmp_path):
    """Test the AI pipeline with a dynamically generated image."""
    # Generate a simple 224x224 blue square to simulate an uploaded photo
    test_image_path = os.path.join(tmp_path, "test_dummy.jpg")
    dummy_image = np.zeros((224, 224, 3), dtype=np.uint8)
    dummy_image[:] = (255, 0, 0)
    cv2.imwrite(test_image_path, dummy_image)
    
    # Run the model
    results = predict_image(test_image_path)
    
    # Verify the backend passes the exact data structure the frontend expects
    assert isinstance(results, list)
    assert len(results) == 5
    
    first_result = results[0]
    assert "label" in first_result
    assert "confidence" in first_result
    assert "is_top" in first_result
    
    # The first item should always be flagged as the top prediction
    assert first_result["is_top"] is True