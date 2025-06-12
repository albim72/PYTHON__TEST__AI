import requests

data = {
    "title": "Zadanie testowe",
    "body": "To jest przykładowa treść",
    "userId":1
}

response = requests.post("http://jsonplaceholder.typicode.com/posts", json=data)

print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")   
