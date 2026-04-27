"""
Author: Harsh Yadav
Branch: CSE-DS
Project: ATM Simulation (Package Architecture)
"""

from atm_package import atm_logic

def main():
    balance = 0.0
    history = []

    while True:
        print("\n==============================")
        print("       ATM SIMULATION")
        print("==============================")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit")
        print("==============================")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            current = atm_logic.display_balance(balance)
            print("Your current balance is:", current)

        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: $"))
                balance = atm_logic.deposit(balance, amount, history)
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: $"))
                balance = atm_logic.withdraw(balance, amount, history)
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        elif choice == '4':
            atm_logic.show_history(history)

        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please select an option from 1 to 5.")

if __name__ == "__main__":
    main()
