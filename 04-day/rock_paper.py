
import random

# Rock is 1
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

#paper is  2
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

#scissors for 3
scissors = """
    _______
---'   ____)____
          ______)1
       __________)
      (____)
---.__(___)
"""

list_of_options = [rock,paper,scissors]


user_input = int(input("Please eneter 1 for rock 2 for paper and 3 for scissors"))
print('YOU CHOOSE ---->')
print(list_of_options[user_input-1])

print("*********************")


ai = random.randint(1,3)
print('AI CHOOSE ---->')
print(list_of_options[ai-1])


#*How user wins
if (user_input == 1 and ai == 3) or( user_input == 2 and ai == 1) or (user_input == 3 and ai == 2):
    print('😍😍You have won congratulations 😍😍')
elif ai == user_input: 
    print('Ohhh, its a Draw try again :D')
else:
    print("You Loose :( :(")
