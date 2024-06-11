import mysql.connector


# DB Connection:
# Connection to lead data:
def sql_connect_load(sql_query, values=None):
    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="root", database="BankDB")

        cursor = connection.cursor()

        if values is not None:
            cursor.execute(sql_query, values)
        else:
            cursor.execute(sql_query)

        connection.commit()
        print("Query executed successfully!")

    except mysql.connector.Error as error:
        print("Error while executing SQL query:", error)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()


# Connection to fetch data:
def fetch_data(sql_query, values=None):
    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="root", database="BankDB")

        cursor = connection.cursor()

        if values is not None:
            cursor.execute(sql_query, values)
        else:
            cursor.execute(sql_query)

        # For fetching the data
        data = cursor.fetchone()
        return data

    except mysql.connector.Error as error:
        print("Error while executing SQL query:", error)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()


# Connection to add balance:
def balance_add(deposit_amount, acc_no, user):
    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="root", database="BankDB")

        cursor = connection.cursor()

        # Update the user's balance in the database
        cursor.execute("UPDATE acc_info SET acc_balance = acc_balance + %s WHERE acc_no = %s", (deposit_amount, acc_no))
        connection.commit()

        # Fetch and print the updated balance
        cursor.execute("SELECT acc_balance FROM acc_info WHERE acc_no = %s", (acc_no,))
        updated_balance = cursor.fetchone()[0]
        print(f"Your account has been credited with {deposit_amount}. New balance is {updated_balance}.")

    except mysql.connector.Error as error:
        print("Error while executing SQL query:", error)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            from Options import show_options
            show_options(user)
