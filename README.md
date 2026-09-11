# Weather App 🌤️

A simple desktop weather application built using **Python**, **PyQt5**, and the **OpenWeatherMap API**.

The application allows the user to enter a city name and displays the current temperature, weather condition, and a corresponding weather emoji.

## Features

* 🌍 Search weather by city name
* 🌡️ Display current temperature in Celsius
* ☁️ Display weather description
* 🌦️ Display weather-based emoji
* ❌ Handles invalid city names and API errors
* 🖥️ Simple PyQt5 graphical user interface

## Technologies Used

* Python
* PyQt5
* Requests
* OpenWeatherMap API

## Project Structure

```text
Weather_py/
│
├── main.py
├── README.md
├── .gitignore
└── .env
```

## Requirements

Make sure Python is installed on your system.

Install the required packages:

```bash
pip install PyQt5 requests python-dotenv
```

## API Key Setup

This project uses the OpenWeatherMap API.

Create a `.env` file in the project directory:

```text
API_KEY=your_api_key_here
```

The API key is loaded using `python-dotenv`.

Make sure `.env` is included in `.gitignore` so your API key is not uploaded to GitHub.

## How to Run

Clone the repository:

```bash
git clone https://github.com/kshitijpachpande12-max/Weather_App
```

Move into the project directory:

```bash
cd Weather_py
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Then run:

```bash
python main.py
```

## How It Works

1. Enter a city name in the input field.
2. Click **Get Weather**.
3. The application uses the OpenWeatherMap Geocoding API to obtain the city's latitude and longitude.
4. It then uses the latitude and longitude to request current weather data.
5. The application displays:

   * Temperature
   * Weather description
   * Weather emoji

## Example

Enter:

```text
Bangalore
```

The application will display the current weather information for the city.

## Future Improvements

* Add humidity and wind speed
* Add weather forecast for multiple days
* Add a better GUI design
* Add automatic location-based weather
* Add weather icons
* Add loading indicators
* Improve error handling

## License

This project is for learning and personal use.
