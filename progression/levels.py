def level_up_threshold(level):
    """
    Amount of points needed to levelup from current level
    Each level costs 1.75x more than the previous level
    Level 1 = 100, level 2 = 175 ....
    """
    cost = 100
    total_cost = 0

    # New amount of points needed after level 1
    for level in range(level):
        total_cost += cost
        cost = round(cost * 1.75)
    return total_cost

def user_level(points):
    """
    Tracks user level based on total points accumulated
    """
    level = 1
    # Level up user until points no longer meet the threshold
    while points >= level_up_threshold(level + 1):
        level += 1
    return level

def next_level_requirements(points):
    """
    Return amount of poitns needed for next level
    """
    current_level = user_level(points)
    level_up_points = level_up_threshold(current_level + 1)
    points_needed = level_up_points - points
    return {
        "points_needed": points_needed,
        "next_level_points": level_up_points - points
    }
