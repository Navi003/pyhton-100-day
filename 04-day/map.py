line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇


line_number = int(position[1]) - 1
column_number = position[0].lower()


print(line_number,column_number)

if(column_number == 'a'):
    column_number = 0
elif(column_number =='b'):
    column_number = 1
else:
    column_number = 2


map[line_number][column_number] = 'x'



# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")