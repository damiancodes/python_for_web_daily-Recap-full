from abc import ABC, abstractmethod
#encapusalation
class Account:
    def __init__(self, account_id, holder_name, balance):
        self.account_id = account_id
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} New balance:  {self.balance}")

    def withdraw(self, amount):
        print(f"Withdrawe {amount} from account with balance:  {self.balance}")
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawed {amount} from account with balance:  {self.balance}")


        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

    def get_holder_name(self):
        return self.holder_name

 #inheritance
class Customer(Account):
    def __init__(self, account_id, holder_name, balance, phone_number):
        super().__init__(account_id, holder_name, balance)
        self.phone_number = phone_number

#polymorphism
class Transaction:
      def __init__(self, amount):
          self.amount = amount
      def execute(self, account):
          pass


class DepositTransaction(Transaction):
    def execute(self, account):
        account.deposit(self.amount)

class WithdrawTransaction(Transaction):
    def execute(self, account):

        account.withdraw(self.amount)

#Abstraction
class PaymentSystem(ABC):
    @abstractmethod
    def process_payment(self, payment):
        pass

class MpesaPaymentSystem(PaymentSystem):
      def process_payment(self,amount):
         print(f"Processing Mpesa payments of {amount} ")


#example usage
mpesa = MpesaPaymentSystem()
account1=Customer(account_id=1, holder_name="Damian", balance=100, phone_number="254700532551")
deposit = DepositTransaction(amount=100)
withdraw = WithdrawTransaction(amount=1000)
deposit.execute(account1)
withdraw.execute(account1)
print(f"The balance of {account1.get_holder_name()} is {account1.get_balance()} ")