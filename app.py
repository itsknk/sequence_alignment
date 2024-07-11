from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import os
from algorithms.needleman_wunsch import nw_align
from algorithms.smith_waterman import sw_align

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['UPLOAD_FOLDER'] = 'uploads/'

ALLOWED_EXTENSIONS = {'fa', 'fasta'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file1' not in request.files or 'file2' not in request.files:
            flash('No file part')
            return render_template('index.html')
        
        file1 = request.files['file1']
        file2 = request.files['file2']
        
        if file1.filename == '' or file2.filename == '':
            flash('No selected file')
            return render_template('index.html')
        
        if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
            filename1 = secure_filename(file1.filename)
            filename2 = secure_filename(file2.filename)
            
            file1_path = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
            file2_path = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
            
            file1.save(file1_path)
            file2.save(file2_path)
            
            algorithm = request.form['algorithm']
            
            if algorithm == 'needleman':
                seq1_align, match_string, seq2_align, alignment_score = nw_align(file1_path, file2_path)
            elif algorithm == 'smith':
                seq1_align, match_string, seq2_align, alignment_score = sw_align(file1_path, file2_path)
            
            os.remove(file1_path)
            os.remove(file2_path)
            
            return render_template('result.html', seq1_align=seq1_align, match_string=match_string, seq2_align=seq2_align, alignment_score=alignment_score)
    
    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
