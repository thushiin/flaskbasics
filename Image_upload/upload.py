from flask import Flask,render_template,request
import os

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('uploadimg.html')

app.config['UPLOAD_PATH']='static/images'
@app.route('/upload', methods=['post'])
def upload():
    upimg=request.files['file']
    print(upimg)
    uplimg=upimg.filename
    print(uplimg)
    upimg.save(os.path.join(app.config['UPLOAD_PATH'],upimg.filename))
    return render_template('displayimg.html',filename=uplimg)
if __name__=='__main__':
    app.run(debug=True)