import tkinter as tk
import time
import math
from datetime import datetime, date

# --- Weather Info ---
weather_data = {
    "New York": "15°C, Cloudy ☁️",
    "Tokyo": "22°C, Sunny ☀️",
    "London": "12°C, Rain 🌧️",
    "Karachi": "34°C, Clear 🌤️"
}

# --- Main Window ---
root = tk.Tk()
root.title("Hybrid Clock – Analog + Digital 🕰️")
root.geometry("500x700")
root.configure(bg='#0f111a')

# --- Canvas ---
canvas = tk.Canvas(root, width=400, height=400, bg='#0f111a', highlightthickness=0)
canvas.pack(pady=20)

center_x = 200
center_y = 200
radius = 150

# --- Clock Outline ---
canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline='#00ffe1', width=5)

# --- Minute Marks (60) ---
for i in range(60):
    angle = math.radians(i * 6)
    x1 = center_x + math.cos(angle) * (radius - 5)
    y1 = center_y + math.sin(angle) * (radius - 5)
    x2 = center_x + math.cos(angle) * (radius - 10)
    y2 = center_y + math.sin(angle) * (radius - 10)
    canvas.create_line(x1, y1, x2, y2, fill='gray', width=1)

# --- Hour Marks (12 big dots) ---
for hour in range(1, 13):
    angle = math.radians((hour - 3) * 30)
    x = center_x + math.cos(angle) * (radius - 15)
    y = center_y + math.sin(angle) * (radius - 15)
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='white', outline='cyan')

# --- Numbers ---
for hour in range(1, 13):
    angle = math.radians((hour - 3) * 30)
    x = center_x + math.cos(angle) * (radius - 35)
    y = center_y + math.sin(angle) * (radius - 35)
    canvas.create_text(x, y, text=str(hour), fill='#00ffe1', font=('Helvetica', 14, 'bold'))

# --- Clock Hands ---
sec_hand = canvas.create_line(center_x, center_y, center_x, center_y - radius + 20, fill='red', width=1)
min_hand = canvas.create_line(center_x, center_y, center_x, center_y - radius + 30, fill='white', width=3)
hour_hand = canvas.create_line(center_x, center_y, center_x, center_y - radius + 50, fill='cyan', width=6)

# --- Center Glow ---
canvas.create_oval(center_x - 7, center_y - 7, center_x + 7, center_y + 7, fill='white', outline='#00ffe1', width=2)

# --- Digital Clock (Outside Analog Circle) ---
digital_label = tk.Label(root, text='', font=('Orbitron', 22, 'bold'), fg='lightgreen', bg='#0f111a')
digital_label.pack(pady=10)

# --- Date Label ---
today = date.today().strftime("%A, %d %B %Y")
date_label = tk.Label(root, text=today, font=('Arial', 14), fg='white', bg='#0f111a')
date_label.pack()

# --- Weather Dropdown ---
def show_weather(city):
    weather = weather_data.get(city, "No data")
    weather_label.config(text=f"{city}: {weather}")

city_var = tk.StringVar()
city_var.set("Select City")
city_menu = tk.OptionMenu(root, city_var, *weather_data.keys(), command=show_weather)
city_menu.config(bg='#21252f', fg='white', font=('Arial', 12), width=15)
city_menu.pack(pady=10)

weather_label = tk.Label(root, text='', font=('Arial', 14), fg='#00ffe1', bg='#0f111a')
weather_label.pack()

# --- Clock Update Function ---
def update_clock():
    now = datetime.now()
    sec = now.second
    min = now.minute
    hour = now.hour % 12 + min / 60.0

    # Angles
    sec_angle = math.radians((sec - 15) * 6)
    min_angle = math.radians((min - 15) * 6)
    hour_angle = math.radians((hour - 3) * 30)

    # Sec Hand
    x_sec = center_x + math.cos(sec_angle) * (radius - 20)
    y_sec = center_y + math.sin(sec_angle) * (radius - 20)
    canvas.coords(sec_hand, center_x, center_y, x_sec, y_sec)

    # Min Hand
    x_min = center_x + math.cos(min_angle) * (radius - 40)
    y_min = center_y + math.sin(min_angle) * (radius - 40)
    canvas.coords(min_hand, center_x, center_y, x_min, y_min)

    # Hour Hand
    x_hour = center_x + math.cos(hour_angle) * (radius - 60)
    y_hour = center_y + math.sin(hour_angle) * (radius - 60)
    canvas.coords(hour_hand, center_x, center_y, x_hour, y_hour)

    # Digital Clock
    current_time = now.strftime("%I:%M:%S %p")
    digital_label.config(text=current_time)

    root.after(1000, update_clock)

update_clock()
root.mainloop()
