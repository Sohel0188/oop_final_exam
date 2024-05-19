class User:
    def __init__(self,name,email,address) -> None:
        self.name = name
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, email, address,account_type) -> None:
        super().__init__(name, email, address)
        self.account_number = name+email
        self.account_type = account_type
        self.balance = 0
        self.history = []
        self.loan_taken = 0 

    def find_item_account(self,acc_number):
        for item in Bank.users:
            print(item.account_number)
            print(acc_number)
            if item.account_number.lower() == acc_number.lower():
                return item
        return None
    
    def transfer_balance(self,acc_number,amount):
        
        item = self.find_item_account(acc_number)
        if item:
            if self.balance > amount:
                item.balance += amount
                self.balance -= amount
                self.history.append(f'Transfer Balance in {acc_number} Amount is {amount}\n')
                print("Your Balance is Successfully Transfer \n")
            else:
                print("Transfer Amount Exceeded \n")
        else:
            print("Account Not Found \n")
        
        
    def create_account(self,customer):
        Bank.users.append(customer)

    def deposit(self,bank,amount):
        if(amount>0):
            self.balance +=amount
            bank.total_balance += amount
            print('Balance Added !')
            self.history.append(f'Add Balance {amount} \n')
        else:
            print('Sorry amount must be More then 1 \n') 

    def withdraw(self,bank,amount):
        if bank.is_bankrupt == False:
            if self.balance >= amount:
                self.balance -= amount
                bank.total_balance -= amount
                self.history.append(f'Withdraw Balance {amount} \n')
                print(f'Your withdrow money is {amount}\n')
                print('Thank you for using us\n')
            else:
                print('You do not have enough money\n')
        else:
            print("Sorry we are Bankrupt\n")
       
    
    

    def chack_balance(self):
        print(f'Your Balance is {self.balance}\n')

    def transaction_history(self):
        for item in self.history:
            print (item)


    def take_loan(self,bank,amount):
        if bank.is_bankrupt == False:
            if bank.loan_feature == True:
                if self.loan_taken <2:
                    self.balance +=amount
                    bank.total_loan_amounts += amount
                    bank.total_balance -= amount
                    self.loan_taken += 1
                    self.history.append(f'Take Loan {amount}\n')
                    print(f'You got loan,Your balance is {self.balance} \n')
                else:
                    print("You are not eligable for loan\n")
            else:
                print('Sorry This feature is currently unavailable\n')
        else:
            print('Sorry We are Bankrupt\n')

class Admin(User):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address)

    def add_new_customer(self, customer):
        Bank.users.append(customer)

    def delete_customer_account(self,bank,name):
        bank.delete_customer_account(name)

    def view_customer_list(self,bank):
        bank.view_customer_list()

    def bank_available_balance(self,bank):
        bank.total_balance_amount()

    def total_loan_amount(self,bank):
        bank.total_loan_amount()

    def bankrupt(self,bank,value):
        bank.bankrupt(value)
        
class Bank:
    users = []
    def __init__(self,bank_name) -> None:
        self.bank_name = bank_name
        self.is_bankrupt = False
        self.loan_feature = True
        self.total_loan_amounts = 0
        self.total_balance = 10000

    def bankrupt(self,value):
        if value == 0:
            self.is_bankrupt = True
        elif value == 1:
            self.is_bankrupt = False

    def find_item(self, name):
        for item in self.users:
            if item.name.lower() == name.lower():
                return item
        return None
    
    def delete_customer_account(self, name):
        item = self.find_item(name)
        if item:
            self.users.remove(item)
            print("Customer deleted\n")
        else:
            print("Customer not found\n")

    def view_customer_list(self):
        print("Our Customer List\n")
        print("Name \t Email \t Address\t Account Number")
        for item in Bank.users:
            print(f"{item.name}\t{item.email}\t{item.address}\t{item.account_number}")
            
    def total_loan_amount(self):
        print(f'Total Loan Amount : {self.total_loan_amounts}\n')
    
    def total_balance_amount(self):
        print(f'Bank Total Balance is {self.total_balance}\n')

    def loan_features(self,value):
        if value == 0:
            self.loan_feature = False
            print('Loan feature is off now \n')
        elif value == 1:
            self.loan_feature = True
            print('Loan feature is active now')

Amar_bank = Bank('Amar Bank')
def register():
    name = input('Enter Your Name : ')
    email = input('Enter Your Email : ')
    address = input('Enter Your Address : ')
    print("1 : Current Account\n2 : Savings Account")
    account_type = int(input())
    account = "current" if account_type == 1 else "savings"

    customer = Customer(name, email, address, account)
    customer.create_account(customer)
    print("Account created successfully!")
    user_menu(customer)

def login():
    print("Enter User Name: ")
    user_name = input()
    print("Enter User Password (Email): ")
    user_password = input()
    
    for customer in Bank.users:
        if customer.name == user_name and customer.email == user_password:
            print("Login successful!")
            user_menu(customer)
            return
    print("Invalid account")

def user_menu(customer):
    while True:
        print(f"Welcome {customer.name}!!")
        print("1. Deposit Balance  ")
        print("2. Withdraw Balance  ")
        print("3. Check Balance  ")
        print("4. Account History  ")
        print("5. Take Loan  ")
        print("6. Transfer Banalce  ")
        print("7. Exit ")

        choice = int(input("Enter Any Nubmer : "))
        if choice == 1:
            balance = int(input("Enter Your Deposit Amount : "))
            customer.deposit(Amar_bank,balance)
        elif choice == 2:
            amount = int(input('Enter Yout Withdraw Amount : '))
            customer.withdraw(Amar_bank,amount)
        elif choice == 3:
            customer.chack_balance()
        elif choice == 4:
            customer.transaction_history()
        elif choice == 5:
            loan_amount = int(input('Enter Your Loan Amount : '))
            customer.take_loan(Amar_bank,loan_amount)
        elif choice == 6:
            acc_num = input("Enter Account Number : ")
            tr_amount = int(input("Enter Transfer Amount : "))
            customer.transfer_balance(acc_num,tr_amount)
        elif choice == 7:
            break
        else:
            print('Invalid Input')

def admin_menu():
    name = input('Enter Your Name : ')
    email = input('Enter Your Email : ')
    address = input('Enter Your Address : ')
    
    admin = Admin(name,email,address)

    while(True):
        print(f"Welcome {admin.name}!!")
        print("1. Add New Account  ")
        print("2. Delete Account ")
        print("3. See All User Accounts List  ")
        print("4. Total Available Balance Of The Bank ")
        print("5. Total Loan Amount  ")
        print("6. On or Off The Loan Feature")
        print("7. On or Off The Bankrupt Feature  ")
        print("8. Exit ")
        choice = int(input("Enter Any Nubmer : "))
        if choice == 1:
            name = input('Enter Your Name :')
            email = input('Enter Your Email :')
            address = input('Enter Your Address :')
            print("1 : Current Account\n2 : Savings Account")
            account_type = int(input())
            print(account_type)
            if(account_type ==1):
                account = "Current"
            elif(account_type == 2):
                account = "Savings"
            customer = Customer(name,email,address,account)
            admin.add_new_customer(customer)
        elif choice == 2:
            name = input("Enter The Name Of User : ")
            admin.delete_customer_account(Amar_bank,name)

        elif choice == 3:
            admin.view_customer_list(Amar_bank)
        elif choice == 4:
            admin.bank_available_balance(Amar_bank)
        elif choice == 5:
            admin.total_loan_amount(Amar_bank)
        elif choice == 6:
            print('1 : Loan Feature On \n0 : Loan Feature Off')
            value = int(input('Enter Value : '))
            admin.loan_feature(Amar_bank,value)
        elif choice == 7:
            print('1 : Active Bank \n0 : Bankrupt')
            option = int(input())
            admin.bankrupt(Amar_bank,option)
        elif choice == 8:
            break
        else:
            print('Invalid Input')
while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        print("1 : Login \n2 : Register ")
        value = int(input())

        if value == 1:
            login()
        elif value == 2:
            register()
        else:
            print('Invalid Input')
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input!!")
