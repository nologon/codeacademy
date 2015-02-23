__author__ = 'thijn'
import random
# Rock-paper-scissors-lizard-Spock template
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

def name_to_number(name):
    number = 0
    if name == "rock":
        number = 0
    elif name == "Spock":
        number == 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print "No valid number given"
    return number

def number_to_name(number):
    name = ""
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    return name

def rpsls(player_choice):
    print ""
    comp_pick = random.randrange(0,4)
    print "Player chooses " + str(player_choice)
    player_number = "The winning player number is: " + str(name_to_number(player_choice))
    print "Computer chooses " + str(number_to_name(comp_pick))
    comp_number = "The winning compy number is: " + str(comp_pick)
    result = int(name_to_number(player_choice) - comp_pick) % 5
    if result >= 3:
        print "The player wins!"
    elif result >= 1:
            print "The Computer wins!"
    else:
        print "Player and computer tie!"

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
