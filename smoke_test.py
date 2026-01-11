import requests

response = requests.post(
    "http://localhost:5000/predict",
    json={"text": "smoke test"}
)

assert response.status_code == 200
print("Smoke test passed!")
