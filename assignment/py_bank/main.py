from pybank import (validate_email, calculate_balance,
                    is_strong_password, apply_interest,
                    get_transaction_summary)

transactions = []
summary_transactions=[]

while True:

    email = input("Enter email: ")
    if validate_email(email):
    
        break
    else:

      print("Invalid email, try again!")


while True:

    password = input("Enter password: ")

    if is_strong_password(password):
    
        break
    else:

      print("Weak password, try again!")

print("Login successful!")

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Apply Interest")
    print("5. Transaction Summary")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        amount = float(input("Amount: "))
        transactions.append(amount)
        summary_transactions.append(["credit",amount])
        print("Deposited!")

    elif choice == "2":
        amount = float(input("Amount: "))
        transactions.append(-amount)
        summary_transactions.append(["debit",amount])
        print("Withdrawn!")

    elif choice == "3":
        print(f"Balance: {calculate_balance(transactions)}")

    elif choice == "4":
        rate = float(input("Rate (e.g 0.1): "))
        years = int(input("Years: "))
        result = apply_interest(calculate_balance(transactions), rate, years)
        print(f"After interest: {result}")

    elif choice == "5":
        summary = get_transaction_summary(summary_transactions)
        print(f"Total Credits: {summary[0][1]}")
        print(f"Total Debits: {summary[1][1]}")
        print(f"Net Balance: {summary[2][1]}")
        print(f"Transaction Count: {summary[3][1]}")

    elif choice == "6":
        print("Goodbye!")
        break
