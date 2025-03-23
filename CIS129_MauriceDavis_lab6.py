# Maurice Davis
# Hotdog Cookout Calculator

# this program will determine:
# the minimum number of packages of hotdogs
# minimum number of packages of buns required for cookout
# the number of hotdogs that will be left over
# the number of buns that will be left over
import math
def main():

   
   DOGS = 10 # hot dogs in a pack
   BUNS = 8  # hot dog buns in a package
   
   

   def getTotalHotDogs():
      # gets total number of hotdogs needed
      people = int(input( "Enter the number of people attending the cookout:\n ")) 
      hotDogs = int(input( "Enter the number of Hotdogs per person:\n "))

      # Calculate and return the total number of hot dogs needed
      total = people * hotDogs      
      return total 
   
   total = getTotalHotDogs()              #caluculates the total # of hotdogs needed

   dogsLeft = (DOGS - (total % DOGS)) 
   bunsLeft = (BUNS - (total % BUNS))
   minDogs = math.ceil(total / DOGS)      # Calculates the minimum number of packages of hot dogs
   minBuns = math.ceil(total / BUNS)      # Calculate the number of left over hot dog buns

   def showResults(dogsLeft, bunsLeft, minDogs, minBuns):

      print(f"Hot dogs left over: {dogsLeft}")
      print(f"Hot dog buns left over: {bunsLeft}")
      print(f"Minimum packages of hot dogs needed: {minDogs}")
      print(f"Minimum packages of hot dog buns needed: {minBuns}")


   showResults(dogsLeft, bunsLeft, minDogs, minBuns)


main()

