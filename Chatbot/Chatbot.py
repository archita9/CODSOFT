import re
import requests

API_KEY = "c21819d69d6586e4ac38e549612dd69f"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

print("Hello! I am your Weather Chatbot 🌦️")
city = input("Enter your city name: ")

# Prepare API request
params = {
    'q': city,
    'appid': API_KEY,
    'units': 'metric'  # for temperature in Celsius
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    weather_description = data['weather'][0]['description']
    print(f"🌤️ The temperature in {city} is {temp}°C with {weather_description}.")
else:
    print("❌ Sorry, I couldn't find the weather for that city. Please check the spelling!")


print("Hello! I'm your rule-based chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    # Exit condition
    if re.search(r'\b(bye|exit|quit)\b', user_input):
        print("Chatbot: Goodbye! Take care!")
        break

    # Greeting
    elif re.search(r'\b(hi|hello|hey)\b', user_input):
        print("Chatbot: Hey there! How can I assist you?")

    # How are you
    elif re.search(r'how are you', user_input):
        print("Chatbot: I'm doing great! Thanks for asking. How about you?")

    # Name
    elif re.search(r'\b(name|who are you)\b', user_input):
        print("Chatbot: I'm your friendly rule-based chatbot!")

    # Help
    elif re.search(r'\b(help|support)\b', user_input):
        print("Chatbot: Sure, I'm here to help! Tell me your issue.")

    # Weather with real API
    elif re.search(r'weather', user_input):
        match = re.search(r'weather in (\w+)', user_input)
        if match:
            city = match.group(1)
            weather_info = get_weather(city)
            print(f"Chatbot: {weather_info}")
        else:
            print("Chatbot: Please mention the city name like 'weather in Delhi'.")

    # Default fallback
    else:
        print("Chatbot: Sorry, I'm still learning. Can you say it differently?")


