Real-Time Weather Monitoring & Flight Safety Recommendation System

A Python + Flask based real-time weather monitoring system that fetches
live meteorological data using the OpenWeatherMap API and provides
automated flight safety recommendations for air traffic controllers.

FEATURES: - Live Weather Data (Temperature, Humidity, Wind Speed,
Visibility, Conditions) - Automated Flight Safety Recommendations -
Interactive Web Interface using HTML, CSS, JS - Backend weather logic
using Python & Flask

INSTALLATION: 1. Clone the repository: git clone
https://github.com/your-username/weather-monitoring-system.git

2.  Install dependencies: pip install -r requirements.txt

3.  Add your OpenWeatherMap API Key inside app.py: API_KEY =
    “your_api_key_here”

4.  Run application: python app.py

5.  Open in browser: http://127.0.0.1:5000/

FLIGHT SAFETY RULES: - Wind Speed > 15 m/s → Risky - Visibility < 5000 m
→ Not Safe - Rain/Snow detected → Unsafe - Otherwise → Safe to Take Off

PROJECT STRUCTURE: app.py templates/index.html static/style.css
static/script.js requirements.txt README.md

LICENSE: MIT License
