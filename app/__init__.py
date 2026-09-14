import os
from flask import Flask


def create_app():
    # Explicitly map the templates and static folders to the root directory
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    
    # Target the uploads directory at the project root
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Import routes after app is created to avoid circular dependencies
    with app.app_context():
        from .Router.main_router import main_bp
        from .Router.recognize_router import recognize_bp
        #from .Router.recognize_router import upload_bp

        app.register_blueprint(main_bp)
        app.register_blueprint(recognize_bp)
        #app.register_blueprint(upload_bp)
    return app

#run command
#flask --app app run --debug