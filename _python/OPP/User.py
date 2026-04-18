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
monty.balance = 20
guido.balance = 150
guido.make_withdrawal(50)
guido.display_user_balance()
guido.transfer_money(monty, 50)
guido.display_user_balance()
monty.display_user_balance()
