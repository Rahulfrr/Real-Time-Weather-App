from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# OpenWeatherMap API URL and your API key (sign up on https://openweathermap.org/api to get your key)
API_KEY = '8891f6c3b938b0ce9ade0358594925da'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city_name = request.form.get("city_name")  # Safer access to form data
        if city_name:
            # Make a request to the OpenWeatherMap API
            response = requests.get(BASE_URL, params={
                'q': city_name,
                'appid': API_KEY,
                'units': 'metric'  # Get temperature in Celsius
            })
            data = response.json()
            
            # If the response is successful
            if response.status_code == 200:
                weather_info = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "wind_speed": data["wind"]["speed"],
                    "weather_description": data["weather"][0]["description"],
                    "visibility": data.get("visibility", "No data") / 1000  # Visibility in km
                }

                # Safety Check Logic (based on simple thresholds)
                safety_message = "Safe to take off"
                
                # Wind speed (threshold in m/s)
                if weather_info["wind_speed"] > 15:  # Wind speed higher than 15 m/s
                    safety_message = "High winds! Not safe to take off."
                
                # Heavy rain or snow (checks based on weather condition)
                if "rain" in weather_info["weather_description"] or "snow" in weather_info["weather_description"]:
                    safety_message = "Heavy precipitation! Not safe to take off."
                
                # Poor visibility (in km, less than 5 km is risky)
                if weather_info["visibility"] < 5:
                    safety_message = "Poor visibility! Not safe to take off."

                return render_template("index.html", weather_info=weather_info, safety_message=safety_message)
            else:
                error_message = data.get("message", "City not found.")
                return render_template("index.html", error_message=error_message)
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
