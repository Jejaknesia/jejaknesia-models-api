import os
import uvicorn
import traceback
import tensorflow.compat.v2 as tf
import numpy as np
from typing import List
tf.enable_v2_behavior()
import h5py

from pydantic import BaseModel
from urllib.request import Request
from fastapi import FastAPI, Response, UploadFile
from utils import load_image_into_numpy_array

app = FastAPI()

# This endpoint is for a test (or health check) to this server
@app.get("/")
def index():
    return "Hello world from ML endpoint!"

# If your model needs text input, use this endpoint!
class RequestText(BaseModel):
    text: str

# here we use tflite for some reason
interpreter = tf.lite.Interpreter(model_path="converted_model.tflite")
def recommendtflite(textinput):
    interpreter.allocate_tensors()

    # get input and output tensors
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # print(input_details)

    interpreter.set_tensor(input_details[0]['index'], np.array([textinput]))
    # interpreter.set_tensor(input_details[0]['index'], np.array(["Pfizer"]))

    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[1]['index'])
    arr = []
    for something in output_data[0]:
        arr.append(something.decode('utf-8'))
    return arr

loaded = tf.saved_model.load("export")
def recommendrawmodel(textinputarr):
    scores, name = loaded(textinputarr)

    arr = []
    for something in name[0]:
        print(something)
        data = something.numpy()
        arr.append(data.decode('utf-8'))
    
    return arr

@app.post("/predict_text")
def predict_text(req: RequestText, response: Response):
    try:
        # In here you will get text sent by the user
        text = req.text
        print("Uploaded text:", text)
        result = recommendtflite(text)
        
        return result
    
    except Exception as e:
        traceback.print_exc()
        response.status_code = 500
        return "Internal Server Error"
    
@app.post("/predict_text2")
def predict_text(req: List[str], response: Response):
    try:
        result = recommendrawmodel(req)
        return result
    
    except Exception as e:
        traceback.print_exc()
        response.status_code = 500
        return "Internal Server Error"


# Starting the server
# You can check the API documentation easily using /docs after the server is running
# port = os.environ.get("PORT", 8080)
# print(f"Listening to http://0.0.0.0:{port}")
# uvicorn.run(app, host='0.0.0.0', port=port)
