import requests

def get_weather(city):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        'forecast': 'today',
        'daily': 'weathercode',
        'timezone': 'Europe/Madrid',
        'location': city
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        if response.text:  # Verificar si la respuesta no está vacía
            try:
                weather_data = response.json()
                return weather_data
            except requests.exceptions.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
        else:
            print("Error: Respuesta vacía.")
    else:
        print(f"Error {response.status_code}: {response.text}")

    return None

def display_weather(weather_data):
    if weather_data and 'current_weather' in weather_data:
        temperature = weather_data['current_weather'].get('temperature_2m', 'N/A')
        description = weather_data['current_weather'].get('weathercode', 'N/A')
        print(f"The current temperature in Madrid is {temperature}°C with weather code {description}.")
    else:
        print("Error: Datos meteorológicos no disponibles.")

if __name__ == "__main__":
    city = 'New York'
    weather_data = get_weather(city)
    display_weather(weather_data)
