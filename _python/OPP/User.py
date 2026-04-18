class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def make_withdrawal(self, amount):
        self.balance -= amount
        return self

    def deposit(self, amount):
        self.balance += amount
        return self

    def display_user_balance(self):
        print(f"username : {self.name}, balance: ${self.balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.deposit(amount) 
        return self


guido = User("Guido van Rossum")
monty = User("Monty")
alice=User('Alice')

# guido.deposit(100)
# guido.deposit(200)
# guido.deposit(300)
# guido.make_withdrawal(50)
# guido.display_user_balance()
guido.deposit(100).deposit(200).deposit(300).make_withdrawal(50).display_user_balance()

# monty.deposit(100)
# monty.deposit(200)
# monty.make_withdrawal(50)
# monty.make_withdrawal(20)
# monty.display_user_balance()
monty.deposit(100).deposit(200).make_withdrawal(50).make_withdrawal(20).display_user_balance()

# alice.deposit(400)
# alice.make_withdrawal(50)
# alice.make_withdrawal(20)
# alice.make_withdrawal(10)
# alice.display_user_balance()
alice.deposit(400).make_withdrawal(50).make_withdrawal(20).make_withdrawal(10).display_user_balance()

# guido.transfer_money(alice, 50)
# guido.display_user_balance()
# alice.display_user_balance()
guido.transfer_money(alice, 50).display_user_balance()
alice.display_user_balance()
