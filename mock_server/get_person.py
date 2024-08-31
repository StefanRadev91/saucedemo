import httpx

url = 'http://127.0.0.1:5000/people/7'

try:
    response = httpx.get(url)
    response.raise_for_status()  # Raise an exception for HTTP error responses
    print(response.json())
except httpx.RequestError as e:
    print(f"An error occurred while making the request: {e}")
except httpx.HTTPStatusError as e:
    print(f"HTTP error occurred: {e}")