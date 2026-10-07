# Counter-controlled approach - must know count first
num_count = int(input("How many numbers? "))
total = 0

for i in range(num_count):
    number = int(input(f"Enter number {i + 1}: "))
    total += number

print(f"Total: {total}")