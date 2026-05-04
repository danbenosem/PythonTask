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



