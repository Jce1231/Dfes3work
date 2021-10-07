class CategoryBudget():
    balance = 0
    budget = 0
    transactions = []
    def __init__(self,limit,category):
        self.budget = limit
        self.category = category

    def deposit(self,amount):
        self.transactions.append(amount)
        self.cal_balance_()

    def withdraw(self,amount):
        self.transactions.append(-amount)
        self.cal_balance_()

    def transfer(self,amount,where):
        where.deposit(amount)
        self.withdraw(amount)
        print(where.balance_())

    def cal_balance_(self):
        self.balance = 0
        for i in self.transactions:
            self.balance += i

    def balance_(self):
        if self.balance > self.budget:
            difference = self.balance - self.budget
            return(f"You have exceeded your budget of {self.budget} for {self.category} by {difference} ")
        else:
            return(f"Your balance for {self.category} is {self.balance}")

    def ledger(self):
        return(self.transactions)