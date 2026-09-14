import os
import pytest
from app import create_app

@pytest.fixture
def app():
    # Initialize the app using your factory function
    app = create_app()
    
    # Override configuration for testing
    app.config.update({
        "TESTING": True,
        "UPLOAD_FOLDER": os.path.join(os.getcwd(), 'tests', 'temp_uploads')
    })
    
    # Create a temporary upload directory for test images
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    yield app

@pytest.fixture
def client(app):
    # A test client to simulate browser requests
    return app.test_client()