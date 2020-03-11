'''
2. Guess the Number

The Goal: Similar to the first project, this project also uses the random module in Python.
The program will first randomly generate a number unknown to the user.
The user needs to guess what that number is. (In other words, the user needs to be able to input information.)
If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too low).
If the user guesses correctly, a positive indication should appear. You’ll need functions to check if the user input is an actual number,
to see the difference between the inputted number and the randomly generated numbers, and to then compare the numbers.
Concepts to keep in mind:

Random function
Variables
Integers
Input/Output
Print
While loops
If/Else statements


Jumping off the first project, this project continues to build up the base knowledge and
introduces user-inputted data at its very simplest. With user input, we start to get into a little bit of variability.
'''

def guess_the_number():
    try:
        import random
        possible=range(1,21)
        secret_num=random.choice(possible)
        user_input=int(input('Give me a number between 1 and 20 inclusive: '))
        while user_input != secret_num:
            if 21 > user_input > secret_num:
                print('Too high, try again')
                user_input = int(input('Give me a number between 1 and 20 inclusive: '))
            elif 0 < user_input < secret_num:
                print('Too low, try again!')
                user_input = int(input('Give me a number between 1 and 20 inclusive: '))
            elif user_input < 0 or user_input > 20:
                print('Outside of acceptable range, learn to read! >:(')
                user_input = int(input('Give me a number between ONE (1) and TWENTY (20) inclusive: '))
        else:
            return 'You got it!'
    except:
        return 'Angry lack of integer noises >:('
print(guess_the_number())