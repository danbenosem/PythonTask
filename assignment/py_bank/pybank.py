def validate_email(email):
    if len(email) <=8:
        return False
    if "@" not in email:
        return False
    if email[0] == "@" or email[-1] == "@":
        return False
    return True



def calculate_balance(transactions):
    if transactions == []:
        return 0
    
    balance = 0
    for amount in transactions:
        balance += amount
    return balance





def is_strong_password(password):
    if len(password) >= 8:
        return True
    return False



def apply_interest(balance, rate, years):
    
        
        compound_interest = balance * (1 + rate) ** years
        return round(compound_interest, 2)


def get_transaction_summary(transactions):
    total_credits = 0
    total_debits = 0

    for transaction in transactions:
        if transaction[0] == "credit":
            total_credits += transaction[1]
        elif transaction[0] == "debit":
            total_debits += transaction[1]

    net_balance = total_credits - total_debits
    transaction_count = len(transactions)

    return [
        ["total_credits", total_credits],
        ["total_debits", total_debits],
        ["net_balance", net_balance],
        ["transaction_count", transaction_count]
    ]
