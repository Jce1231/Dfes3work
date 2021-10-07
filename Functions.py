# def mark(hwM,asM,esM):
#     hwM = (hwM / 25) * 100 #Get homework as a percentage
#     asM = (asM / 50)*100 #Get assignment mark as a percent
#     return((hwM+asM+esM)/3) #Average them out
# def grade(intMark):
#     if intMark >= 80: #Checks the input to see what grade it'd equate to
#         return("A")  #If grade is below 50, it's a fail.
#     elif intMark >= 70:
#         return("B")
#     elif intMark >= 60:
#         return("C")
#     elif intMark >=50:
#         return("D")
#     else:
#         return("Fail")




# studName = input("Please enter your name: ")
# intHomework = int(input("Please enter your homework mark out of 25: "))
# intAssignment = int(input("Please enter your Assignment mark out of 50: "))
# intExamScore = int(input("Please enter your exam score out of 100: "))
# #Get my stuff

# while intHomework >25 or intHomework < -1:
#     intHomework = int(input("Please enter a homework mark between 0 and 25: "))
# while intAssignment >50 or intAssignment < -1:
#     intAssignment = int(input("Please enter your Assignment mark between 0 and 50: "))
# while intExamScore > 100 or intExamScore < -1:
#     intExamScore = int(input("Please enter an exam score between 0 and 100: "))
# #Making sure the input is in the correct range.
# intICTMark = round(mark(intHomework,intAssignment,intExamScore)) #Rounds the result from mark to get rid of the decimal.
# intGrade = grade(intICTMark) #generates the grade based on mark

# print(f"{studName}, your overall mark is {intICTMark} graded at a {intGrade}") #Pretty output for the user