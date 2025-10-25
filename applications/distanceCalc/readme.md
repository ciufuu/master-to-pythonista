# 🗺️ Python Distance Calculator

A small Python app that shows driving distances and travel times between cities using **OpenRouteService** and **Geopy**.

---

## ⚙️ What it does
- Shows a list of predefined cities  
- Lets you add new ones (geocoding via Geopy + Nominatim)  
- Calculates driving distance and duration between two places  

---

## 🧩 Setup
Install dependencies:
```bash
pip install openrouteservice geopy
```

Set your OpenRouteService API key in the script before running:
```python
API_KEY = "YOUR_KEY_HERE"
```
> ⚠️ The key in the code should **not be your real key** if the repo is public.

You can get a free key here: [OpenRouteService Signup](https://openrouteservice.org/dev/#/signup)

---

## ▶️ Run it
```bash
python distance_calculator.py
```

Menu example:
```
1. Show locations
2. Add a location
3. Calculate distance
0. Exit
```

---

## 💬 Example Output
```
🛣️ Distance between Bucharest and Brasov: 166.4 km
⏱️ Duration: 2.4 hours
```

---

Made for fun and learning 🌍
