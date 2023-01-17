from fastapi import FastAPI
from . import schemas
import pandas as pd
from fastapi.encoders import jsonable_encoder
import pickle

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Root home"}

@app.post("/model")
def get_result(input_model: schemas.ModelInput):
    model = pickle.load(open("models/model.pkl", 'rb'))
    df_feats = pd.DataFrame([jsonable_encoder(input_model)])
    predict = model.predict(df_feats)

    return int(predict[0])