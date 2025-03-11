from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/weather",methods =['post'])
def get_weather():
    city =request.form['city']
    api_key ="cdf5379c32119b0241d242a93f5d40db"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    temp = response['main']['temp']
    desc = response['weather'][0]['description']
    if "sun" in desc.lower():
        weather_class = "sunny"
    elif "rain" in desc.lower():
        weather_class = "rainy"
    elif "cloud" in desc.lower():
        weather_class = "cloudy"
    else:
        weather_class = "default"
    return render_template('index.html', temperature=temp, description=desc, weather_class=weather_class)
    

if __name__ == '__main__':
    app.run(debug=True)