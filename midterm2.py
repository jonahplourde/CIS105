import csv

# Challenge 1 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Define classes

print("\nCHALLENGE 1\n")

class Account:
    def __init__(self, deposit, withdraw):
        self._deposit = deposit
        self._withdraw = withdraw

    def show_balance(self):
        balance = self._deposit - self._withdraw
        print(f"Account balance: ${balance}")


class SavingsAccount(Account):
    def __init__(self, deposit, withdraw, interest):
        super().__init__(deposit, withdraw)
        self.interest = interest

    def show_balance(self):
        balance = self._deposit - self._withdraw + self.interest
        print(f"Savings Account balance (with interest): ${balance}")


class CheckingAccount(Account):
    def __init__(self, deposit, withdraw, overdraft):
        super().__init__(deposit, withdraw)
        self.overdraft = overdraft

    def show_balance(self):
        balance = self._deposit - self._withdraw - self.overdraft
        print(f"Checking Account balance (with overdraft): ${balance}")

# Create accounts
accounts = [
    SavingsAccount(1000, 200, 50),
    CheckingAccount(1500, 500, 100),
    SavingsAccount(500, 50, 10),
    CheckingAccount(800, 100, 0),
]

# Loop and call a method to show balances on each account
for account in accounts:
    account.show_balance()


# Challenge 2 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Define classes

print("\nCHALLENGE 2\n")

class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def restock(self, amount):
        self.quantity += amount
        print(f"Restocked {self.name} by {amount}. New quantity: {self.quantity}")

    def __str__(self):
        return f"Product: {self.name}, Quantity: {self.quantity}"
    
class Supplier:
    def __init__(self, name):
        self.name = name
        self.products = []  # Composition: Supplier has Products

    def add_product(self, product):
        self.products.append(product)

    def __str__(self):
        return f"Supplier: {self.name}"

class Inventory:
    def __init__(self):
        self.suppliers = []

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)

    def print_inventory(self):
        print("Inventory:")
        for supplier in self.suppliers:
            print(supplier)
            for product in supplier.products:
                print(f"  {product}")

# Example usage
inv = Inventory()
s1 = Supplier("Acme")
s2 = Supplier("Walmart")
p1 = Product("Steak", 10)
p2 = Product("Bread", 5)
p3 = Product("Candy", 2)
s1.add_product(p1)
s1.add_product(p2)
s2.add_product(p3)
inv.add_supplier(s1)
inv.add_supplier(s2)

# Restock products
p1.restock(5)
p3.restock(10)

# Print inventory
inv.print_inventory()

# Challenge 3 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Define classes

print("\nCHALLENGE 2\n")

class Student:
    def __init__(self, name, gpa, major):
        self.name = name
        self.gpa = float(gpa)
        self.major = major
    def __str__(self):
        return f"{self.name} | GPA: {self.gpa} | Major: {self.major}"

class StudentManager:
    def __init__(self, filename):
        self.students = []
        try:
            with open(filename, 'r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    student = Student(row['name'], row['gpa'], row['major'])
                    self.students.append(student)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"Error reading file: {e}")
    def print_students(self):
        for student in self.students:
            print(student)
    def filter_by_gpa(self, min_gpa):
        return [s for s in self.students if s.gpa >= min_gpa]
    def export_filtered(self, filtered, out_filename):
        try:
            with open(out_filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['name', 'gpa', 'major'])
                for s in filtered:
                    writer.writerow([s.name, s.gpa, s.major])
            print(f"Exported filtered students to {out_filename}")
        except Exception as e:
            print(f"Error writing file: {e}")

# Example usage:
filename = 'students.csv'  # Make sure this file exists with columns: name,gpa,major
manager = StudentManager(filename)
print("All students:")
manager.print_students()

min_gpa = 3.0
filtered = manager.filter_by_gpa(min_gpa)
print(f"\nStudents with GPA >= {min_gpa}:")
for s in filtered:
    print(s)
manager.export_filtered(filtered, 'filtered_students.csv')
