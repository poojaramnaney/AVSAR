from flask import Flask
from flask import request
from flask import render_template
import os

from keywordtoanswer import main_function,get_audio,speak

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        f = request.files['audio_data']
        with open('audio.wav', 'wb') as audio:
            f.save(audio)
        print('file uploaded successfully')


        return render_template('index.html', request="POST")


    else:
        return render_template("htm/index.html")
    main_function()
