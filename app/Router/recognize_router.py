import os
from flask import current_app as app, request, render_template, send_from_directory, redirect,Blueprint
from werkzeug.utils import secure_filename
from model.classifier import predict_image

recognize_bp = Blueprint('recognize', __name__)

@recognize_bp.route('/recognize', methods=['GET', 'POST'])
def recognize():
    # Renders the Recognition / Upload Page
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
            
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
            
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            results = predict_image(filepath)
            
            # Pass the results and filename to the template
            return render_template('recognize.html', results=results, filename=filename)
            
    return render_template('recognize.html')

@recognize_bp.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)