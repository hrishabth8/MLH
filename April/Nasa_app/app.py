import os
import requests
from flask import Flask, render_template
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

NASA_API_KEY = os.getenv("NASA_API_KEY")
NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"


@app.route("/")
def home():
    # Fetch data from NASA's APOD API
    params = {"api_key": NASA_API_KEY}
    response = requests.get(NASA_APOD_URL, params=params)
    if response.status_code == 200:
        apod_data = response.json()
        return render_template("index.html", apod=apod_data)
    else:
        return "Failed to fetch data from NASA API. Please try again later."


if __name__ == "__main__":
    app.run(debug=True)
