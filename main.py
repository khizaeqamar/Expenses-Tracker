# Project : Expenses Tracker

expenses = []

print("WELCOME TO EXPENSES TRACKER")

while True:
    print("\n=== EXPENSES TRACKER ===")
    print("1- Add Expense")
    print("2- View Expenses")
    print("3- Total Expenses")
    print("4- Exit")

    choice = input("Please Enter Your Choice: ")

    # 1️⃣ Add Expense
    if choice == "1":
        name = input("Enter Expense Name: ")
        category = input("Enter Category (Food, Travel, etc): ")
        amount = float(input("Enter Amount: "))

        expense = {
            "name": name,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)
        print("✅ Expense added successfully!")

    # 2️⃣ View Expenses
    elif choice == "2":
        if len(expenses) == 0:
            print("❌ No Expenses Added!")
        else:
            print("\n--- All Expenses ---")
            for i in range(len(expenses)):
                print(
                    i + 1,
                    expenses[i]["name"],
                    "| Rs.", expenses[i]["amount"],
                    "|", expenses[i]["category"]
                )

    # 3️⃣ Total Expenses
    elif choice == "3":
        total = 0
        for i in range(len(expenses)):
            total += expenses[i]["amount"]

        print("💰 Total Expense: Rs.", total)

    # 4️⃣ Exit
    elif choice == "4":
        print("👋 Program exited. Goodbye!")
        break

    else:
        print("❌ Invalid choice! Try again.")
