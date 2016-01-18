import os
import logging
from logging import Formatter, FileHandler
from flask import Flask, request, jsonify, render_template, send_file

from ocr import process_image

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/capage', methods=["POST"])
def ocr():
    try:
        url = request.json['image_url']
        output = process_image(url)
	    #print output
        return jsonify({"output": output})
    except:
        return jsonify(
            {"error": "Wrong input type"}
        )

@app.route('/a.jpg')
def img():
    return send_file('img/a.jpg',mimetype='image/jpeg')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
