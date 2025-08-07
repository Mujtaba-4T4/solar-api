import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

NOCT = 44

def calulcate_Tbom(AIR_TEMP, NOCT, Gpoa):
    return AIR_TEMP + ((NOCT - 20) / 800) * Gpoa

def calculate_Gpoa(Gglob_hor, Gdiff_hor):
    return Gglob_hor + Gdiff_hor

def calculate_time(DATE):
    dt = pd.to_datetime(DATE)
    month = dt.month
    hour = dt.hour
    minute = dt.minute
    
    Hour_sin = np.sin(2 * np.pi * hour / 24)
    Hour_cos = np.cos(2 * np.pi * hour / 24)
    Month_sin = np.sin(2 * np.pi * month / 12)
    Month_cos = np.cos(2 * np.pi * month / 12)
    Minute_sin = np.sin(2 * np.pi * minute / 60)
    Minute_cos = np.cos(2 * np.pi * minute / 60)

    return Hour_sin, Hour_cos, Month_sin, Month_cos, Minute_sin, Minute_cos


def calculate_data(Gglob_hor, Gdiff_hor, RH_AIR, AIR_TEMP, WIND_SPEED, DATE):
    
    Hour_sin, Hour_cos, Month_sin, Month_cos, Minute_sin, Minute_cos = calculate_time(DATE)
    Gpoa = calculate_Gpoa(Gglob_hor, Gdiff_hor)
    Tbom = calulcate_Tbom(AIR_TEMP, NOCT, Gpoa)

    data = {
        "Tbom": [Tbom],
        "Gpoa": [Gpoa],
        "Gglob_hor": [Gglob_hor],
        "Gdiff_hor": [Gdiff_hor],
        "RH_AIR": [RH_AIR],
        "AIR_TEMP": [AIR_TEMP],
        "WIND_SPEED": [WIND_SPEED],
        "Hour_sin": [Hour_sin],
        "Hour_cos": [Hour_cos],
        "Month_sin": [Month_sin],
        "Month_cos": [Month_cos],
        "Minute_sin": [Minute_sin],
        "Minute_cos": [Minute_cos]
    }

    df = pd.DataFrame(data)

    scaler = StandardScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

    return df_scaled