import uvicorn
from fastapi import FastAPI
import numpy as np
from base_data import Data
import pickle
import pandas as pd


app=FastAPI(title="Deploying Presentation")

model=pickle.load(open("C:/Users/ismai/OneDrive/Masaüstü/Galaksiya Staj/Deploy/app/new_pipeline.pkl","rb"))

@app.get("/")
def home():
    return "Hello"


@app.post("/predict")
def predict(data:Data):
    data=dict(data)
    calc=data["calc"]
    gravity=data["gravity"]
    ph=data["ph"]
    cond=data["cond"]
    osmo=data["osmo"]
    urea=data["urea"]

    oxalate_concentration = data['calc'] / data['osmo']

    # Ratio of calcium to oxalate
    calc_to_oxalate_ratio = data['calc'] / oxalate_concentration

    # Ion balance
    ion_balance= data['calc'] - oxalate_concentration

    # Specific gravity to osmolarity ratio
    sg_to_osmo_ratio= data['gravity'] / data['osmo']

    # Urea to creatinine ratio
    urea_to_creatinine_ratio = data['urea'] / data['cond']

    # pH balance
    #pH_balance= ph.apply(lambda x: 1 if 5.5 <= x <= 7.5 else 0)
    if ph>=5.5 and ph<=7.5:
        pH_balance=1
    else:
        pH_balance=0

    # Osmolarity to conductivity ratio
    osmo_to_cond_ratio = data['osmo'] / data['cond']
    
    prediction=model.predict([[gravity,ph,cond,calc,osmo,urea,oxalate_concentration,calc_to_oxalate_ratio,ion_balance,sg_to_osmo_ratio,urea_to_creatinine_ratio,pH_balance,osmo_to_cond_ratio]])
    
    if(prediction[0]==1):
        prediction="Patient has kidney stone"
    elif(prediction[0]==0):
        prediction="Patient has not kidney stone"
    else:
        prediction="Hata"
    return {
        "prediction":prediction
    }



    


if __name__=="__main__":
    
    uvicorn.run(app,host="127.0.0.1",port=8000)