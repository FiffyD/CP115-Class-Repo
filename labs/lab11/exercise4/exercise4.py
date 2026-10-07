sales = int(input())
count = 0
record_days = 0
max_sales = 0

while sales != 0 :
    count += 1
    if count == 1:
        record_days += 1
        max_sales = sales
    elif sales > max_sales:
        record_days += 1
        max_sales = sales

    sales = int(input())

print(count)
print(record_days)
