import requests

API_KEY = 'YOUR_API_KEY'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

city = input("Sacramento: ")
request_url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
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

