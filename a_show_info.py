from b_add_funds import *


# 1. Display Account Information
def show_account_info(user):
    print("Account Information:")
    print("Account Number:", user[0])
    print("Balance:", user[-1])

    from Options import show_options
    show_options(user)

    if user[-1] == 0:
        print("Account balance is 0. Make Deposit? (y for yes or another other key for no):")
        decision = input().lower()
        if decision == 'yes':
            initiate_deposit(user)
            print("Transaction Successful!")
            show_options(user)
        else:
            show_options(user)
