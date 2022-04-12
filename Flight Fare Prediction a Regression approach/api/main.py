from datetime import datetime
from fastapi import FastAPI
import uvicorn
from joblib import load
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import sklearn
from pydantic import BaseModel


class request_body(BaseModel):
    Airline: str
    Source: str
    Destination: str
    Total_Stops: str
    Journey_day: datetime
    Arrival_day: datetime


app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model = load(r"../saved_models\flight_fare.joblib")
clm = load(r"../saved_models\clm.joblib")


@app.get("/")
def run():
    return "App is running"


@app.post('/predict')
def predict(data: request_body):

    # dict = {'Airline': '', 'Source': '', 'Destination': '', 'Total_Stops': '',
    #         'Journey_day': 0, 'Journey_month': 0, 'Dep_hour': 0, 'Dep_minute': 0,
    #         'Arrival_hour': 0, 'Arrival_minute': 0,'Duration_hour':0, 'Duration_minute': 0}

    dict = {}

    dict['Airline'] = data.Airline
    dict['Source'] = data.Source
    dict['Destination'] = data.Destination
    dict['Total_Stops'] = data.Total_Stops
    dict['Journey_day'] = pd.to_datetime(
        data.Journey_day, format="%Y-%m-%dT%H:%M").day
    dict['Journey_month'] = pd.to_datetime(
        data.Journey_day, format="%Y-%m-%dT%H:%M").month
    dict['Dep_hour'] = pd.to_datetime(
        data.Journey_day, format="%Y-%m-%dT%H:%M").hour
    dict['Dep_minute'] = pd.to_datetime(
        data.Journey_day, format="%Y-%m-%dT%H:%M").minute
    dict['Arrival_hour'] = pd.to_datetime(
        data.Arrival_day, format="%Y-%m-%dT%H:%M").hour
    dict['Arrival_minute'] = pd.to_datetime(
        data.Arrival_day, format="%Y-%m-%dT%H:%M").minute
    dict['Duration_hour'] = abs(dict['Dep_hour'] - dict['Arrival_hour'])
    dict['Duration_minute'] = abs(dict['Dep_minute'] - dict['Arrival_minute'])

    # arr = [[data.Airline,
    #         data.Source,
    #         data.Destination,
    #         data.Total_Stops,
    #         pd.to_datetime(data.Journey_day, format="%Y-%m-%dT%H:%M").day,
    #         pd.to_datetime(data.Journey_day, format="%Y-%m-%dT%H:%M").month,
    #         pd.to_datetime(data.Journey_day, format="%Y-%m-%dT%H:%M").hour,
    #         pd.to_datetime(data.Journey_day, format="%Y-%m-%dT%H:%M").minute,
    #         pd.to_datetime(data.Arrival_day, format="%Y-%m-%dT%H:%M").hour,
    #         pd.to_datetime(data.Arrival_day, format="%Y-%m-%dT%H:%M").minute,
    #         pd.to_datetime(data.Journey_day, format="%Y-%m-%dT%H:%M").hour -
    #         pd.to_datetime(data.Arrival_day, format="%Y-%m-%dT%H:%M").hour,
    #         pd.to_datetime(data.Journey_day, format="%Y-%m-%dT%H:%M").minute - pd.to_datetime(data.Arrival_day, format="%Y-%m-%dT%H:%M").minute]]

    # df = pd.DataFrame(arr, columns= ['Airline', 'Source', 'Destination', 'Total_Stops',
    #    'Journey_day', 'Journey_month', 'Dep_hour', 'Dep_minute',
    #    'Arrival_hour', 'Arrival_minute', 'Duration_hour', 'Duration_minute'])

    df = pd.DataFrame(dict, index = [0])
    test = clm.transform(df)
    prediction = model.predict(test)
    return {"prediction": float(prediction)}


# if __name__ == "__main__":
#     uvicorn.run(app)
