
# #*for loops


# fruits = ["apple","Pech","Pear"]

# for fruit in fruits:
#     print(fruit)
    
    
# Input a Python list of student heights
# student_heights = ["168","168"]
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆

# sum_of_heights = 0

# for height in student_heights:
#       	sum_of_heights += height


# average_heights = sum_of_heights/len(student_heights)

# print(f"total height = {sum_of_heights}")
# print(f"number of students = {len(student_heights)}")
# print(f"average height = {round(average_heights)}")


#* Range function

# for number in range(1,10,3):
#     print(number)
# target = int(input())

# sum_of_evens = 0

# for number in range(1,target):
#   if number % 2:
#       sum_of_evens += number
    
    
# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
    
    




import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#%&()*+'

print("****Password Generator******")

letters_count = int(input("How many letters would you like in your password?\n"))
symbols_count = int(input("How many symbols would you like?\n"))
numbers_count = int(input("How many numbers would you like?\n"))

# Choose random letters
password = [random.choice(letters) for _ in range(letters_count)]


# Insert random symbols at random positions
for _ in range(symbols_count):
    random_symbol = random.choice(symbols)
    random_position = random.randint(0, len(password))
    password.insert(random_position, random_symbol)

# Insert random numbers at random positions
for _ in range(numbers_count):
    random_number = random.choice(numbers)
    random_position = random.randint(0, len(password))
    password.insert(random_position, random_number)

final_password = ''.join(password)

print(final_password)