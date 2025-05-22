import pandas as pd
import numpy as np

def load_weather_data(csv_path):
    """Wczytuje dane pogodowe z pliku CSV"""
    df = pd.read_csv(csv_path)
    return df

def add_temperature_fahrenheit(df):
    """Dodaje kolumnę z temperaturą w Fahrenheitach"""
    df["temperature_f"] = np.round(df["temperature_c"] * 9/5 + 32, 2)
    return df

def average_temperature(df):
    """Zwraca średnią temperaturę w Celsjuszach"""
    return np.mean(df["temperature_c"])
