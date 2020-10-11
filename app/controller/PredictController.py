# Load libraries
import os
import flask
from keras.preprocessing import image
from pandas import np
from tensorflow import keras
from flask import request
from app import response
from utils.util import base64_to_pil

# instantiate flask
app = flask.Flask(__name__)
loaded_model = keras.models.load_model(os.path.join('utils', 'model', 'model-2.h5'))
names = ['Bintang Maratur', 'Mangiring', 'Ragi Hotang', 'Sibolang', "Suri-Suri"]

def index():
    try:
        return response.ok("prediction", "")
    except Exception as e:
        print(e)


def prediction():
    try:
        filename = os.path.join('utils', 'image', 'image.png')
        img = base64_to_pil(request.json['image'])
        img.save(filename)

        img_size = 180
        img = image.load_img(filename, target_size=(img_size, img_size))
        img_tensor = image.img_to_array(img)
        img_tensor = np.expand_dims(img_tensor, axis=0)
        class_pred = loaded_model.predict_classes(img_tensor).tolist()
        return response.ok(class_pred[0], names[class_pred[0]])
    except Exception as e:
        print(e)
        return response.badRequest("error", "error")
