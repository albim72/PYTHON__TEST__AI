import requests

response = requests.get("https://en.wikipedia.org/wiki/Strona_główna")

print(f"Tytuł strony: {response.text.split('<title>')[1].split('</title>')[0]}")

print("\nCookies: ")
for key, value in response.cookies.items():
    print(f"{key}: {value}")

print("\nHeaders: ")
for key, value in response.headers.items():
    print(f"{key}: {value}")
