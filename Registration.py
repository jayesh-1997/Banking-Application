import random
from DBConnection import sql_connect_load
from Validation import *


def details_into_db(acc_no, user_name, address, aadhar, mobile_no, acc_pwd):
    sql_query = "INSERT INTO acc_info (acc_no, user_name, address, aadhar_no, mobile_no, acc_pwd, acc_balance) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (acc_no, user_name, address, int(aadhar), int(mobile_no), acc_pwd, 0.0)
    sql_connect_load(sql_query, values)


# Account number generation:
def generate_account_number():
    return ''.join(random.choices('0123456789', k=random.randint(11, 14)))


# Card number generation:
def generate_card(card_type):
    card_number = ''.join(random.choices('0123456789', k=16))
    pin = ''.join(random.choices('0123456789', k=4))
    cvv = ''.join(random.choices('0123456789', k=3))

    return {"type": card_type, "number": card_number, "pin": pin, "cvv": cvv}


# User Inputs:
def register_user():
    # Get valid input from user
    while True:
        user_name = input("Enter username (alphabets only): ")
        if validate_username(user_name):
            break
        else:
            print("Invalid username. Please enter alphabets only.")

    while True:
        address = input("Enter address: ")
        if validate_address(address):
            break
        else:
            print("Invalid address. Please enter alphanumeric characters with special characters.")

    while True:
        aadhar = input("Enter Aadhar number (12 digits): ")
        aadhar_with_gaps = validate_aadhar(aadhar)
        if aadhar_with_gaps:
            print("Aadhar number with automatic gaps insertion:")
            print(aadhar_with_gaps)
            break
        else:
            print("Invalid Aadhar number. Please enter 12 digits.")

    while True:
        mobile_no = input("Enter mobile number (10 digits): ")
        if validate_mobile(mobile_no):
            break
        else:
            print("Invalid mobile number.")

    while True:
        acc_pwd = input("Enter password (minimum 8 characters, alphanumeric with special characters): ")
        if validate_password(acc_pwd):
            break
        else:
            print("Invalid password. Password should be at least 8 characters long and contain alphanumeric characters with special characters.")

    # Display User details after registration
    # clean the window before displaying the details:
    # for o/p screen
    # os.system('clear')
    # fro notebook (not working, skipping to the input section)
    # clear_output(wait=True)

    print("Registration successful!")
    acc_no = generate_account_number()
    print("Your Account Number: ", acc_no)
    print("Your User Name: ", user_name)
    print("Your Address: ", address)
    print("Your Aadhar Number: ", aadhar)
    print("Your Mobile Number: ", mobile_no)
    print("Your Account Password: ", acc_pwd)
    # print("Your Balance: ",user_name)

    details_into_db(acc_no, user_name, address, aadhar, mobile_no, acc_pwd)
