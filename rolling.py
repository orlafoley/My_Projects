'''
1. Dice Rolling Simulator

The Goal: Like the title suggests, this project involves writing a program that simulates rolling dice.
When the program runs, it will randomly choose a number between 1 and 6.
(Or whatever other integer you prefer — the number of sides on the die is up to you.)
The program will print what that number is. It should then ask you if you’d like to roll again.
For this project, you’ll need to set the min and max number that your dice can produce. For the average die,
that means a minimum of 1 and a maximum of 6. You’ll also want a function that randomly grabs a number within that range and prints it.
Concepts to keep in mind:

Random
Integer
Print
While Loops


A good project for beginners, this project will help establish a solid foundation for basic concepts.
And if you already have programming experience, chances are that the concepts used in this project aren’t
completely foreign to you. Print, for example, is similar to Javascript’s console.log.
'''
def roll_a_die():
    try:
        import random
        dice=list(range(1,7))
        out=random.choice(dice)
        print(out)
        again=input(str('Would you like to roll the dice again? [Y/N] '))
        again=again[0].upper()
        while again == 'Y':
            if again=='Y':
                out = random.choice(dice)
                print(out)
                again = input(str('Would you like to roll the dice again? [Y/N] '))
                again = again[0].upper()
        return 'Goodbye!'

    except:
        return 'Fight me >:('
print(roll_a_die())