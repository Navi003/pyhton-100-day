# Welcome to the tip calculator.
# What was the total bill? $124.56
# What percentage tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7
# Each person should pay: $19.93


print(" Welcome to the tip calculator.")

bill_value = float(input("What was the total bill? "))
tip_value = float(input("hat percentage tip would you like to give? 10, 12, or 15? "))
how_many_people =  int(input("How many people to split the bill? "))



percentage_of_tip = (tip_value / 100) * bill_value  

total_bill = bill_value + percentage_of_tip

print(total_bill)

each_person_to_pay = total_bill / how_many_people

final_amount = round(each_person_to_pay,2)

print(f"Each person should pay: ${final_amount}")
