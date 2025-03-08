# Maurice Davis 03/04/2025 
# this program  will allow a grocery store to keep track 
#   of the total number of bottles collected for seven days.

# Lab 5 the Bottle Return Program
total_bottles = 0
counter = 1
today_bottles = 0
total_payout = 0
payout_per_bottle = .10
nbr_of_days = 7
keepGoing = "y"  # Control variable to rerun the program


while keepGoing == "y":

    total_bottle = 0  # Stores the total bottles collected for the week

    today_bottle = 0  # Stores the bottles collected for the current day

    total_payout = 0  # Stores the total payout for the week

    counter = 1  # Control variable for the loop (tracks days of the week)    
    
    print("\nEnter the number of bottles returned for each day of the week:")

    while counter <= 7:

        today_bottle = int(input(f"Day {counter}: "))

        counter += 1  # Move to the next day
        
        total_bottle += today_bottle

        total_payout = total_bottle * payout_per_bottle # Calculate the total payout

        
    print(f"Total bottles returned: {total_bottle}")

    print(f"Total amount paid: ${total_payout:.2f}")

    keepGoing = input( "do you have more data to enter?\n").lower()
    