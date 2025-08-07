from fastapi import FastAPI
from tensorflow.keras.models import load_model
from solar_utils import calculate_data

app = FastAPI()

model = load_model("best_model.keras")


@app.get("/")
def root():
    return {"frfr" : "ong"}


@app.post("/ml")
def predict_Pm(time, direct_radiation, diffuse_radiation, temp, humidity, windspeed):
    df = calculate_data(time, direct_radiation, diffuse_radiation, temp, humidity, windspeed)
    df2 = calculate_data(Gglob_hor, Gdiff_hor, RH_AIR, AIR_TEMP, WIND_SPEED, DATE)
    pred = model.predict(df)
    return pred