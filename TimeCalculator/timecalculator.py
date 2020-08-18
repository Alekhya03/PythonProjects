def add_time(time, duration, day = None):
    """ Adds duration to the starting time """
    daysoftheweek = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    time = time.replace(":", " ").split()
    time[0] = int(time[0])
    time[1] = int(time[1])

    # Change time to 24hr time.
    if time[2] == "PM" and time[0] != 12:
        time[0] += 12

    duration = duration.replace(":", " ").split()
    hours = int(duration[0])
    minutes = int(duration[1])

    # Add duration to start time.
    new_time_hours = time[0] + hours + ((time[1] + minutes) // 60)
    days = new_time_hours // 24
    new_time_hours = new_time_hours % 24
    new_time_minutes = (time[1] + minutes) % 60

    if new_time_hours < 12:
        am_pm = "AM"
    elif new_time_hours >= 12:
        am_pm = "PM"

    # Change it to specified format.
    if new_time_hours > 12:
        new_time_hours -= 12
    elif new_time_hours == 0:
        new_time_hours = 12

    days_phrase = ""
    if days == 1:
        days_phrase = " (next day)"
    elif days > 1:
        days_phrase = f" ({days} days later)"

    # Work out day of the week.
    new_day = ""
    if day != None:
        day = day.lower()
        index = daysoftheweek.index(day)
        index += days
        index = index % 7
        new_day = f", {daysoftheweek[index].capitalize()}"


    return f"{new_time_hours}:{new_time_minutes:02d} {am_pm}{new_day}{days_phrase}"
    
# Test cases
# print(add_time("3:00 PM", "3:10")) 
# print(add_time("11:30 AM", "2:32", "Monday")) 
# print(add_time("11:43 AM", "00:20")) 
# print(add_time("10:10 PM", "3:30")) 
# print(add_time("11:43 PM", "24:20", "tueSday")) 
# print(add_time("6:30 PM", "205:12", "Wednesday")) 