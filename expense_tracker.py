expenses = []

def add_expense(description, amount):
    expenses.append((description, amount))

def total_expenses():
    return sum(amount for _, amount in expenses)

add_expense("Food", 500)
add_expense("Transport", 200)

print("Total Expenses:", total_expenses())
