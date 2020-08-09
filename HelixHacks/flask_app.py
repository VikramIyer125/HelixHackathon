import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from keras.models import load_model
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)

model = load_model('keras_model.h5')

def predict(img_path, model): 
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(img_path)    
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    print(prediction)
    if(prediction[0][0]>prediction[0][1]): 
        return 'Covid infected' 
    else: 
        return 'Normal'

UPLOAD_FOLDER = '/Users/vikramiyer/Desktop/HelixHacks/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/localtestingcenter.html') 
def testing_center():
    return render_template('localtestingcenter.html')

@app.route('/bodyscan.html', methods=['GET']) 
def body_scan():
    print('here')
    return render_template('bodyscan.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        print(f)
        basepath = os.path.dirname(UPLOAD_FOLDER)
        file_path = os.path.join( basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        preds = predict(file_path, model)
        return preds
    return None

@app.route('/morecovidinfo.html') 
def more_info():
    return render_template('morecovidinfo.html')

@app.route('/faq.html') 
def faq():
    return render_template('faq.html')

@app.route('/register.html') 
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run()