# Maurice Davis 03/24/2025
# Hotdog Cookout Calculator lab 6

# this program will determine:
# the minimum number of packages of hotdogs
# minimum number of packages of buns required for cookout
# the number of hotdogs that will be left over
# the number of buns that will be left over
from math import ceil
def main():

   DOGS = 10                                                                    # hot dogs in a pack
   BUNS = 8                                                                     # hot dog buns in a package
   total = getTotalHotDogs()                                                    # sets variable total to the funtion getTotalHotDogs

   dogsLeft = (DOGS - (total % DOGS)) % DOGS
   bunsLeft = (BUNS - (total % BUNS)) % BUNS
   minDogs = ceil(total / DOGS)                                            # Calculates the minimum number of packages of hot dogs
   minBuns = ceil(total / BUNS)                                            # Calculate the number of left over hot dog buns
   
   showResults(dogsLeft, bunsLeft, minDogs, minBuns)                            # calls showResult funtion with specific arguments


def getTotalHotDogs():

   ''' this function gets the total number of hotdogs needed '''

   people = int(input( "Enter the number of people attending the cookout:\n ")) # receives input for the amount of people attending cookout
   hotDogs = int(input( "Enter the number of Hotdogs per person:\n "))          # receives input for the amount of hotdogs eac person will get

   # Calculate and return the total number of hot dogs needed
   total = people * hotDogs      
   return total 
   

def showResults(dogsLeft, bunsLeft, minDogs, minBuns):
   ''' this funtion takes the results of the minimum amount of hotdogs and hotdog buns,
       the left over hot dogs and hotdog buns, and displays them '''
   
   print(f"Hot dogs left over: {dogsLeft}")
   print(f"Hot dog buns left over: {bunsLeft}")
   print(f"Minimum packages of hot dogs needed: {minDogs}")
   print(f"Minimum packages of hot dog buns needed: {minBuns}")

main()                                                                           #calls the main funtion