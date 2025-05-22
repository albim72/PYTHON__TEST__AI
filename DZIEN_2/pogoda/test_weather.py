import pytest
import pandas as pd
from weather import load_weather_data, add_temperature_fahrenheit, average_temperature

@pytest.fixture
def sample_df():
    data = {
        "city": ["Warsaw", "Krakow", "Gdansk"],
        "temperature_c": [22, 25, 19]
    }
    return pd.DataFrame(data)

def test_add_temperature_fahrenheit(sample_df):
    df = add_temperature_fahrenheit(sample_df.copy())
    assert "temperature_f" in df.columns
    assert round(df.loc[0, "temperature_f"], 2) == 71.6

def test_average_temperature(sample_df):
    avg = average_temperature(sample_df)
    assert avg == pytest.approx(22.0, abs=0.1)
