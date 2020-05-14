from flask import Flask, request
from .process_image import process_image
import requests
import json
from time import strftime, gmtime
app = Flask(__name__)

def server():
    @app.route('/', methods=['POST'])
    def get_image():
        if request.method == 'POST':
            s = strftime("%Y-%m-%dT%H:%M:%S.000Z", gmtime())
            print(s)
            data = request.get_json()
            process_image(data.image)


if __name__ == '__main__':
    app.run()
