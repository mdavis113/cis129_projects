# this programs purpose is to document the amount of inventory purchased by the consumer

# the program asks the user to enter the number of item (coffees, muffins, donuts, and lemonade) purchased

# the program adds a subtotal and a tax amount to then display a final total.

# welcome the user to the coffee shop.

# declare variables and constants 

# author Maurice Davis


# this section of code defines teh varibles used in this shop
shop = ( "'Bake-Code-Ry'")

tax = .06

coffee_price = 5.00

muffin_price = 4.00

donut_price = 3.00

lemonade_price = 2.00

# this section of code displays welcome to user, asks the number of items 
# the user is purchasing and displays those item amounts

print ("***********************************************")

print ( '''Welcome to The " + shop + "!" 
        ''')

coffee = input( " number of coffees bought? " )

print ( coffee )

muffins = input( " number of muffins bought? " )

print ( muffins )

donuts = input(" number of donuts bought? " )

print (donuts)

lemonade = input(" number of lemonades bought? " ) 

print( lemonade)

# this section of code multiplys the item amount by the price of each specific item

total_coffee = (coffee_price) * int( coffee )

total_muffins = (muffin_price) * int( muffins)

total_donuts = (donut_price) * int( lemonade )

total_lemonades = ( lemonade_price ) * int( lemonade )
 
total_tax =  (total_coffee + total_muffins + total_donuts + total_lemonades ) * tax




print ("***********************************************")

print (
      
     
      )


print ("***********************************************")

# displays shop receipt
print (" The " + shop + " Receipt " )

# this section displays  the total amount  of items, the price,  and multiplies
# them by the tax to display a final total

print ( coffee, "Coffee at $" , int(coffee_price), "each: $", total_coffee )

print ( muffins, "Muffins at $" , int(muffin_price), "each: $", total_muffins )

print ( donuts, "donuts at $" , int(donut_price), "each: $", total_donuts )

print ( lemonade, "lemonades at $" , int(lemonade_price), "each: $", total_lemonades )


print ("6% tax: ", total_tax)

print ("Total: $", total_coffee + total_muffins + total_donuts + total_lemonades + total_tax)  

print ('''***********************************************"
       
       ''')
# thank you message to customer 
print ( "Thank you so much for vistings us here at the " + shop + "!")

print ('''We appreciate your Business!
       
              please come again soon! ''')
