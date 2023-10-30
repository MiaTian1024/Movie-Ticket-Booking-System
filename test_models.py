import pytest
from Models import Customer

def test_customer_login():
    # Create a customer
    customer = Customer("JohnDoe", "johndoe@example.com", "password123")

    # Test a valid login
    assert customer.login("johndoe@example.com", "password123") == True

    # Test an invalid login with wrong email
    assert customer.login("wrongemail@example.com", "password123") == False

    # Test an invalid login with wrong password
    assert customer.login("johndoe@example.com", "wrongpassword") == False