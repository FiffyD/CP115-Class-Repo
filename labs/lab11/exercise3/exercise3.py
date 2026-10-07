number = int(input())
count = 0 
biggest_jump = 0
previous_number = number

while number != 0 :
    count += 1
    next_number = int(input())
    if next_number != 0 :
        jump = next_number - previous_number 
        if jump > biggest_jump:
            biggest_jump = jump 
    previous_number = next_number
    number = next_number

print(count)
print(biggest_jump)