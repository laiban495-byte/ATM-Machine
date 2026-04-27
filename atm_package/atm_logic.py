"""
Logic module for ATM Simulation.
"""

def display_balance(balance):
    return f"${balance}"

def deposit(balance, amount, history):
    if amount <= 0:
        print("Amount must be greater than zero.")
        return balance
        
    balance += amount
    history.append(f"Deposited: ${amount}")
    print(f"Successfully deposited ${amount}")
    return balance

def withdraw(balance, amount, history):
    if amount <= 0:
        print("Amount must be greater than zero.")
        return balance
        
    if amount > balance:
        print("Insufficient balance!")
        return balance
        
    balance -= amount
    history.append(f"Withdrew: ${amount}")
    print(f"Successfully withdrew ${amount}")
    return balance

def show_history(history):
    if len(history) == 0:
        print("No transactions yet.")
    else:
        print("Transaction History:")
        for transaction in history:
            print("- " + transaction)
