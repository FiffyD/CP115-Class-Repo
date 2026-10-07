speed = int(input())
total_reading = 0 
current_streak = 0
longest_streak = 0

while speed >= 0:
    total_reading += 1
    if speed < 20:
        current_streak += 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else :
        current_streak = 0
    speed = int(input())

print(total_reading)
print(longest_streak)
