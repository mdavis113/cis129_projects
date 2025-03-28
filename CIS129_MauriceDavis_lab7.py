# Maurice Davis 03-27-25
# this program  is a dice game

# lab 7-3 The Dice Game
# add libraries needed

import random



def main():
    print()

    #initialize variables
    endProgram = ('no')
    playerOne = ('NO NAME')
    playerTwo = ('NO NAME')


    # call to input names    
    playerOne, playerTwo = inputNames(playerOne, playerTwo)

    # while loop to run program again
    while endProgram == "no":
        # populate variables
        winnerName = ('NO NAME')
        p1number = 0
        p2number = 0
        
        # call to roll dice
        winnerName = rollDice(p1number, p2number, playerOne, playerTwo , winnerName)

        #call to displayinfo
        displayInfo(winnerName)

        endProgram = input('Do you want to end program? (yes/no): ')

# this function gets players names
def inputNames(playerOne, playerTwo):
    playerOne = input('Enter the name for Player 1: ')
    playerTwo = input('Enter the name for Player 2: ')

    return playerOne, playerTwo

# this function will get the random values
def rollDice(p1number, p2number, playerOne, playerTwo , winnerName):
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)

    if p1number > p2number:
        winnerName = playerOne
    elif p1number < p2number:
        winnerName = playerTwo
    else :
        winnerName = ('Tie')
    return winnerName

# this function displays the winner
def displayInfo(winnerName):
    print(f"The winner is: {winnerName}")

#calls main
main()