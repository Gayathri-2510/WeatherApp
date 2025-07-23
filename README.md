---

# Weather App with Enhanced Features

## Overview

This Weather App is a modern, visually appealing web application built using Streamlit, designed to provide real-time weather information and forecasts for any location specified by the user. The app features a sleek user interface with custom styling, multiple data presentation options, and several useful functionalities aimed at enhancing user experience.

---

## Features

- **Current Weather Display:** Provides detailed current weather data including temperature, humidity, weather description, sunrise, and sunset times.
- **5-Day Forecast:** Presents an easy-to-understand 5-day weather forecast in a styled box with expandable daily summaries.
- **Multiple Input Methods:** Users can search by city name or manually input latitude and longitude coordinates.
- **Unit Toggle:** Switch between Celsius and Fahrenheit temperature units seamlessly.
- **Dynamic Icons:** Weather icons update based on real-time conditions for visual clarity.
- **Responsive Layout:** Utilizes multi-column design for aligned data presentation.
- **Custom Styling:** Rich CSS styling for headers, boxes, and footer for a professional look.
- **Footer Section:** Includes a footer with app information and branding.

---

## Additional Planned Features (Future Enhancements)

1. **Temperature Conversion Button:** Instantly switch between Celsius and Fahrenheit.
2. **Favorite Cities Management:** Save and access favorite locations for quick retrieval.
3. **Weather Alerts:** Show alerts or warnings if severe weather conditions are detected.
4. **Geolocation Button:** Use browser geolocation to fetch weather for the user's current location.
5. **Daily Weather Tips:** Display daily tips or weather facts to educate users.

---

## Technologies & Dependencies

- **Streamlit:** For building interactive web apps with Python.
- **Requests:** To fetch weather data from the OpenWeatherMap API.
- **OpenWeatherMap API:** Provides real-time weather data and forecasts.
- **Python Standard Library:** For date/time formatting and data handling.

**Note:** Ensure you have the following installed:

```bash
pip install streamlit requests
```

---

## Setup & Usage

### Prerequisites

- Python 3.7+
- An OpenWeatherMap API key (sign up at https://openweathermap.org/api)

### Steps

1. **Clone or download this repository.**

2. **Obtain an API Key:**
   - Sign up at [OpenWeatherMap](https://openweathermap.org/api).
   - Generate an API key and replace `'YOUR_API_KEY'` in the code with your actual key.

3. **Run the app:**
   
```bash
streamlit run your_script_name.py
```

4. **Open the URL provided in your terminal (usually http://localhost:8501).**

---

## Customization & Extension

- **Styling:** Modify the embedded CSS in the code for further customization of the app’s appearance.
- **Features:** Implement the planned additional features such as favorite management, weather alerts, or geolocation using Streamlit plugins or additional APIs.
- **Data Sources:** Integrate other weather data providers for more comprehensive information.

---

## Code Structure Overview

- **Header Section:** Features a background image and app title with an icon.
- **Input Section:** Allows city search or manual coordinate input.
- **Weather Display:**
  - **Current Weather:** Shown in a styled box with aligned columns for clarity.
  - **Forecast:** 5-day forecast displayed inside a styled box with expandable daily summaries.
- **Footer:** Contains app branding and information.
- **CSS Styling:** Embedded in the app for consistent visual design.

---

## Support

For issues, feature requests, or contributions, please open an issue or pull request in the repository.

---

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [OpenWeatherMap](https://openweathermap.org/)
- [Icons8](https://icons8.com/icons)

---