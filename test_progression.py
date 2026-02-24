import requests

BASE_URL = "http://localhost:3000"

# Health check
response = requests.get(f"{BASE_URL}/api/health")
print("Health:", response.json())

# Tests POST by sending informatiot
response = requests.post(f"{BASE_URL}/api/update", json={
    "user_id": 7,
    "points_earned": 250,
    "event_type": "task_completed"
})
print("POST stats:", response.json())

# Retrieves stats that were posted
response = requests.get(f"{BASE_URL}/api/progress/7")
print("GET Stats:", response.json())
