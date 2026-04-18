class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def make_withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def display_user_balance(self):
        print(f"username : {self.name}, balance: ${self.balance}")

    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.deposit(amount) 


guido = User("Guido van Rossum")
monty = User("Monty")
alice=User('Alice')

guido.deposit(100)
guido.deposit(200)
guido.deposit(300)
guido.make_withdrawal(50)
guido.display_user_balance()

monty.deposit(100)
monty.deposit(200)
monty.make_withdrawal(50)
monty.make_withdrawal(20)
monty.display_user_balance()

alice.deposit(400)
alice.make_withdrawal(50)
alice.make_withdrawal(20)
alice.make_withdrawal(10)
alice.display_user_balance()

guido.transfer_money(alice, 50)
guido.display_user_balance()
alice.display_user_balance()
