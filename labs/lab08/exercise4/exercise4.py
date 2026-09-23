current_reading = int(input())
previous_reading = int(input())

consumption = current_reading - previous_reading 

if consumption <= 20 :
    water_cost = consumption * 0.57
elif consumption <= 35 :
    water_cost = (0.57* 20) + ((consumption - 20) * 1.03)
else :
    water_cost = (0.57*20) + (1.03*15) + ((consumption - 35) * 1.40 )

service_charge = 8
sewerage = 2
extra_charges = service_charge + sewerage
total_bill = water_cost + extra_charges 

print(consumption)
print(water_cost)
print(total_bill)
