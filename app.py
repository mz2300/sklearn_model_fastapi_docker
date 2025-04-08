import numpy as np
import PIL.Image
import io

from contextlib import asynccontextmanager
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from keras.applications.efficientnet import EfficientNetB0
from keras.applications.efficientnet import preprocess_input, decode_predictions



model_dict = {}

@asynccontextmanager
async def lifespan(app: FastAPI):

    ## --------startup tasks--------

    # 1. Load the ML model
    model_dict['model'] = EfficientNetB0()

    yield

     ## --------shutdown tasks--------
    

app = FastAPI(lifespan = lifespan, 
              title = "Image Classifiction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def convert_to_output(preds):
    decoded_preds = decode_predictions(preds, top=5)[0]
    
    out = ''
    for p in decoded_preds:
        out += str(p[1])
        out += ': '
        out += str(p[2])
        out += '; '

    return out


@app.get("/")
async def root():
    return {"healthCheck": "OK"}

@app.post('/predict-image/')
async def predict_image(file: UploadFile = File(...)):
    contents = await file.read()
    img_pil = PIL.Image.open(io.BytesIO(contents))
    img_pil = img_pil.resize((224, 224), PIL.Image.LANCZOS)
    img_arr = np.array(img_pil)[:, :, :3] # take first 3 channels (without transparency)
    img_arr = np.expand_dims(img_arr, axis=0)
    img_arr = preprocess_input(img_arr)
    preds = model_dict['model'].predict(img_arr)

    return {'predictions' :  convert_to_output(preds)}