import DBConnection


# 2. Add funds
def initiate_deposit(user):
    deposit_amount = int(input("Enter deposit amount: "))
    if deposit_amount < 1:
        print("Deposit a valid amount(>0)")
        return

    DBConnection.balance_add(deposit_amount, user[0], user)
