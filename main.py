import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget , QLabel , QLineEdit , QPushButton , QVBoxLayout)
from PyQt5.QtCore import Qt
from dotenv import load_dotenv
import os

load_dotenv()

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ",self)
        self.city_input = QLineEdit(self)
        self.get_weather_btn = QPushButton("Get Weather",self)
        self.temp = QLabel(self)
        self.emoji = QLabel(self)
        self.description = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_btn)
        vbox.addWidget(self.temp)
        vbox.addWidget(self.emoji)
        vbox.addWidget(self.description)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp.setAlignment(Qt.AlignCenter)
        self.emoji.setAlignment(Qt.AlignCenter)
        self.description.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.get_weather_btn.setObjectName("get_weather_btn")
        self.city_input.setObjectName("city_input")
        self.temp.setObjectName("temp")
        self.emoji.setObjectName("emoji")
        self.description.setObjectName("description")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input{
                font-size: 40px;
            }
            QPushButton#get_weather_btn{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temp{
                font-size: 75px;
            }
            QLabel#emoji{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#description{
                font-size: 50px;
            }
        """)

        self.get_weather_btn.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = os.getenv("API_key")
        city = self.city_input.text()
        url1 = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}"

        try:
            response1 = requests.get(url1)
            response1.raise_for_status()
            data1 = response1.json()[0]
            lat = data1["lat"]
            lon = data1["lon"]
            url2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
            response2 = requests.get(url2)
            response2.raise_for_status()
            data2 = response2.json()
            self.display_weather(data2)
        except requests.exceptions.HTTPError:
            match response1.status_code:
                case 400:
                    self.display_error("Bad request\nPlease check your input")
                case 404:
                    self.display_error("City not found")

    def display_error(self,message):
        self.temp.setStyleSheet("font-size: 30px;")
        self.temp.setText(message)

    def display_weather(self, data):
        temp_c = data["main"]["temp"] - 273.15
        self.temp.setText(f"{temp_c:.0f}°C")
        weather_description = data["weather"][0]["description"]
        self.description.setText(weather_description)
        weather_id = data["weather"][0]["id"]
        self.emoji.setText(self.get_weather_emoji(weather_id))

    def get_weather_emoji(self,weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌥️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "🌨️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 800:
            return "☀️"
        else:
            return "☀️"
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())