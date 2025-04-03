# Maurice Davis 03-31-24
# Drama theater seating lab 

'''
This program is for a drama theater that offers tickets for viewing in three seaparate sections. 
the program will offer prices according to each section. 
''' 


def main():                                                                                 # main function
         

    print('Welcome to the Drama theater Movie Company!\n')

    print('tickets are now available in sections A, B, and C!\n')

    print('Section A tickets: $20, section B tickets: $15, section C tickets: $10\n')
    
    

    section_price_a = 20                                                                    # Local variables
    section_price_b = 15
    section_price_c = 10
    total_seats_a = 300	
    total_seats_b = 500 
    total_seats_c = 200 
    section_a = "A"
    section_b = "B"
    section_c = "C"
    purchase_more = "y" 
    prompt = "how many tickets would you like to buy"
    min = 0
    subtotal_a = 0
    subtotal_b = 0
    subtotal_c = 0
    grand_total = 0
    total_tix_sold_a = 0
    total_tix_sold_b = 0
    total_tix_sold_c = 0

    while purchase_more == "y" or purchase_more == "yes":                                   # Ticket purchase loop                       
                                                                                           
        tix_sold_a = getValidNum(f"{prompt} in Section {section_a}? Tickets available: '{total_seats_a}'\n", total_seats_a, min) # asks for number of tickets to buy in each section. 
        tix_sold_b = getValidNum(f"{prompt} in Section {section_b}? Tickets available: '{total_seats_b}'\n", total_seats_b, min) 
        tix_sold_c = getValidNum(f"{prompt} in Section {section_c}? Tickets available: '{total_seats_c}'\n", total_seats_c, min)
    
        
        total_seats_a -= tix_sold_a                                                         # Update seat availability in each section
        total_seats_b -= tix_sold_b
        total_seats_c -= tix_sold_c


        subtotal_a += tix_sold_a * section_price_a                                          # Update the price total for the amount of tickets sold for each section
        subtotal_b += tix_sold_b * section_price_b
        subtotal_c += tix_sold_c * section_price_c

        total_tix_sold_a += tix_sold_a                                                      # updates the amount of tickets sold for each seaction
        total_tix_sold_b += tix_sold_b
        total_tix_sold_c += tix_sold_c
        
        print(f"Subtotal for Section A: ${subtotal_a}")                                     # Displays amount of income generated from ticket sales for each section before more purchase
        print(f"Subtotal for Section B: ${subtotal_b}")
        print(f"Subtotal for Section C: ${subtotal_c}")

        purchase_more = getYesOrNo("Would you like to buy more tickets?\n")                 # Ask if the user wants to buy more tickets

        
    grand_total = subtotal_a + subtotal_b + subtotal_c                                      # Calculate the grand total and display ticket sales
    ticketsSold(total_tix_sold_a,total_tix_sold_b, total_tix_sold_c)                        # call to ticketsSold function
    priceTotals(subtotal_a,subtotal_b, subtotal_c, grand_total)                             # call to priceTotal function



 
def ticketsSold(total_tix_sold_a,total_tix_sold_b, total_tix_sold_c):
    '''
    This function displays the number of tickets sold in each section
    '''
    print(f"Tickets sold for Section A: {total_tix_sold_a}")
    print(f"Tickets sold for Section B: {total_tix_sold_b}")
    print(f"Tickets sold for Section C: {total_tix_sold_c}")

 
def priceTotals(subtotal_a, subtotal_b, subtotal_c, grand_total):   
    '''
    this function displays a subtotal amount of income generated
    from ticket sales for each section and grand total
    '''                        
    print(f"Subtotal for Section A: ${subtotal_a}")
    print(f"Subtotal for Section B: ${subtotal_b}")
    print(f"Subtotal for Section C: ${subtotal_c}")    
    print(f"grand_total : ${grand_total}")



def get_integer(msg):                                                                       # function to collect any integer value
    while True:
        try:    
            user_input = int(input(msg))
            return user_input
        except ValueError:
            print('Incorrect or no data  was entered, please re-attempt')


def getValidNum(msg, high, low):
    newValue = get_integer(msg)
    #validate the user's input using isInvalid() to check conditions
    while isInvalid(newValue, high, low):
        print('Invalid number!')
        newValue = get_integer(msg)
    return newValue


def isInvalid(value, h, l):                                                                 # isInvlaid is called in the getValidNum() function
    # returns True if value is invalid (bad data)
    # returns False if value is valid (good data)
    # many conditions can be added to this function
    if value < l:
        return True #invalid data, too low
    if value > h:
        return True #invalid data, too high
    return False #passed all checks, good data

def getYesOrNo(msg):                                                                        
    '''
    this function asks the user for a yes or no response
    and loops if specific  keywords are not input
    '''
    response = input(msg).lower()
    while response != "yes" and  response != "no" and  response != "y" and  response != "n":
        print ("error")
        response = input(msg) 
    return response

main()                                                                                      # call to main function to run the program

	 