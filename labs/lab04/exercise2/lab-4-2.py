income = float(input())
if income <= 50000:
    totalTax = 0
else:
    if income <= 100000:
        totalTax = 500 + income - 100000 * 0.01
    else:
        totalTax = 500 + income - 100000 * 0.02
print(totalTax)
