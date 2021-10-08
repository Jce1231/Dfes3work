from BudgetAppClass import CategoryBudget
from random import randint
from termcolor import colored
budgetCategory = [
CategoryBudget(200,'food'),
CategoryBudget(200,'clothing'),
CategoryBudget(500,'bills'),
CategoryBudget(50,'entertainment'),
CategoryBudget(400,'car')
]
##Plan use file in and file out,
# use a folder to store the output for each category type.
#Code to detect the categorys
#GUI for easier user visuality? color code green for money in, red for out.


for i in range(5):
    budgetCategory[0].deposit(randint(-10,25)) #Food
    budgetCategory[1].deposit(randint(-25,50)) #Clothing
    budgetCategory[2].deposit(randint(-25,50)) #Bills
    budgetCategory[3].deposit(randint(-10,25)) #Entertainment
    budgetCategory[4].deposit(randint(-40,150)) #Car

budgetCategory[0].transfer(100,budgetCategory[2])
for i in budgetCategory:
    print(f"The ledger for {i.category} is: ")
    for j in i.ledger():
        if j >0:
            print(f"{colored(j,'green')}")
        else:
            print(f"{colored(j,'red')}")
    print(i.balance_())