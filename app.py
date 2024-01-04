from contextlib import asynccontextmanager
from fastapi import FastAPI
from joblib import load
from model.wine import Wine

model_dict = {}

@asynccontextmanager
async def lifespan(app: FastAPI):

    # Load the ML model
    model_dict['model'] = load('model/ml/wine_model.joblib')

    yield



app = FastAPI(lifespan = lifespan, 
              title = "Wine ML API", 
              description = "API for wine dataset ml model")



@app.post('/predict', tags = ["predictions"])
async def get_prediction(data: Wine):
    data = dict(data)['data']
    prediction = model_dict['model'].predict(data).tolist()
    log_proba = model_dict['model'].predict_proba(data).tolist()
    return {"prediction": prediction,
            "log_proba": log_proba}