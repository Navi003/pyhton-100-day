
print("welcome to rollercoster ride")
height = int(input("what is your height?"))

bill = 0


if  height >= 120:
    print("You can ride the rollercoster")
    bill = 12
    age = int(input("what is your age?"))
   
   
    if age < 12:
        bill = 5  
        print(f"Child tickets are ${bill}")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are  ${bill}")
    else:
        print(f"Adult tickets are ${bill}")
    
    wants_photo = input("Do your want a photo taken? Y or N")
    
    if wants_photo == "Y":
            bill += 3
  

    print(f"Your Final Bill is ${bill}")
else:
    print("Sorry, you have to frow taller")
    
  
  
############################
#?EVEN ODD Exersise 
#*##########################
    
#  # Which number do you want to check?
# number = int(input())
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇

# check = number % 2

# if check == 1:
#     print("This is an odd number.")
# else:
#      print("This is an even number.")



#? BMI Calculator with conditinals 

# "Your BMI is 18.28678, you are underweight."
# "Your BMI is 22.0, you have a normal weight."
# "Your BMI is 28.50752, you are slightly overweight."
# "Your BMI is 32.56189, you are obese."
# "Your BMI is 37.50000, you are clinically obese."

# height = float(input("Please enter your height"))
# weight = float(input("Please enter your weight"))

# height_meters = height / 100.0

#     # Calculate BMI
# b = weight / (height_meters ** 2)

# bmi = round(b)

# print(bmi)

# if bmi < 18.5:
#         print(f"Your BMI is {bmi}, you are underweight.")
# elif 18.5 <= bmi < 25:
#         print(f"Your BMI is {bmi}, you have a normal weight.")
# elif 25 <= bmi < 30:
#         print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif 30 <= bmi < 35:
#         print(f"Your BMI is {bmi}, you are obese.")
# else:
#         print(f"Your BMI is {bmi}, you are clinically obese.")



