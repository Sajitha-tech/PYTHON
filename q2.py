class BankAccount:

    def __init__(self,name,Account_number,type_of_account,balance):
        self.name=name
        self.Account_number=Account_number
        self.type_of_account=type_of_account
        self.balance=balance

    def display(self):
        print("\n name:",self.name,"\n Account_Number:",self.Account_number,"\n Type_of_Account:",self.type_of_account,"\n Balance:",self.balance)
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        self.balance=self.balance-amount

c1=BankAccount("Anu",10001,"Savings",10000)
c1.deposit(2000)
c1.withdraw(500)
c1.display()
