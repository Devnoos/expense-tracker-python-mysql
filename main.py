from module.add import add_expense
from module.view import view_expenses
from module.update import update_expense
from module.total import total_expense
def main():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Total Expense")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            update_expense()
        elif choice == "4":
            total_expense()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again!")
if __name__ == "__main__":
    main()
