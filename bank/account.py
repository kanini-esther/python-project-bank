
# class BankAccount:
#     bank = "KCB"
#     def __init__(self,first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.balance = 0
        
#     def account_name(self):
#         name = "{} account for {} {}".format(
#         self.bank, self.first_name, self.last_name)
#         return name
#     def deposit(self):
#         deposit = int(input('Enter the amount you want to deposiit'))
#         self.balance += deposit
#         print ('{}, you have deposited  {}, in your account'.format(self.first_name,deposit))
#     def withdraw(self):
#         withdraw =int(input('Enter amount you want to withdraw'))
#         self.balance -=withdraw
#         if balance < withdraw:
#             print('{},your have insufficient balance'.format(self.first_name,self.balance))
#         else:
#             balance > deposit()
#         print ('{},your balance is {},in your account'.format(self.first_name,self.balance))
            

        
        
    
# acc1 = BankAccount("Esther","Kanini",'+254707792765')
# acc1 .deposit()
# acc1.withdraw()
# print(acc1.balance)
    
from datetime import datetime
class BankAccount:
    bank="KCB"
    deposit_history = []
    loan = {}
    loan_balance = 0
    applied_for_loan = False
    # loan
    _MAXIMUM_LOAN_BORROWABLE = 3000000
    _LOAN_INTEREST_RATE = .12

    #Constructor
    def __init__(self, first_name, second_name):
        self.first_name=first_name
        self.second_name=second_name
        self.balance=0 

    #Returns the current time in string form
    def _getCurrentTime(self):
        now = datetime.now()
        now_formatted = now.strftime("%b %d %Y, %H:%M:%S")
        return now_formatted

    def account_name(self):
        name= "{} account for {} {} ".format(self.bank, self.first_name,self.second_name)
        return name
    def deposit(self,amount):
        if amount >0:
            self.balance+=amount
            timeDate = self._getCurrentTime()
            transaction_details = {"amount": amount, "date":timeDate}
            self.deposit_history.append(transaction_details)
            print("You have deposited {} to your account at {}".format(amount, timeDate))
        else:
            print("Too low ")
  
  
    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            print("You have withdrawed {} from your account".format(amount))
        else:
            print("Amount too low")
    def get_balance(self):
        return "The balance of {} is {} ".format(self.account_name(),self.balance)
    
    def get_statement(self):
        for statement_item in self.deposit_history:
            print("On",statement_item['date'], ", you deposited KES", statement_item['amount'])
    
    def getLoanBalance(self):
        print("Your balance is KES",self.loan_balance,"for loan KES", self.loan["amount_borrowed"],"Borrowed on", self.loan["date"])
    def requestLoan(self, amount):
        # When customer has no Loan balance Give a loan
        if not self.loan_balance > 0:
            timeDate = self._getCurrentTime()
            self.loan["date"] = timeDate
            self.loan["amount_borrowed"] = amount
            self.loan_balance += amount
        #Else Deny loan
        else:
            print("Err:Loan Request Failed Reason:", end="")
            print(self.getLoanBalance())
            
    def payLoan(self,amount):
        if self.loan_balance == 0:
            print("You have no loan balance")
        elif amount > self.loan_balance:
            self.loan_balance = 0
        elif amount <= self.loan_balance:
            self.loan_balance -= amount

        return

    
acc1=BankAccount("Berril","Wanjiku")
acc2=BankAccount("Faith", "Stella")

acc1.deposit(-2000)
acc2.deposit(520)
acc1.deposit(300)
acc2.deposit(40)
acc1.withdraw(210)
acc2.withdraw(530)
acc1.withdraw(220)
acc2.withdraw(610)

acc2.get_statement()
acc1.requestLoan(3000)
acc1.requestLoan(999)
acc1.payLoan(600)
acc1.getLoanBalance()
print(acc1.get_balance())
print(acc2.get_balance())

print(acc1.account_name())
print(acc2.account_name())

acc1.withdraw()
print(acc1.balance)
        

    
    
  