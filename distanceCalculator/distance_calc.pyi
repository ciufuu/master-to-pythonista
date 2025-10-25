import openrouteservice
from geopy.geocoders import Nominatim
from time import sleep

# ===============================
# CONFIGURATION
# ===============================

API_KEY = " "  # <-- replace with your real key
client = openrouteservice.Client(key=API_KEY)
geolocator = Nominatim(user_agent="geoapp")


locations = {
    "Bucharest": [26.1025, 44.4268],
    "Brasov": [25.5948, 45.6580],
    "Cluj": [23.5940, 46.7712],
    "Iasi": [27.6014, 47.1585]
}

# ===============================
# FUNCTIONS
# ===============================

def get_coordinates(place_name):
    """Use geopy to obtain coordinates for a place."""
    try:
        location = geolocator.geocode(place_name)
        sleep(1)  # short pause to avoid overloading Nominatim
        if location:
            # openrouteservice expects [lon, lat]
            return [location.longitude, location.latitude]
        else:
            print("⚠️ Location could not be found.")
            return None
    except Exception as e:
        print("❌ Error obtaining coordinates:", e)
        return None

def add_location():
    """Allow the user to add a new location using geocoding."""
    name = input("Enter place name (e.g. Timișoara, Paris): ").strip()
    coords = get_coordinates(name)
    if coords:
        locations[name] = coords
        print(f"✅ Location '{name}' has been added: {coords}")
    else:
        print("⚠️ Location was not added.")

def show_locations():
    """Display all available locations."""
    print("\n📍 Available locations:")
    for name, coords in locations.items():
        print(f" - {name}: {coords}")
    print()

def calculate_distance():
    """Calculate driving distance between two locations."""
    show_locations()
    start = input("From location: ").strip()
    end = input("To location: ").strip()

    if start not in locations or end not in locations:
        print("⚠️ One of the locations is missing. Add it first!")
        return

    start_coords = locations[start]
    end_coords = locations[end]

    try:
        route = client.directions(
            coordinates=[start_coords, end_coords],
            profile='driving-car',
            format='geojson'
        )
        props = route['features'][0]['properties']['segments'][0]
        dist_km = props['distance'] / 1000
        duration_h = props['duration'] / 3600

        print(f"\n🛣️ Driving distance between {start} and {end}: {dist_km:.2f} km")
        print(f"⏱️ Estimated duration: {duration_h:.2f} hours\n")

    except Exception as e:
        print("❌ Error calculating the route:", e)

# ===============================
# MENU
# ===============================

while True:
    print("""
=== MENU ===
1. Show locations
2. Add a location (geocode)
3. Calculate distance between two locations
0. Exit
""")
    opt = input("Choose an option: ").strip()

    if opt == "1":
        show_locations()
    elif opt == "2":
        add_location()
    elif opt == "3":
        calculate_distance()
    elif opt == "0":
        print("👋 Exiting program.")
        break
    else:
        print("⚠️ Invalid option. Try again.")
