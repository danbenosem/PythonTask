



import pytest


from pybank import (validate_email, calculate_balance,
                    is_strong_password, apply_interest,
                    )


def test_valid_email():


    assert validate_email("user@gmail.com") == True

def test_email_too_short():


    assert validate_email("u@g.co") == False

def test_email_no_at():


    assert validate_email("usergmail.com") == False

def test_email_starts_with_at():


    assert validate_email("@gmail.com") == False

def test_email_ends_with_at():


    assert validate_email("user.com@") == False

def test_email_has_at():


    assert validate_email("hello@semicolon.com") == True

def test_email_exactly_8():
    assert validate_email("a@bcd.co") == False

def test_email_middle_at():
    assert validate_email("user@domain.com") == True



def test_balance_deposits_and_withdrawals():


    assert calculate_balance([100, -100, 200]) == 200

def test_balance_empty_list():


    assert calculate_balance([]) == 0



def test_balance_all_debits():


    assert calculate_balance([-100, -50]) == -150


def test_balance_single_deposit():

    assert calculate_balance([500]) == 500

def test_balance_single_withdrawal():

    assert calculate_balance([-200]) == -200

def test_balance_zero():
    assert calculate_balance([100, -100]) == 0



def test_strong_password():


    assert is_strong_password("mypassword") == True

def test_weak_password():


    assert is_strong_password("abc") == False
 
    assert is_strong_password("123")== False

def test_weak_password1():


    assert is_strong_password("abc") == False


def test_password_exactly_8():


    assert is_strong_password("abcd1234") == True


def test_balance_large_numbers():


    assert calculate_balance([10000, -5000]) == 5000

def test_password_exactly_7():

    assert is_strong_password("abcd123") == False

def test_password_long():

    assert is_strong_password("myverylongpassword") == True



def test_apply_interest():

    assert apply_interest(1000, 0.1, 2) == 1210.0

def test_password_numbers_only():

    assert is_strong_password("12345678") == True

def test_apply_interest_one_year():
    assert apply_interest(1000, 0.1, 1) == 1100.0

def test_apply_interest_zero_balance():
    assert apply_interest(0, 0.1, 1) == 0.0


