import os
from random import randint
from datetime import datetime, timedelta

# Define the start and end dates
start_date = datetime(year=2024, month=2, day=1)
end_date = datetime(year=2024, month=12, day=30)

# Calculate the number of days in the range
delta_days = (end_date - start_date).days

# Loop through each day from start_date to end_date
for i in range(delta_days + 1):
    current_date = start_date + timedelta(days=i)
    d = current_date.strftime('%Y-%m-%d') + ' days ago'
    for j in range(randint(1, 10)):
        with open('file.txt', 'a') as file:
            file.write(d + '\n')  # Added a newline character for better readability
            os.system('git add .')
            os.system('git commit --date="' + current_date.strftime('%Y-%m-%d') + '" -m "commit"')

os.system('git push -u origin main')
