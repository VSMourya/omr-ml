import jsonify
import os
import json
import flask 
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from transform import main
import cv2

app = flask.Flask(__name__)


@app.route('/predict', methods=['GET','POST'])
def predict():

    if request.method == 'POST':
        # Get the file from post request
        f = request.files['image']

        # Save the file to ./uploads
        # basepath = os.path.dirname(__file__)
        file_name = secure_filename(f.filename)
        file_path = os.path.join("imgs", file_name)
        f.save(file_path)

        questions = 20
        # imgPath =f"./imgs/{filename}"
        im = cv2.imread(file_path)

        resp = main(im,file_path,questions)

        return json.dumps(resp)
    
if __name__ == "__main__":
    app.run()