price1 = float(input())
quantity1 = int(input())
price2 = float(input())
quantity2 = int(input())
price3 = float(input())
quantity3 = int(input())

item1 = price1 * quantity1
item2 = price2 * quantity2
item3 = price3 * quantity3

subtotal = item1 + item2 + item3
tax = subtotal * 0.06
total = subtotal + tax

print(subtotal)
print(tax)
print(total)