import calendar

year = int(input("Enter a year: "))

print("Calendars for the year", year)

for month in range(1, 13):
  print("Calendar for", calendar.month_name[month], year)
  
  print("-" * 20)
  
  print("Month:", calendar.month_name[month])
  print("Year:", year)
  
  print(calendar.month(year, month))
  
  print("-" * 20)
  
  print("This is the calendar for", calendar.month_name[month], "in the year", year)
  
  print()

print("End of calendars for the year", year)
