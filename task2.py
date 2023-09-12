from datetime import datetime, timedelta

current_datetime = datetime.now()
new_datetime = current_datetime + timedelta(days=7)
formatted_result = new_datetime.strftime('%Y-%m-%d')

print(formatted_result)
