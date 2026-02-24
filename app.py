import logging
from flask import Flask, request, jsonify

from progression.levels import user_level, next_level_requirements

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

users = {}

# ===========================
#           POST
# ===========================
@app.route("/api/update", methods=["POST"])
def update_progress():
    """
    Track user points and level progress
    """
    try:
        data = request.get_json(force=True, silent=True)
        if data is None:
            return jsonify({"error": "Missing JSON"}), 400
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    user_id = data.get("user_id")
    points_earned = data.get("points_earned", 0)

    # Validate user_id
    if not user_id:
        return jsonify({"error": "user_id required"}), 400

    # Convert user_id to string
    user_id = str(user_id)

    # Validate points
    try:
        points_earned = float(points_earned)
    except (TypeError, ValueError):
        return jsonify({"error": "points must be a number"}), 400

    # New user
    if user_id not in users:
        users[user_id] = 0

    # Update total points
    users[user_id] += points_earned
    total_points = users[user_id]

    try:
        current_level = user_level(total_points)
        next_level_info = next_level_requirements(total_points)
        try:
            valid_user_id = int(user_id)
        except ValueError:
            valid_user_id = user_id

        if isinstance(next_level_info, dict):
            points_to_next = next_level_info.get("next_level_points", 0)
        else:
            points_to_next = next_level_info - total_points

        result = {
                "status": "success",
                "user_id": valid_user_id,
                "current_level": current_level,
                "total_points": total_points,
                "next_level_requirement": total_points + points_to_next
                }
        logger.info(f"User {user_id} update: +{points_earned} points")
        return jsonify(result), 200

    except Exception:
        logger.error(f"Error calculating level for user {user_id}")
        return jsonify({"error": "Internal server error"}), 500

# ============================
#           GET
# ============================
@app.route("/api/progress/<user_id>", methods=["GET"])
def get_progress(user_id):
    """
    Retrieves progress information based on user
    """
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    
    user_id = str(user_id)

    # Get points from userID
    total_points = users.get(user_id)

    # If no points
    if total_points is None:
        return jsonify({"error": "user not found"}), 404
    
    try:
        current_level = user_level(total_points)
        next_level_info = next_level_requirements(total_points)
        try:
            valid_user_id = int(user_id)
        except ValueError:
            valid_user_id = user_id

        if isinstance(next_level_info, dict):
            points_to_next = next_level_info.get("next_level_points", 0)
        else:
            points_to_next = next_level_info - total_points

        result = {
                "status": "success",
                "user_id": valid_user_id,
                "current_level": current_level,
                "total_points": total_points,
                "next_level_requirement": total_points + points_to_next
                }
        return jsonify(result), 200
    
    except Exception:
        logger.error(f"Error retrieving progress for {user_id}")
        return jsonify({"error": "Internal server error"}), 500

@app.route("/api/stats/<user_id>", methods=["GET"])
def get_stats(user_id):
    """
    Returns OVERALL indepth statistics of user.
    Currently retrieves the same info as get_progress until further sprints 
    such as achievements are added
    """
    user_id = str(user_id)

    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    total_points = users[user_id]
    
    try:
        current_level = user_level(total_points)
        next_level_info = next_level_requirements(total_points)
        try:
            valid_user_id = int(user_id)
        except ValueError:
            valid_user_id = user_id

        if isinstance(next_level_info, dict):
            points_to_next = next_level_info.get("next_level_points", 0)
        else:
            points_to_next = next_level_info - total_points

        # Add future stats
        result = {
                "status": "success",
                "user_id": valid_user_id,
                "current_level": current_level,
                "total_points": total_points,
                "next_level_requirement": total_points + points_to_next
                }
        return jsonify(result), 200
    
    except Exception:
        logger.error(f"Error retrieving progress for {user_id}")
        return jsonify({"error": "Internal server error"}), 500
# ===============================
#            HEALTH
# ===============================
@app.route("/api/health", methods=["GET"])
def health_check():
    """
    Check endpoints
    """
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port, debug=False)
