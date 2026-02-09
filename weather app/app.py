import tkinter as tk
from tkinter import messagebox
import requests
API_KEY = "92ae672786a1a580be30806e815e20ba"
def get_weather():
    try:
        city_name = city_entry.get()

        if city_name == "":
            messagebox.showwarning("Input Error", "Please enter a city name")
            return
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            raise Exception(data.get("message"))
        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"].title()
        location_label.config(text=f"📍 Location: {city}, {country}")
        temp_label.config(text=f"🌡 Temperature: {temp} °C")
        humidity_label.config(text=f"💧 Humidity: {humidity} %")
        weather_label.config(text=f"☁ Weather: {weather}")
    except Exception:
        messagebox.showerror("Error", "Unable to fetch weather data")
# GUI setup
root = tk.Tk()
root.title("Weather Forecast App")
root.geometry("350x350")
tk.Label(root, text="Weather Forecast", font=("Arial", 16)).pack(pady=10)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)
city_entry.insert(0, "Chennai")
tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)
location_label = tk.Label(root, text="📍 Location: -")
location_label.pack()
temp_label = tk.Label(root, text="🌡 Temperature: -")
temp_label.pack()
humidity_label = tk.Label(root, text="💧 Humidity: -")
humidity_label.pack()
weather_label = tk.Label(root, text="☁ Weather: -")
weather_label.pack()
root.mainloop()