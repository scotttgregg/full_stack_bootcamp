# Let’s represent an ATM with a class containing two attributes: a balance and an interest rate.
# A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer,
# as well as the following functions:
#
# check_balance() returns the account balance
# deposit(amount) deposits the given amount in the account
# check_withdrawal(amount) returns true if the withdrawn amount won’t put the account in the negative
# withdraw(amount) withdraws the amount from the account and returns it
# calc_interest() returns the amount of interest calculated on the account

class BankAccount:
    def __init__(self, first_name, last_name, st_balance, interest_rt):
        self.first = first_name
        self.last = last_name
        self.bal = st_balance
        self.int_rt = interest_rt


class Atm:
    def __init__(self, accounts=None):
        self.account_num = None
        self.accounts = accounts or {}


    def check_balance(self):
            return self.account_num.bal

    def deposit(self, amount):
        self.account_num.bal += amount
        return self.account_num.bal

    def check_withdrawal(self, amount):
        while True:
            if self.withdrawal(amount) > self.account_num.bal:
                print("The amount withdrawn can not exceed balance on account.")


    def withdrawal(self, amount):
        self.account_num.bal -= amount
        return self.account_num.bal

    def calc_interest(self):
        return self.account_num.bal * self.account_num.int_rt + self.account_num.bal

    def atm_menu(self, user):
        if user:
            while True:
                prompt = input('What would you like to do? (deposit, withdraw, check balance): ')
                if prompt == 'deposit':
                    money = int(input('How much would you like to deposit?: '))
                    print(self.deposit(money))
                elif prompt == 'withdraw':
                    money = int(input("How much would you like to withdraw?: "))
                    self.check_withdrawal(money)
                    print(self.withdrawal(money))
                elif prompt == 'check balance':
                    print(atm.check_balance())
                elif prompt == 'calc interest':
                    print(atm.calc_interest())



    def user_authentication(self):
        account_number = input('What is your account number?: ')

        if account_number in self.accounts:
            self.account_num = self.accounts[account_number]
            return True
        else:
            print("Not a Valid Account Number.")
            return False


dictionary_atm = {"0001": BankAccount("Scott", "Gregg", 100, 0.03),
                  "0002": BankAccount("Remington", "Henderson", 150, 0.02)}

atm = Atm(dictionary_atm)

while True:
    user = atm.user_authentication()
    atm.atm_menu(user)




