#Get user input
num_rounds = int(input())
round_processed = 0
final_score = 0

for i in range (num_rounds):
    score = float(input())

#Determine total score categories
    if score > 100:
       score *= 1.20

    final_score += score
    round_processed += 1

#Display output
print(f"{final_score:.1f}")
print(round_processed)