score = int(input())
total_a = 0
total_b = 0
is_a_turn = True

while score != -1:
    if is_a_turn:
        total_a += score
    else:
        total_b += score
    
    is_a_turn = not is_a_turn
    score = int(input())

if total_a > total_b:
    winner = "A"
elif total_b > total_a:
    winner = "B"
else:
    winner = "Tie"

print(total_a)
print(total_b)
print(winner)