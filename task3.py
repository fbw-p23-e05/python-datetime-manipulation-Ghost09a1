from datetime import datetime, timedelta

current_date = datetime(year=2020, month=1, day=1)
due_date = current_date + timedelta(days=25)
formatted_message = f"Hello Friedrich, your rent of 300 € is due on {due_date.strftime('%d %B, %Y')}."

print(formatted_message)
