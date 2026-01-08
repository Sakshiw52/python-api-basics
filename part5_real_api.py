
"""
Part 5: Real-World APIs - Weather & Crypto Dashboard
====================================================
Difficulty: Advanced
"""

import requests
from datetime import datetime


# ---------------- CITY COORDINATES ----------------
CITIES = {
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "bangalore": (12.9716, 77.5946),
    "chennai": (13.0827, 80.2707),
    "kolkata": (22.5726, 88.3639),
    "hyderabad": (17.3850, 78.4867),
    "new york": (40.7128, -74.0060),
    "london": (51.5074, -0.1278),
    "tokyo": (35.6762, 139.6503),
    "sydney": (-33.8688, 151.2093),
}


# ---------------- CRYPTO IDS ----------------
CRYPTO_IDS = {
    "bitcoin": "btc-bitcoin",
    "ethereum": "eth-ethereum",
    "dogecoin": "doge-dogecoin",
    "cardano": "ada-cardano",
    "solana": "sol-solana",
    "ripple": "xrp-xrp",
}


# ---------------- WEATHER FUNCTIONS ----------------
def get_weather(city_name):
    city = city_name.lower().strip()

    if city not in CITIES:
        print("City not found!")
        return None

    lat, lon = CITIES[city]

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "timezone": "auto"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Weather Error:", e)
        return None


def display_weather(city_name):
    data = get_weather(city_name)
    if not data:
        return

    weather = data["current_weather"]

    print("\n" + "=" * 40)
    print(f" Weather in {city_name.title()}")
    print("=" * 40)
    print(f" Temperature : {weather['temperature']}°C")
    print(f" Wind Speed  : {weather['windspeed']} km/h")
    print(f" Wind Dir    : {weather['winddirection']}°")
    print("=" * 40)


# ---------------- CRYPTO FUNCTIONS ----------------
def get_crypto_price(coin_name):
    coin = coin_name.lower().strip()
    coin_id = CRYPTO_IDS.get(coin, coin)

    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Crypto Error:", e)
        return None


def display_crypto(coin_name):
    data = get_crypto_price(coin_name)

    if not data:
        print("Coin not found!")
        return

    usd = data["quotes"]["USD"]

    print("\n" + "=" * 40)
    print(f" {data['name']} ({data['symbol']})")
    print("=" * 40)
    print(f" Price       : ${usd['price']:,.2f}")
    print(f" Market Cap  : ${usd['market_cap']:,.0f}")
    print(f" 24h Change  : {usd['percent_change_24h']:+.2f}%")
    print("=" * 40)


# ---------------- DASHBOARD ----------------
def dashboard():
    print("\n" + "=" * 50)
    print(" Real-World API Dashboard")
    print(datetime.now().strftime(" %Y-%m-%d %H:%M:%S"))
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("1. Check Weather")
        print("2. Check Crypto Price")
        print("3. Quick Dashboard (Delhi + Bitcoin)")
        print("4. Exit")

        choice = input("Choose (1-4): ").strip()

        if choice == "1":
            print("Available cities:", ", ".join(CITIES.keys()))
            city = input("Enter city: ")
            display_weather(city)

        elif choice == "2":
            print("Available cryptos:", ", ".join(CRYPTO_IDS.keys()))
            coin = input("Enter crypto: ")
            display_crypto(coin)

        elif choice == "3":
            display_weather("delhi")
            display_crypto("bitcoin")

        elif choice == "4":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice!")


# ---------------- MAIN ----------------
if __name__ == "__main__":
    dashboard()

# --- CHALLENGE EXERCISES ---
#
# Exercise 1: Add more cities to the CITIES dictionary
#             Find coordinates at: https://www.latlong.net/
#
# Exercise 2: Create a function that compares prices of multiple cryptos
#             Display them in a formatted table
#
# Exercise 3: Add POST request example
#             Use: https://jsonplaceholder.typicode.com/posts
#             Send: requests.post(url, json={"title": "My Post", "body": "Content"})
#
# Exercise 4: Save results to a JSON file
#             import json
#             with open("results.json", "w") as f:
#                 json.dump(data, f, indent=2)
#
# Exercise 5: Add API key support for OpenWeatherMap
#             Sign up at: https://openweathermap.org/api
#             Use environment variables:
#             import os
#             api_key = os.environ.get("OPENWEATHER_API_KEY")
