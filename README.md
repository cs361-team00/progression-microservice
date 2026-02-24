# progression-microservice
Progression microservice for tracking user points and level progress (User Story 1: Track User Progress). Levels scale using a 1.75x multiplier — level 1 requires 100 points, each subsequent level costs 1.75x more than the previous.


## Start the server:
Run program in terminal
```
python app.py
```

Server listens on http://0.0.0.0:3000.

## Testing
If requests is not installed

```
pip install requests
```
Run program in separate terminal:
```
python test_progression.py
```




## How to REQUEST DATA
### Uses API POST
User's points and level are updated with the required information


| Field   | required | Description |
|---------|----------| ------------|
| user_id |    yes   | ID of user  |
| points_earned| yes  | Number of points |

BASE_URL is constantly set in test file.

Example:
```
response = requests.post("http://localhost:3000/api/update", json={
    "user_id": 7,
    "points_earned": 750
})
```

Response:
```
{
  "status": "success",
  "user_id": 7,
  "current_level": 3,
  "total_points": 750.0,
  "next_level_requirement": 1117.0
}
```

## How to RECEIVE data
### Uses API GET
Retrieve user's progress:
```
response = requests.get("http://localhost:3000/api/progress/<user_id>")
```
Response:
```
{
  "status": "success",
  "user_id": 7,
  "current_level": 3,
  "total_points": 750.0,
  "next_level_requirement": 1117.0
}
```
## GET Health
Health check returns {"status": "ok"}