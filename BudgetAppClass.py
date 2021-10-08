class CategoryBudget():
    def __init__(self,limit:float,category):
        self.budget = limit
        self.category = category
        self.transactions = []
    def deposit(self,amount):
        self.transactions.append(amount)
        self.cal_balance_()

    def withdraw(self,amount):
        self.transactions.append(-amount)
        self.cal_balance_()

    def transfer(self,amount,where):
        where.deposit(amount)
        self.withdraw(amount)
    def cal_balance_(self):
        self.balance = 0
        for i in self.transactions:
            self.balance += i

    def balance_(self):
        if self.balance > self.budget:
            difference = self.balance - self.budget
            return(f"Your balance for {self.category} is £{self.balance}, which is £{difference} more than your budget of £{self.budget}")
        else:
            difference = self.budget - self.balance
            return(f"Your balance for {self.category} is £{self.balance}, which is £{difference} less than your budget of £{self.budget}")

    def ledger(self):
        return(self.transactions)