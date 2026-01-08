"""
Part 1: Basic GET Request
=========================
Difficulty: Beginner

Learn: How to make a simple GET request and view the response.

We'll use JSONPlaceholder - a free fake API for testing.
"""

"""
Part 1: Basic GET Request
=========================
Difficulty: Beginner
"""

import requests

# =========================
# Exercise 1: Fetch post 5
# =========================
url1 = "https://jsonplaceholder.typicode.com/posts/5"
response1 = requests.get(url1)

print("=== Exercise 1: Fetch Post 5 ===\n")
print(f"URL: {url1}")
print(f"Status Code: {response1.status_code}")
print("Response Data:")
print(response1.json())


# =========================
# Exercise 2: Fetch all users
# =========================
url2 = "https://jsonplaceholder.typicode.com/users"
response2 = requests.get(url2)

print("\n=== Exercise 2: Fetch All Users ===\n")
print(f"URL: {url2}")
print(f"Status Code: {response2.status_code}")
print("Response Data:")
print(response2.json())


# =========================
# Exercise 3: Fetch non-existing post
# =========================
url3 = "https://jsonplaceholder.typicode.com/posts/999"
response3 = requests.get(url3)

print("\n=== Exercise 3: Fetch Non-Existing Post ===\n")
print(f"URL: {url3}")
print(f"Status Code: {response3.status_code}")
print("Response Data:")
print(response3.json())


# --- EXERCISES ---
# Try these on your own:
#
# Exercise 1: Change the URL to fetch post number 5
#             Hint: Change /posts/1 to /posts/5

# Exercise 2: Fetch a list of all users
#             URL: https://jsonplaceholder.typicode.com/users
#
# Exercise 3: What happens if you fetch a post that doesn't exist?
#             Try: https://jsonplaceholder.typicode.com/posts/999
