from datetime import date

def calculate_streak(current_streak, last_activity, event_type):
    today = date.today().isoformat()
    
    if last_activity == None:
        return 1, today

    days_inactive = (date.fromisoformat(today) - date.fromisoformat(last_activity)).days

    # User already logged in
    if days_inactive == 0:
        new_streak = current_streak
    # User active again 
    elif days_inactive == 1:
        new_streak = current_streak + 1
    # User inactive
    else:
        new_streak = 0

    return new_streak, today

