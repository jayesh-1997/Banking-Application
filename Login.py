from DBConnection import fetch_data
from Options import show_options


# User login:
def login_user():
    user_name = input("\nEnter username: ")
    password = input("Enter password: ")
    sql_query = "SELECT * FROM acc_info WHERE user_name = %s AND acc_pwd = %s"
    values = (user_name, password)

    user = fetch_data(sql_query, values)

    if user:
        print(f"\nWelcome, {user[1]}")
        # Assuming there's a function called show_options to display options
        show_options(user)
    else:
        print("Invalid username or password.")
