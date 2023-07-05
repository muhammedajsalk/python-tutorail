from datetime import date, timedelta

today = date.today()
print("Today's date:", today)

yesterday = today - timedelta(days=1)
print("Yesterday's date:", yesterday)

tomorrow = today + timedelta(days=1)
print("Tomorrow's date:", tomorrow)
