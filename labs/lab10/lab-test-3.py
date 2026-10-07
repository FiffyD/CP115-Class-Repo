#Get user input 
usage = float(input("Enter usage : "))

#Determine discount categories based on usage
if usage < 50 :
    discount = 0
elif usage <= 100 :
    discount = 0.05
else :
    discount = 0.20

#Calculate discount amount and bill
discount_amount = usage * discount
bill = usage - discount_amount

#Display output  
print("Discount amount : RM",discount_amount)
print("Bill to be paid : RM",bill)