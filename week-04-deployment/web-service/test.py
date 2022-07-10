import requests

ride = {"PULocationID": 10, "DOLocationID": 50, "trip_distance": 40}

url = "http://localhost:9696/predict-duration"
response = requests.get(url, json=ride)
print(response.json())
