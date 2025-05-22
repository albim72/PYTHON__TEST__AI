from weather import load_weather_data, add_temperature_fahrenheit, average_temperature

def main():
    path = "data.csv"

    # 1. Wczytaj dane
    df = load_weather_data(path)
    print("📊 Dane pogodowe:")
    print(df)

    # 2. Dodaj temperaturę w Fahrenheitach
    df = add_temperature_fahrenheit(df)
    print("\n🌡️ Dane z temperaturą w °F:")
    print(df)

    # 3. Oblicz średnią temperaturę
    avg_temp = average_temperature(df)
    print(f"\n📈 Średnia temperatura (°C): {avg_temp:.2f}")

if __name__ == "__main__":
    main()
