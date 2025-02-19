#this programs purpose is to document the amount of inventory purchased by the consumer

# the prgram asks the user to enter the number of coffees and muffins purchased

# the add a subtotal and a tax amount to then display a final total.

# welcome the user to the coffee shop.

#declare variables and constants 

# author Maurice Davis


#this section of code defines teh varibles used in this shop
shop = ( "'Bake-Code-Ry'")

tax = .06

coffee_price = 5.00

muffin_price = 4.00

#this section of code displays welcome to user, asks the number of items 
# the user is purchasing and displays those item amounts

print ("***********************************************")

print ( " Welcome to The " + shop + "!" )

coffee = input( " number of coffees bought? " )

print ( coffee )

muffins = input( " number of muffins bought? " )

print ( muffins )

# this section of code multiplys the item amount by the price of each specific item

total_coffee = (coffee_price) * int( coffee )

total_muffins = (muffin_price) * int( muffins)
 
total_tax =  (total_coffee + total_muffins) * tax




print ("***********************************************")

print (
      
     
      )


print ("***********************************************")

#displays shop receipt
print (" The " + shop + " Receipt " )

# this section displays  the total amount  of items and the price and multiplys
# them by the tax todisplay a final total

print ( coffee, "Coffee at $" , int(coffee_price), "each: $", total_coffee )

print ( muffins, "Muffins at $" , int(muffin_price), "each: $", total_muffins )

print ("6% tax: ", total_tax)

print ("Total: $", total_coffee + total_muffins + total_tax)  

print ("***********************************************")
