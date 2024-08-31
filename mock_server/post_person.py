import httpx

url = 'http://127.0.0.1:5000/people/7'
data = {
    "id": "7",
    "name": "Stefano Gabanna",
    "age": 22
}

response = httpx.post(url, json=data)
print(response.json())