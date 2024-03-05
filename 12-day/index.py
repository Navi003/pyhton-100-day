
import random


# Guess Nummber Game


#1 Create a Variablie betwin Range of 1-100 ( This should be Random Nummber)
random_number = random.randint(1, 100)

#2 Ask user to choose between Easy and hard lever set this variable to 5 or 10 deppendes on what user chooses  (user tries)

tries = 0

level = input('Please Choose level between easy and hard  ')

if level == 'hard':
    tries = 5 
if level == 'easy':
    tries = 10

print(tries)    

#4 start a while loop where we will check if user has left tries and random_number not equal to user guess if. 
while tries > 0 :
    guess =  int(input('Please guess a number between 1 and 100 '))
    
    if guess > random_number:
        print('it is too high')
        tries -= 1
    if guess < random_number:
        tries -= 1
        print('it is too low')
    if guess == random_number:
        print(f'you guessed it right you have {tries} left')
    


#5 in While loop we will ask user for a guess 

#6 then in while loop we will check if the guess is lower or higher 

#give user feedback





