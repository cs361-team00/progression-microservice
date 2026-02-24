from datetime import date

def calculate_streak(current_streak, last_activity):
    today = date.today().isoformat()

    if last_activity is None:
        return 1, today

    days_inactive = (date.fromisoformat(today) - date.fromisoformat(last_activity)).days

    if days_inactive == 0:
        return current_streak, today

    elif days_inactive == 1:
        return current_streak + 1, today

    return 0, today

