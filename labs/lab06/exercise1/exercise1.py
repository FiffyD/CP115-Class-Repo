# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.
# Without \n - everything prints on one line
# Without \t - no spacing
# Creating a formatted table
receipt = "\n\t  RECEIPT\n\nItem\tPrice\tQty\tTotal\nCoffee\t$3.50\t2\t$7.00\nMuffin\t$2.10\t3\t6.30\nWater\t&1.05\t4\t4.20\nSubtotal\t$17.50\nTax (6%)\t$1.05\nTotal\t\t$18.55\n"
Coffee = (3.50 * 2)
Muffin = (2.10 * 3)
Water = (1.05 * 4)
subtotal = (Coffee + Muffin + Water)
Tax = 0.06
Total =subtotal + (subtotal*Tax)
print(receipt)
