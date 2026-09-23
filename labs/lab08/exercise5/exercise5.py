main_course = input()
drink = input()
dessert = input()

if main_course == "Chicken" :
    course_price = 10
elif main_course == "Beef" :
    course_price = 12
else :
    price = 11

if drink == "Soft Drink" :
    price = 2
else :
    price = 3

if dessert == "Ice Cream" :
    price = 4
else :
    price = 5

menu_prices = main_course + drink + dessert
final_bill = menu_prices + (menu_prices * 0.10)

print(f"{final_bill:.2f}")
