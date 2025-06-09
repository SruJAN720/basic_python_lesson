import datetime

current_time = datetime.datetime.now()
print(current_time)
hour = current_time.hour
hour = 35
if 0 <= hour < 12:
    greeting = "Good morning"
elif 12 <= hour < 16:
    greeting = "Good afternoon"
elif 16 <= hour < 21:
    greeting = "Good evening"
elif 21<= hour <24:
    greeting = "Good night"
else:
    greeting = "It's invalid time" 

print(greeting+" sir")

