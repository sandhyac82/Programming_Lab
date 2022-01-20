class bank:
    def __init__(self):
        self.balance=0
        name=input("enter the name of account holder:")
        acno=int(input("enter the account no:"))
    
        print ("The account is created")
        print("\n name of account:",name)
        print("\n account no:",acno)
        
    def deposit(self):
        amount=int(input(" enter the amount:"))
        self.balance+=amount
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn:"))

        if (self.balance>=amount):
            self.balance-=amount
            print("\nYou Withdraw:", amount)
        else:
            print("\ninsufficient balance")
    def display(self):
       
        print("\nAvailable Balance =",self.balance)
        
b=bank()
b.deposit()
b.withdraw()
b.display()

