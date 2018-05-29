import os
import pathlib
import export_vec_to_csv as doc2vec
from flask import Flask, request, render_template, send_from_directory, flash, redirect
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['csv'])
UPLOAD_FOLDER = 'uploads'
application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@application.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

@application.route('/uploads', methods=['POST'])
def upload_csv():
    if request.method == 'POST':
        file = request.files['csv']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(application.config['UPLOAD_FOLDER'], filename))
            doc2vec.process_doc2vec(os.path.join(application.config['UPLOAD_FOLDER'], filename))
            try:
                return send_from_directory(application.root_path, 'extracted.csv', as_attachment=True)
            except Exception as e:
                return str(e)
