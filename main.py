##############################################
# FCS 49 - Assignment 2 - Oussama Walieddine #
##############################################

print(" FCS 49 - Assignment 2 - Oussama Walieddine\n--------------------------------------------")


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

# Finds the number of digits in an integer #

# Count function #
def count(n):
  if n < 10:
    return 1
  else:
    return 1 + count(n/10)
  
# Choice 1 main function #
def choice1():
# Request input + option to go back
  print("\nType <back> to go back to the previous menu or ")
  userInput = input("enter a number: ")
# if userInput is numeric, call the recursive count function then return to choice 1
  if(userInput.isnumeric()):
    print("Number of digits is: ",count(int(userInput)),"\n--------------------------")
    choice1()
# if userInput is 'back', call the main function
  elif(userInput == "back"):
    main()
# if userInput is not numeric (excluding 'back'), return to choice 1
  else:
    print("Invalid number.\n---------------")
    choice1()


#######################
# Choice 2 - Find Max #
#######################

# Finds the maximum in a list of integers #

# Max function #
def maxValue(nList):
  if len(nList) == 1:
    return nList[0]
  else:
    if(nList[0] < nList[1]):
      return maxValue(nList[1:])
    else:
      return maxValue([nList[0]] + nList[2:])

# Choice 2 main function #
def choice2():
  print("\nType <back> to go back to the previous menu or ")
  userInput = input("enter a list of integers separated by a space:\n").split()

# if user types 'back' return to main function
  if(userInput[0] == "back"):
    main()

# check if all values in list are numeric before passing intList to the maxValue function
  elif(x.isnumeric() for x in userInput):
    intList = [int(i) for i in userInput]
    print(maxValue(intList)," is the maximum value in the list.\n--------------------------")
    choice2()

# Values in list are not all numeric, return to choice 2
  else:
    print("Invalid list.\n---------------")
    choice2()
   






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
    print("Program terminated... Have a nice day")
    return
  else:
    print("Invalid choice.")
    main()

main()