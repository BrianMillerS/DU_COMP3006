#!/usr/bin/env python3

"""
# Class: COMP 3006
# Author: Brian Miller
# DU ID: 873601817
# Date: 2/9/2022

########  WAR DICE  ########

## USAGE ##
python3 war_dice_game.py

## NOTES TO THE GRADER ##
Rather than compare all instance attributes, all comparison magic methods
just compare the roll outcomes, for example:
self.outcome (for the Class Dice)
self.sum_of_dice (for the Class Cup_of_Dice)
Doing this is perticularly helpful in the game (player.sum_of_dice > computer.sum_of_dice...)
"""

import os
from random import randint


class Dice():
    """Represent a die which can be rolled"""
    
    def __init__(self, sides=6):
        # inititialize the die
        self.sides = sides
        self.outcome = randint(1, self.sides)
    
    
    def __str__(self):
        return "[Roll Outcome: {}, Number of sides: {}]".format(self.outcome, self.sides)
    
    
    def __add__(self, other_die_instance):
        # add, returns the sum of the two roll outcomes
        if type(self) == type(other_die_instance):
            return self.outcome + other_die_instance.outcome
        else:
            return NotImplemented
    
    
    def __eq__(self, other_die_instance):
        # equals, compares the roll outcomes only
        if type(self) == type(other_die_instance):
               return ((self.outcome) == (other_die_instance.outcome))
        else:
            return NotImplemented
        
        
    def __ne__(self, other_die_instance):
        # not equals, compares the roll outcomes only
        if type(self) == type(other_die_instance):
               return ((self.outcome) != (other_die_instance.outcome))
        else:
            return NotImplemented


    def __lt__(self, other_die_instance):
        # less than, compares the roll outcomes only
        if type(self) == type(other_die_instance):
               return ((self.outcome) < (other_die_instance.outcome))
        else:
            return NotImplemented
        
        
    def __gt__(self, other_die_instance):
        # greater than, compares the roll outcomes only
        if type(self) == type(other_die_instance):
               return ((self.outcome) > (other_die_instance.outcome))
        else:
            return NotImplemented
        
        
    def __le__(self, other_die_instance):
        # less than, or equals to, compares the roll outcomes only
        if type(self) == type(other_die_instance):
               return ((self.outcome) <= (other_die_instance.outcome))
        else:
            return NotImplemented
        
        
    def __ge__(self, other_die_instance):
        # greater than, or equals to, compares the roll outcomes only
        if type(self) == type(other_die_instance):
               return ((self.outcome) >= (other_die_instance.outcome))
        else:
            return NotImplemented


class Cup_of_dice():
    """Represent a cup of dice which can be rolled"""
    
    def __init__(self, num_dice=2, sides_per_die=6):
        # inititialize the cup of dice
        self.num_dice = num_dice
        self.sides_per_die = sides_per_die

        # roll all of the dice
        list_of_dice = []
        sum_of_dice = 0
        for i in range(1, num_dice+1): # for each die
            new_die = Dice(sides=sides_per_die) # roll that die
            sum_of_dice += new_die.outcome # add result to sum
            list_of_dice.append(new_die) # add die to list of die
            
        self.list_of_dice = list_of_dice
        self.sum_of_dice = sum_of_dice
    
    def __str__(self):
        # use the Class dice to print out each of the dice in the Cup of Dice
        list_of_dice_str = [Dice.__str__(i) for i in self.list_of_dice]
        return "[Dice: {}, Sides per die: {}, Sum: {}, Dice: {}]".format(self.num_dice, self.sides_per_die, self.sum_of_dice, list_of_dice_str)
    
    
    def __eq__(self, other_cup_of_dice_instance):
        # equals
        if type(self) == type(other_cup_of_dice_instance):
               return ((self.sum_of_dice) == (other_cup_of_dice_instance.sum_of_dice))
        else:
            return NotImplemented
        
        
    def __ne__(self, other_cup_of_dice_instance):
        # not equals
        if type(self) == type(other_cup_of_dice_instance):
               return ((self.sum_of_dice) != (other_cup_of_dice_instance.sum_of_dice))
        else:
            return NotImplemented


    def __lt__(self, other_cup_of_dice_instance):
        # less than
        if type(self) == type(other_cup_of_dice_instance):
               return ((self.sum_of_dice) < (other_cup_of_dice_instance.sum_of_dice))
        else:
            return NotImplemented
        
        
    def __gt__(self, other_cup_of_dice_instance):
        # greater than
        if type(self) == type(other_cup_of_dice_instance):
               return ((self.sum_of_dice) > (other_cup_of_dice_instance.sum_of_dice))
        else:
            return NotImplemented
        
        
    def __le__(self, other_cup_of_dice_instance):
        # less than, or equals to
        if type(self) == type(other_cup_of_dice_instance):
               return ((self.sum_of_dice) <= (other_cup_of_dice_instance.sum_of_dice))
        else:
            return NotImplemented
        
        
    def __ge__(self, other_cup_of_dice_instance):
        # greater than, or equals to
        if type(self) == type(other_cup_of_dice_instance):
               return ((self.sum_of_dice) >= (other_cup_of_dice_instance.sum_of_dice))
        else:
            return NotImplemented


if __name__ == "__main__":
    
    # clear the terminal output
    start_game=" "
    while start_game != "":
        start_game = input("Press ENTER to start the game!")
    os.system('clear')
    
    # prompt the user to pick a username
    player_username = input("Please pick a username: ")
    print("Username selected...")
    print("Welcome to the game: {}".format(player_username))
    
    # initial user inputs
    n_dice_per_cup = int(input("Choose the number of dice to roll: "))
    n_sides_per_die = int(input("Choose the number of sides each die has: "))
    player_amount = int(input("Choose your starting cash amount ($): "))
    computer_amount = int(input("Choose the computer's cash amount ($): "))

    # set up game loop condition
    keep_running_game = True
    while keep_running_game == True:
        
        # print the scoreboard
        os.system('clear')
        print("Money ({}): ${}".format(player_username, player_amount))
        print("Money (Computer): ${}".format(computer_amount))
        print("---------------------------------\n")
        
        # determine the bet amount
        bet_amount_determined = False
        while bet_amount_determined == False:
            bet_amount = int(input("Amount to bet ($): "))
            if (bet_amount > player_amount) or (bet_amount <= 0): # make sure the bet amount is logical
                print("Sorry, that bet amount doesn't make sense...")
                continue
            bet_amount_determined = True  # break the loop
        
        # set up bet loop condition
        roll_winner_determined = False
        while roll_winner_determined == False:
            
            # perform the user's roll
            roll=" "
            while roll != "":
                roll = input("\nPress ENTER to use your cup of {} dice...".format(n_dice_per_cup))
            user_roll = Cup_of_dice(num_dice = n_dice_per_cup, sides_per_die = n_sides_per_die)
            # print the users dice, and the sum
            for die in user_roll.list_of_dice:
                print("die outcome: {}".format(die.outcome))
            print("{}'s dice summed to {}".format(player_username, user_roll.sum_of_dice))
            
            # perform the computer's roll
            roll=" "
            while roll != "":
                roll = input("\nPress ENTER to let the computer roll their {} dice...".format(n_dice_per_cup))
            computer_roll = Cup_of_dice(num_dice = n_dice_per_cup, sides_per_die = n_sides_per_die)
            # print the users dice, and the sum
            for die in computer_roll.list_of_dice:
                print("die outcome: {}".format(die.outcome))
            print("The Computer's dice summed to {}".format(computer_roll.sum_of_dice))
            
            # determine if it's a tie
            if user_roll == computer_roll:
                print("\nIt's a tie! Let's roll again...\n")
                continue
            # determine if you won
            elif user_roll > computer_roll:
                player_amount += bet_amount
                computer_amount -= bet_amount
                print("\nYou won!")
            # determine if you lost
            elif user_roll < computer_roll:
                player_amount -= bet_amount
                computer_amount += bet_amount
                print("\nYou lost!")
            
            # prompt the user to continue
            next_roll = " "
            while next_roll != "":
                next_roll = input("\nPress ENTER to continue...")
            
            roll_winner_determined = True  # exit loop
        
        # check the player and the computer's balance
        if player_amount <= 0:
            print("You lost the game! Better luck next time :(")
            keep_running_game = False
            
        elif computer_amount <= 0:
            print("You won the game!")
            keep_running_game = False

        
###  CLASS TESTING  ###

# print("\n## Testing Dice Class ##")
# die_1 = Dice(sides = 6)
# die_2 = Dice(sides = 6)
# print(die_1)
# print(die_2)
# print("{} == {} :{}".format(die_1.outcome, die_2.outcome, die_1 == die_2))
# print("{} != {} :{}".format(die_1.outcome, die_2.outcome, die_1 != die_2))
# print("{} < {}  :{}".format(die_1.outcome, die_2.outcome, die_1 <  die_2))
# print("{} > {}  :{}".format(die_1.outcome, die_2.outcome, die_1 >  die_2))
# print("{} <= {} :{}".format(die_1.outcome, die_2.outcome, die_1 <= die_2))
# print("{} >= {} :{}".format(die_1.outcome, die_2.outcome, die_1 >= die_2))
# print("{} + {}  :{}".format(die_1.outcome, die_2.outcome, die_1 + die_2))
# print("\n## Testing Dice Class ##")
# cup_of_dice_1 = Cup_of_dice(num_dice = 2, sides_per_die = 6)
# cup_of_dice_2 = Cup_of_dice(num_dice = 2, sides_per_die = 6)
# print(cup_of_dice_1)
# print(cup_of_dice_2)
# print("{} == {} :{}".format(cup_of_dice_1.sum_of_dice, cup_of_dice_2.sum_of_dice, cup_of_dice_1 == cup_of_dice_2))
# print("{} != {} :{}".format(cup_of_dice_1.sum_of_dice, cup_of_dice_2.sum_of_dice, cup_of_dice_1 != cup_of_dice_2))
# print("{} < {}  :{}".format(cup_of_dice_1.sum_of_dice, cup_of_dice_2.sum_of_dice, cup_of_dice_1 <  cup_of_dice_2))
# print("{} > {}  :{}".format(cup_of_dice_1.sum_of_dice, cup_of_dice_2.sum_of_dice, cup_of_dice_1 >  cup_of_dice_2))
# print("{} <= {} :{}".format(cup_of_dice_1.sum_of_dice, cup_of_dice_2.sum_of_dice, cup_of_dice_1 <= cup_of_dice_2))
# print("{} >= {} :{}".format(cup_of_dice_1.sum_of_dice, cup_of_dice_2.sum_of_dice, cup_of_dice_1 >= cup_of_dice_2))