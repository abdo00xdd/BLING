import calendar
from datetime import datetime

# Get the current year, month, and day
now = datetime.now()
year = now.year
month = now.month
day = now.day

# Create a TextCalendar object

cal = calendar.TextCalendar(calendar.SUNDAY)

# Generate the calendar for the current month
month_calendar = cal.formatmonth(year, month)

# Split the calendar into lines
calendar_lines = month_calendar.split('\n')

# Highlight the current day with a circle
for i in range(len(calendar_lines)):
    if str(day) in calendar_lines[i]:
        # Replace the day with a circled version
        calendar_lines[i] = calendar_lines[i].replace(f'{day:2}', f'({day:2})')

# Join the lines back together
highlighted_calendar = '\n'.join(calendar_lines)

# Print the highlighted calendar
print(highlighted_calendar)