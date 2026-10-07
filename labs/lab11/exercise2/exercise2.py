num_days = int(input())
danger_threshold = float(input())

# Initialize variables to keep track of danger days and the total temperature
danger_days = 0
total_temperature = 0.0

# Loop through each day to collect temperatures
for i in range(num_days):
    current_temp = float(input())
    total_temperature += current_temp
    
    # Check if the temperature exceeds the danger threshold
    if current_temp > danger_threshold:
        danger_days += 1

# Calculate the average temperature
average_temp = total_temperature / num_days

# Print the final results
print(danger_days)
print(f"{average_temp:.1f}")
