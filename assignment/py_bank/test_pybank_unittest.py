import unittest


from pybank import (validate_email,
                     calculate_balance,
                     is_strong_password,
                     apply_interest,
                    )


class TestPyBank(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(validate_email("user@gmail.com"))

    def test_validate_email_too_short(self):
        self.assertFalse(validate_email("u@g.co"))

    def test_email_no_at(self):


        self.assertFalse(validate_email("usergmail.com")) 

    def test_email_starts_with_at(self):


        self.assertFalse(validate_email("@gmail.com"))

    def test_email_ends_with_at(self):


        self.assertFalse(validate_email("user.com@"))

    def test_email_has_at(self):


        self.assertTrue(validate_email("hello@semicolon.com"))


    def test_email_exactly_8(self):
       self.assertFalse(validate_email("a@bcd.co"))

    def test_email_middle_at(self):
        self.assertTrue (validate_email("user@domain.com"))



    def test_balance_deposits_and_withdrawals(self):
        self.assertEqual(calculate_balance([100, -100, 200]), 200)

    def test_balance_empty_list(self):
        self.assertEqual(calculate_balance([]), 0)

    def test_balance_all_debits(self):
        self.assertEqual(calculate_balance([-100, -50]), -150)

    def test_balance_single_deposit(self):
        self.assertEqual(calculate_balance([500]), 500)

    def test_balance_single_withdrawal(self):
        self.assertEqual(calculate_balance([-200]), -200)

    def test_balance_zero(self):
        self.assertEqual(calculate_balance([100, -100]), 0)

    def test_balance_large_numbers(self):
        self.assertEqual(calculate_balance([10000, -5000]), 5000)














    def test_strong_password(self):
        self.assertTrue(is_strong_password("mypassword"))

    def test_weak_password(self):
        self.assertFalse(is_strong_password("abc"))
        self.assertFalse(is_strong_password("123"))

    def test_weak_password1(self):
        self.assertFalse(is_strong_password("abc"))

    def test_password_exactly_8(self):
        self.assertTrue(is_strong_password("abcd1234"))

    def test_password_exactly_7(self):
        self.assertFalse(is_strong_password("abcd123"))

    def test_password_long(self):
        self.assertTrue(is_strong_password("myverylongpassword"))

    def test_password_numbers_only(self):
        self.assertTrue(is_strong_password("12345678"))




    def test_apply_interest(self):
        self.assertEqual(apply_interest(1000, 0.1, 2), 1210.0)

    def test_apply_interest_one_year(self):
        self.assertEqual(apply_interest(1000, 0.1, 1), 1100.0)

    def test_apply_interest_zero_balance(self):
        self.assertEqual(apply_interest(0, 0.1, 1), 0.0)

