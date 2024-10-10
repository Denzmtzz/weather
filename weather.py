import requests

API_KEY = '0508b5e6db9b6fb4dea69718840'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

city = input("Enter city name: ")
request_url = f"{BASE_URL}q={city}&appid={0508b5e6db9b6fb4dea69718840}&units=metric"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    main = data['main']
    temperature = main['temp']
    weather = data['weather'][0]['description']
    print(f"Temperature: {temperature}°C")
    print(f"Weather: {weather}")
else:
    print("City not found.")

