##############################################
# FCS 49 - Assignment 2 - Oussama Walieddine #
##############################################

#print(" FCS 49 - Assignment 2 - Oussama Walieddine\n--------------------------------------------")

################
# Display Menu #
################

def displayMenu():
  print('''
=================================

   Select Choice:
  ---------------- 
   1 - Count Digits
   2 - Find Max
   3 - Count Tags
   4 - Count Normalized Columns
   5 - Exit

=================================
  ''')
###########################
# Choice 1 - Count Digits #
###########################

# Choice 1 count function #
def count(n):
  if n < 10:
    return 1
  else:
    return 1 + count(n/10)
  
# Choice 1 main function #
def choice1():
  print("\nType <back> to go back to the previous menu or ")
  userInput = input("enter a number: ")
  if(userInput.isnumeric()):
    print("Number of digits is: ",count(int(userInput)),"\n-------------------------")
    choice1()
    # if userInput is numeric, call the recursive count function then return to choice 1
  elif(userInput == "back"):
    main()
    # if userInput is 'back', call the main function
  else:
    print("Invalid number.\n---------------")
    choice1()
    # if userInput is not numeric (excluding 'back'), return to choice 1

#################
# Main Function #
#################
def main():
  displayMenu()
  userInput = input("Enter choice number: ")
  if(userInput == "1"):
    choice1()
  elif(userInput == "2"):
    choice2()
  elif(userInput == "3"):
    choice3()
  elif(userInput == "4"):
    choice4()
  elif(userInput == "5"):
    print("Program closing... Have a nice day")
    return
  else:
    print("Invalid choice.")
    main()

main()
