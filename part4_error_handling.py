"""
Part 4: Robust Error Handling
=============================
Difficulty: Intermediate+

Learn:
- Try/except blocks for API requests
- Handling network errors
- Timeout handling
- Response validation
- Retry logic
- Logging
"""

import requests
import time
import logging
from requests.exceptions import (
    ConnectionError,
    Timeout,
    HTTPError,
    RequestException
)

# ---------------- LOGGING SETUP (Exercise 3) ----------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------------- SAFE API REQUEST WITH RETRY (Exercise 1) ----------------
def safe_api_request(url, timeout=5, retries=3):
    """Make an API request with retry and logging."""
    for attempt in range(1, retries + 1):
        try:
            logging.info(f"Attempt {attempt}: Requesting {url}")
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
            return {"success": True, "data": response.json()}

        except ConnectionError:
            logging.error("Connection failed")

        except Timeout:
            logging.error(f"Request timed out after {timeout} seconds")

        except HTTPError as e:
            logging.error(f"HTTP Error: {e.response.status_code}")
            break  # no retry for HTTP errors

        except RequestException as e:
            logging.error(f"Request failed: {e}")

        time.sleep(1)

    return {"success": False, "error": "All retry attempts failed"}

# ---------------- CRYPTO RESPONSE VALIDATION (Exercise 2) ----------------
def validate_crypto_response(data):
    """Validate crypto API response structure."""
    if "quotes" not in data:
        return False

    if "USD" not in data["quotes"]:
        return False

    return True

# ---------------- DEMO ERROR HANDLING ----------------
def demo_error_handling():
    print("=== Error Handling Demo ===\n")

    print("--- Test 1: Valid URL ---")
    result = safe_api_request("https://jsonplaceholder.typicode.com/posts/1")
    if result["success"]:
        print("Success:", result["data"]["title"])
    else:
        print("Failed:", result["error"])

    print("\n--- Test 2: 404 Error ---")
    result = safe_api_request("https://jsonplaceholder.typicode.com/posts/99999")
    print("Result:", result["error"])

    print("\n--- Test 3: Invalid Domain ---")
    result = safe_api_request("https://invalid-domain-xyz.com")
    print("Result:", result["error"])

    print("\n--- Test 4: Timeout ---")
    result = safe_api_request("https://httpstat.us/200?sleep=5000", timeout=1)
    print("Result:", result["error"])

# ---------------- SAFE CRYPTO FETCH ----------------
def fetch_crypto_safely():
    print("\n=== Safe Crypto Price Checker ===\n")
    coin = input("Enter coin (btc-bitcoin, eth-ethereum): ").strip().lower()

    if not coin:
        print("Invalid input")
        return

    url = f"https://api.coinpaprika.com/v1/tickers/{coin}"
    result = safe_api_request(url)

    if result["success"] and validate_crypto_response(result["data"]):
        usd = result["data"]["quotes"]["USD"]
        print(f"\n{result['data']['name']} ({result['data']['symbol']})")
        print(f"Price: ${usd['price']:,.2f}")
        print(f"24h Change: {usd['percent_change_24h']:+.2f}%")
    else:
        print("Invalid crypto data or request failed")

# ---------------- JSON VALIDATION ----------------
def validate_json_response():
    print("\n=== JSON Validation Demo ===\n")

    url = "https://jsonplaceholder.typicode.com/users/1"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        required_fields = ["name", "email", "phone"]
        missing = [f for f in required_fields if f not in data]

        if missing:
            print("Missing fields:", missing)
        else:
            print("All required fields present")
            print(data["name"], data["email"], data["phone"])

    except Exception as e:
        print("Error:", e)

# ---------------- MAIN ----------------
def main():
    demo_error_handling()
    print("\n" + "=" * 40)
    validate_json_response()
    print("\n" + "=" * 40)
    fetch_crypto_safely()

if __name__ == "__main__":
    main()

# --- EXERCISES ---
#
# Exercise 1: Add retry logic - if request fails, try again up to 3 times
#             Hint: Use a for loop and time.sleep() between retries
#
# Exercise 2: Create a function that validates crypto response
#             Check that 'quotes' and 'USD' keys exist before accessing
#
# Exercise 3: Add logging to track all API requests
#             import logging
#             logging.basicConfig(level=logging.INFO)
