import streamlit as st
import requests
from datetime import datetime
from collections import defaultdict

API_KEY = 'YOUR API KEY'

# Set page configuration
st.set_page_config(page_title="Weather App", page_icon="🌤️")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .header-section {
        background-image: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        background-position: center;
        padding: 20px;
        display: flex;
        align-items: center;
        gap: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    .main {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #fff; /* Set text to white */
    }

    .section {
        background-color: transparent;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        font-weight: bold;
        color: #fff; /* White text inside sections */
    }

    .section-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 15px;
        font-size: 24px;
        font-weight: 700;
        color: #fff;
    }

    .weather-icon {
        width: 50px;
        height: 50px;
    }

    .weather-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
        color: #fff;
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        font-size: 20px; /* Larger text size */
    }

    .forecast-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        margin-top: 10px;
        color: #fff;
        font-size: 20px;
    }

    .forecast-item {
        border-bottom: 1px solid #ccc;
        padding: 10px 0;
    }

    .button-row {
        display: flex;
        gap: 10px;
        align-items: center;
        margin-top: 10px;
    }

    div.stButton > button {
        background-color: #003366;
        color: #ffffff;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
        border-radius: 8px;
        cursor: pointer;
        font-size: 16px;
    }
    div.stButton > button:hover {
        background-color: #0055aa;
    }

    .footer {
        text-align: center;
        padding: 15px;
        font-size: 16px;
        background-color: rgba(0,0,0,0.2);
        margin-top: 40px;
        border-radius: 10px;
        color: #fff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main">', unsafe_allow_html=True)

st.markdown(
    """
    <div class="header-section">
        <img src="https://img.icons8.com/ios-filled/50/ffffff/partly-cloudy-day.png" width="50" height="50" alt="Weather Icon"/>
        <h1 style="margin:0;color:red;text-align:center;"> SKYSENSE</h1>
    </div>
    """,
    unsafe_allow_html=True
)

unit_option = st.radio(
    "Select Temperature Unit:",
    ('Celsius', 'Fahrenheit')
)

st.sidebar.header("Search for a city's weather")
city_input = st.sidebar.text_input("City", "London")

st.markdown("### Or enter your location manually")
lat = st.number_input("Latitude", -90.0, 90.0, step=0.0001)
lon = st.number_input("Longitude", -180.0, 180.0, step=0.0001)

def format_time(ts):
    return datetime.fromtimestamp(ts).strftime('%H:%M:%S')

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fetch_weather_by_coords(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        if unit_option == 'Fahrenheit':
            data['main']['temp'] = celsius_to_fahrenheit(data['main']['temp'])
            data['main']['temp_min'] = celsius_to_fahrenheit(data['main']['temp_min'])
            data['main']['temp_max'] = celsius_to_fahrenheit(data['main']['temp_max'])
        return data
    return None

def fetch_weather_by_city(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        if unit_option == 'Fahrenheit':
            data['main']['temp'] = celsius_to_fahrenheit(data['main']['temp'])
            data['main']['temp_min'] = celsius_to_fahrenheit(data['main']['temp_min'])
            data['main']['temp_max'] = celsius_to_fahrenheit(data['main']['temp_max'])
        return data
    return None

def fetch_forecast_by_city(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    resp = requests.get(url)
    if resp.status_code == 200:
        forecast = resp.json()
        if unit_option == 'Fahrenheit':
            for e in forecast['list']:
                e['main']['temp'] = celsius_to_fahrenheit(e['main']['temp'])
        return forecast
    return None

col1, col2 = st.columns(2)
with col1:
    get_coords = st.button("Get Weather at Coordinates")
with col2:
    get_city = st.button(f"Get Weather for {city_input}")

if get_coords:
    weather = fetch_weather_by_coords(lat, lon)
    forecast = None
    if weather:
        icon_code = weather['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        st.markdown('<div class="section">', unsafe_allow_html=True)
        # Header with icon only
        st.markdown(
            f"""
            <div class="section-header">
                <img src="{icon_url}" class="weather-icon"/>
                <span>Current Weather</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        # Two-columns aligned current weather info
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                f"""
                <div class="weather-box" style="text-align:center;">
                    <p style="font-size:22px;"><strong>Description:</strong> {weather['weather'][0]['description'].capitalize()}</p>
                    <p style="font-size:22px;"><strong>Temp:</strong> {weather['main']['temp']:.1f}°{'F' if unit_option=='Fahrenheit' else 'C'}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                f"""
                <div class="weather-box" style="text-align:center;">
                    <p style="font-size:22px;"><strong>Humidity:</strong> {weather['main']['humidity']}%</p>
                    <p style="font-size:22px;"><strong>Sunrise:</strong> {format_time(weather['sys']['sunrise'])}</p>
                    <p style="font-size:22px;"><strong>Sunset:</strong> {format_time(weather['sys']['sunset'])}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)
        st.map([{'lat': lat, 'lon': lon}])
    else:
        st.error("Unable to fetch weather data at provided coordinates.")

if get_city:
    with st.spinner("Loading weather data..."):
        weather = fetch_weather_by_city(city_input)
        forecast = fetch_forecast_by_city(city_input)
        if weather:
            icon_code = weather['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
            st.markdown('<div class="section">', unsafe_allow_html=True)
            # Head with icon only
            st.markdown(
                f"""
                <div class="section-header">
                    <img src="{icon_url}" class="weather-icon"/>
                    <span>Current Weather</span>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown(
                f"""
                <div class="weather-box">
                    <div style="display:flex; justify-content:space-around;">
                        <div style="width:45%; text-align:center;">
                            <p style="font-size:22px;"><strong>Description:</strong> {weather['weather'][0]['description'].capitalize()}</p>
                            <p style="font-size:22px;"><strong>Temp:</strong> {weather['main']['temp']:.1f}°{'F' if unit_option=='Fahrenheit' else 'C'}</p>
                        </div>
                        <div style="width:45%; text-align:center;">
                            <p style="font-size:22px;"><strong>Humidity:</strong> {weather['main']['humidity']}%</p>
                            <p style="font-size:22px;"><strong>Sunrise:</strong> {format_time(weather['sys']['sunrise'])}</p>
                            <p style="font-size:22px;"><strong>Sunset:</strong> {format_time(weather['sys']['sunset'])}</p>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Five-day forecast in a styled box
            if 'list' in forecast:
                st.markdown('<div class="forecast-box">', unsafe_allow_html=True)
                st.markdown(
                    """
                    <div class="section-header">
                        <img src="https://img.icons8.com/ios-filled/50/007BFF/calendar.png" class="weather-icon"/>
                        <span>5-Day Forecast</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                forecast_list = forecast['list']
                daily = defaultdict(list)
                for e in forecast_list:
                    date_str = e['dt_txt'].split(' ')[0]
                    daily[date_str].append(e)
                for date_str in sorted(daily)[:5]:
                    entries = daily[date_str]
                    temps = [e['main']['temp'] for e in entries]
                    min_t, max_t = min(temps), max(temps)
                    icon_code = entries[0]['weather'][0]['icon']
                    desc = entries[0]['weather'][0]['description'].capitalize()
                    date_fmt = datetime.strptime(date_str, '%Y-%m-%d').strftime('%A, %b %d')
                    with st.expander(date_fmt):
                        col1, col2 = st.columns([1, 3])
                        with col1:
                            st.image(f"http://openweathermap.org/img/wn/{icon_code}@2x.png")
                        with col2:
                            st.write(f"**{desc}**")
                            st.write(f"Min: {min_t:.1f}{'°F' if unit_option=='Fahrenheit' else '°C'}")
                            st.write(f"Max: {max_t:.1f}{'°F' if unit_option=='Fahrenheit' else '°C'}")
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.error("Weather forecast data not available.")
        else:
            st.error("Failed to fetch weather data.")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="footer">
        © 2025  Weather App | Designed for quick weather info & forecasts | Enjoy your day!
    </div>
    """,
    unsafe_allow_html=True
)
