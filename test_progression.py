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
print("GET Progress:", response.json())

# Retrieves stats (User story 2 test)
response = requests.get(f"{BASE_URL}/api/stats/7")
print("GET Stats: ", response.json())

# POST streak
response = requests.post(f"{BASE_URL}/api/streak/update", json={
    "user_id": 7,
    "event_type": "task_completed"
})
print("POST Streak:", response.json())

# GET streak
response = requests.get(f"{BASE_URL}/api/streak/7")
print("GET Streak:", response.json())
