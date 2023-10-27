##############################################
# FCS 49 - Assignment 2 - Oussama Walieddine #
##############################################

# print program title #
print(" FCS 49 - Assignment 2 - Oussama Walieddine\n--------------------------------------------")


################
# Display Menu #
################

# define display menu function #
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

# define count function (recursive) #
def count(n):
  # if n is less than 10, the number consists of 1 digit
  if n < 10:
    return 1
  # if n is greater than 10, the number consists of 1 digit plus the number of digits in int(n/10)
  # int(n/10) is n minus the last digit
  else:
    return 1 + count(n/10)
  
# define choice 1 main function #
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

# define max function (recursive) #
def maxValue(nList):
  
  if len(nList) == 1:
  #if the list contains only 1 value, return that value as maxValue
    return nList[0]
  else:
    # if the list contains more than 1 value, check if the first value is smaller than the second value
    if(nList[0] < nList[1]):
      # if true, delete the first value by returning maxValue of the remaining list (second value till end of list)
      return maxValue(nList[1:])
    else:
      # if false, delete the second value by returning maxValue of the first value + the remaining list (third value till end of list)
      return maxValue([nList[0]] + nList[2:])
      
  # after enough recursions, the list will be truncated to only 1 value, and will be returned as maxValue

# define choice 2 main function #
def choice2():
  print("\nType <back> to go back to the previous menu or ")
  # split user input into a list of strings
  userInput = input("enter a list of integers separated by a space:\n").split()
  # check if all values in the list are numeric
  inputEval = [x.isnumeric() for x in userInput]
  numeric = True
  for i in inputEval:
    if(i == False):
      numeric = False    

# if user types 'back' return to main function
  if(userInput == ["back"]):
    main()

# if all values are numeric, call the recursive maxValue function then return to choice 2
  elif(numeric == True):
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
