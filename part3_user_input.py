"""
Part 3: Dynamic Queries with User Input
=======================================
Difficulty: Intermediate
"""

import requests


# ======================================
# Helper: Input validation for user ID
# ======================================
def get_valid_user_id():
    user_id = input("Enter user ID (1-10): ").strip()

    if not user_id.isdigit():
        print("❌ Error: User ID must be a number.")
        return None

    user_id = int(user_id)
    if user_id < 1 or user_id > 10:
        print("❌ Error: User ID must be between 1 and 10.")
        return None

    return user_id


# ======================================
# Option 1: User Info
# ======================================
def get_user_info():
    print("\n=== User Information Lookup ===\n")

    user_id = get_valid_user_id()
    if user_id is None:
        return

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\n--- User #{user_id} Info ---")
        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Phone: {data['phone']}")
        print(f"Website: {data['website']}")
    else:
        print("User not found!")


# ======================================
# Option 2: Search Posts by User
# ======================================
def search_posts():
    print("\n=== Post Search ===\n")

    user_id = get_valid_user_id()
    if user_id is None:
        return

    url = "https://jsonplaceholder.typicode.com/posts"
    params = {"userId": user_id}

    response = requests.get(url, params=params)
    posts = response.json()

    if posts:
        print(f"\n--- Posts by User #{user_id} ---")
        for i, post in enumerate(posts, 1):
            print(f"{i}. {post['title']}")
    else:
        print("No posts found.")


# ======================================
# Option 3: Crypto Price
# ======================================
def get_crypto_price():
    print("\n=== Cryptocurrency Price Checker ===\n")
    print("Available: btc-bitcoin, eth-ethereum, doge-dogecoin")

    coin_id = input("Enter coin ID: ").strip().lower()
    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        usd = data["quotes"]["USD"]
        print(f"\n{data['name']} ({data['symbol']})")
        print(f"Price: ${usd['price']:,.2f}")
        print(f"24h Change: {usd['percent_change_24h']:+.2f}%")
    else:
        print("Invalid coin ID!")


# =================================================
# EXERCISE 1: Weather by City (Open-Meteo API)
# =================================================
def get_weather():
    print("\n=== Weather Checker ===\n")

    cities = {
        "delhi": (28.61, 77.23),
        "mumbai": (19.07, 72.87),
        "pune": (18.52, 73.85)
    }

    print("Available cities:", ", ".join(cities.keys()))
    city = input("Enter city name: ").strip().lower()

    if city not in cities:
        print("City not available.")
        return

    lat, lon = cities[city]
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    response = requests.get(url, params=params)
    data = response.json()
    weather = data["current_weather"]

    print(f"\nWeather in {city.title()}:")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Wind Speed: {weather['windspeed']} km/h")


# =================================================
# EXERCISE 2: Search Todos by Completion Status
# =================================================
def search_todos():
    print("\n=== Todo Search ===\n")

    status = input("Enter status (true/false): ").strip().lower()

    if status not in ["true", "false"]:
        print("Invalid input! Use true or false.")
        return

    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"completed": status}

    response = requests.get(url, params=params)
    todos = response.json()

    print(f"\nShowing first 5 todos (completed={status}):")
    for todo in todos[:5]:
        print(f"- {todo['title']}")


# ======================================
# Main Menu
# ======================================
def main():
    print("=" * 45)
    print("   Dynamic API Query Demo")
    print("=" * 45)

    while True:
        print("\n1. Look up user info")
        print("2. Search posts by user")
        print("3. Check crypto price")
        print("4. Check weather")
        print("5. Search todos")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ")

        if choice == "1":
            get_user_info()
        elif choice == "2":
            search_posts()
        elif choice == "3":
            get_crypto_price()
        elif choice == "4":
            get_weather()
        elif choice == "5":
            search_todos()
        elif choice == "6":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()


# --- EXERCISES ---
#
# Exercise 1: Add a function to fetch weather for a city
#             Use Open-Meteo API (no key required):
#             https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true
#             Challenge: Let user input city name (you'll need to find lat/long)
#
# Exercise 2: Add a function to search todos by completion status
#             URL: https://jsonplaceholder.typicode.com/todos
#             Params: completed=true or completed=false
#
# Exercise 3: Add input validation (check if user_id is a number)
