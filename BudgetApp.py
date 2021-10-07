from BudgetAppClass import CategoryBudget
from random import randint
budgetCategory = [
CategoryBudget(200,'food'),
CategoryBudget(200,'clothing'),
CategoryBudget(500,'bills'),
CategoryBudget(50,'entertainment'),
CategoryBudget(400,'car')
]


for i in range(5):
    budgetCategory[0].deposit(randint(-10,25)) #Food
    budgetCategory[1].deposit(randint(-25,50)) #Clothing
    budgetCategory[2].deposit(randint(-25,50)) #Bills
    budgetCategory[3].deposit(randint(-10,25)) #Entertainment
    budgetCategory[4].deposit(randint(-40,150)) #Car

budgetCategory[0].transfer(100,budgetCategory[2])
for i in budgetCategory:
    print(f"The ledger for {i.category} is: {i.ledger()}")
    print(i.balance_())