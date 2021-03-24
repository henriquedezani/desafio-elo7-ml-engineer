import logging
from flask import Flask, request
import os
import cloudpickle

app = Flask(__name__)

logger = logging.getLogger('werkzeug')
logger.addHandler(logging.FileHandler(os.getenv("LOGGING_PATH")))
logger.setLevel(logging.ERROR)

with open(os.getenv("MODEL_PATH"), 'rb') as model_file:
    model = cloudpickle.load(model_file)

@app.route('/v1/categorize', methods=["POST"])
def categorize():
    try:
        products = request.json['products']
        categories = model.predict([product['title'] for product in products])
        return {"categories": categories.tolist()}
    except Exception as ex:
        logger.error('erro' + str(ex))
        return "(Bad Request)", 400