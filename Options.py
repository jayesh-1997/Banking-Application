from a_show_info import *
from c_add_benf import *
from e_add_card import add_card
from f_list_cards import list_cards
from g_transfer_funds import transfer_funds
from h_view_transactions import view_transactions
from i_change_pin import change_pin
from j_update_info import update_info


def show_options(user):
    s1 = "1. Display Information"
    s2 = "2. Add funds"
    s3 = "3. Add Beneficiary"
    s4 = "4. Beneficiaries List"
    s5 = "5.  Add Card"
    s6 = "6. List of Cards"
    s7 = "7. Transfer Funds"
    s8 = "8. View Transactions"
    s9 = "9. Change PIN"
    s10 = "10. Update Information"

    print("\nOptions (0. Exit):")
    print(f"{s1:<{25}}{s2:<{21}}{s3:<{25}}{s4:<{25}}{s5:<{25}}")
    print(f"{s6:<{25}}{s7:<{21}}{s8:<{25}}{s9:<{25}}{s10:<{25}}")


    choice = input("Enter your choice: ")
    if choice == '1':
        show_account_info(user)
    elif choice == '2':
        initiate_deposit(user)
    elif choice == '3':
        add_beneficiary(user)
    elif choice == '4':
        list_beneficiaries(user)
    elif choice == '5':
        add_card(user)
    elif choice == '6':
        list_cards(user)
    elif choice == '7':
        transfer_funds(user)
    elif choice == '8':
        view_transactions(user)
    elif choice == '9':
        change_pin(user)
    elif choice == '10':
        update_info(user)
    elif choice == '0':
        print("Exiting\n")
    else:
        print("Invalid option. Please try again.")
        show_options(user)
