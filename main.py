import requests
import os


# Telegram Bot
def bot_message(chat_id):
    token = os.environ.get("TELEGRAM_TOKEN")
    message = "Don't forget your umbrella."
    send = "https://api.telegram.org/bot" + token + "/sendmessage?chat_id=" + chat_id + "&text=" + message
    bot_response = requests.get(send)
    return bot_response.json()


chat_ids = "chat id here"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")

# Geographical coordinates (lat: latitude, lon: longitude)
params = {
    "lat": 0,
    "lon": 0,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(url=OWM_endpoint, params=params)
response.raise_for_status()
weather_data = response.json()
# Slice the data (next 12 hours)
weather_hour = weather_data["hourly"][:12]

# Check the weather condition
for hour in weather_hour:
    condition_code = int(hour["weather"][0]["id"])
    # Codes below 700 means: rain, snow, drizzle or thunderstorm
    if condition_code < 700:
        # Send the umbrella reminder
        bot_message(chat_ids)
