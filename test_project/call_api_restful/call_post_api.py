import requests

# Specify the API endpoint URL and data to send

api_url = "http://127.0.0.1:8000/api/items_create"  # Replace with the actual API endpoint URL
data = {
    "name": "bb",
    "population": "4444",
    
}

# Make a PUT request to the API
response = requests.post(api_url, json=data)

# Check if the request was successful (status code 200 or 204)
if response.status_code in (201, 204):
    print("POST Request Successful")
else:
    print("POST Request Failed with status code:", response.status_code)