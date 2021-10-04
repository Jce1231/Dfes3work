# names = 0
# while names < 5:
#     name = input("Please enter a name: ")
#     print(name + " Is awesome!")
#     names = names + 1

# for i in range(10, 21, 2):
    # print(i)
    #Iterates through a loop from 10, to 21, stepping 2 numbers at a time instead of 1
    #prints even numbers between 10 and 20, so 10,12,14,16,18,20

# varName = input("Please enter a name to check if it's a palindrome: ").lower()
# varCheck = ''
# for i in range(len(varName)-1,-1,-1):
#     varCheck = varCheck + varName[i]
# if varCheck == varName:
#     print("Congrats your name is a palindrome: " + varName)
# else:
#     print("Sorry: " + varName + " Is not a palindrome")



#https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php


#Exercise 1
# for i in range(1500,2700,5):
#     if i % 7 == 0:
#         print(i," is a multiple of both 5 and 7")


#Exercise 2
# conFaren = True
# if (input("Please press F to convert to Farenheit, press anything else to convert to Celsius: ").lower == 'f'):
#     conFaren = False

# temp = float(input("Please enter the Temperature to convert: "))
# conTemp = 0.0
# if conFaren:
#     conTemp = (temp *(9/5)) + 32
# else:
#     conTemp = (temp-32)*(5/9)
# print("Your input was: ", temp, " This converts to: ", conTemp)