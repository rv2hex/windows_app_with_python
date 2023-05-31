import hashlib
import eel
# name of folder where the html, css, js, image files are located
eel.init('templates')

@eel.expose
def demo(x):
   return x**2

# 1000 is width of window and 600 is the height
eel.start('index.html', size=(320, 680))

class Block:
    def __init__(self, data, prev_hash):
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode("utf-8"))
        return sha.hexdigest()

class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        return f"Personal Details\n\nName: {self.name}\nAge: {self.age}\nGender: {self.gender}"


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 20000

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                return "Deposit amount must be positive"
            else:
                self.balance += amount
                return "Account balance has been updated: $" + str(self.balance)
        except ValueError:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                return "Withdrawal amount must be positive"
            elif amount > self.balance:
                return "Withdrawal bounce: Insufficient balance"
            else:
                self.balance -= amount
                return "Account balance has been updated: $" + str(self.balance)
        except ValueError:
            return "Invalid withdrawal amount"

    def view_balance(self):
        details = self.show_details()
        return details + "\nAccount balance: $" + str(self.balance)


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("genesis block", "0")

    def add_block(self, data):
        prev_hash = self.chain[-1].hash
        new_block = Block(data, prev_hash)
        self.chain.mainend(new_block)


blockchain = Blockchain()

user = Bank("homan", 16, "Male")
