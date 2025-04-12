#Maurice Davis 04/10/2025
#Palindrome tester
'''
This Program is a Palidrome tester. A palindrome 
is a word, sentence, verse, or even a number 
that reads the same backward or forward.
'''

message = ('''Palindromes can be fun! let's test a word, phrase, or set of numbers to see
                            if we've found one!''')
greeting = 'Welcome to the Palindrome Testing Center!'

def main():                                           # main function with program function calls
    print(greeting)
    print(message)
    print("Go ahead! Try it out!")
    keep_going = 'yes'
    
    while keep_going in ['y', 'yes']:                   # loops the program with certain response
        is_palindrome()
        keep_going =  getYesOrNo("Would you like to try another one? (yes/no)\n")  #sets variable  
                                                     # keep _going after call to I.V.F getYesOrNo
    print("Thank's for visiting! see you next time!")
        
def is_palindrome():
    '''
     This function was design to test if    
     a word, phrase or string of numbers fits the
     criteria to be considered a palindrome.
     Parameter = None
     Returns True or False
    '''
        
    response = input('Please enter any palindrome:\n').lower()            
    letter_list = []
                
    for i in response:                                                #itterates through Response
        if i != " " and i not in ['.', ',','?','!',"''",'""', ':', ';','-',]: # values to exclude
            letter_list.append(i)              # adds letters to list without unwanted characters
    print(letter_list)
    for i in letter_list:                                          #itterates through letter_list
        if i != letter_list.pop():                              # verifies itterable matches .pop
            print('Sorry! that is not a palindrome!\n')                           
            return False
        else:
             print("ahhh so satisfying! That's a palindrome!\n")               
        return True
        
def getYesOrNo(msg):                                                                        
    '''
    this function asks the user for a yes or no response
    and loops if specific  keywords are not input
    '''
    response = input(msg).lower()
    while response not in ['yes', 'no', 'y', 'n']:
        print ("Error. Try again")
        response = input(msg) 
    return response

main()