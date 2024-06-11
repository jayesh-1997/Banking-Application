import mysql.connector
import decimal


# 7. Transfer Funds
def transfer_funds(user):
    beneficiary_number = input("Enter beneficiary account number: ")

    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="Nine@123", database="Bank_Sch")
        cursor = connection.cursor()

        # Check if the beneficiary account exists in the Beneficiaries table
        query = "SELECT * FROM Benf WHERE user_name = %s AND benf_acc_no = %s"
        cursor.execute(query, (user[1], beneficiary_number))
        beneficiary = cursor.fetchone()
        if not beneficiary:
            print("Beneficiary account not found. Please add the beneficiary first.")
            show_options(user)
            return

        amount = decimal.Decimal(input("Enter amount to transfer: "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
            return

            # Check if the user has sufficient balance
        query = "SELECT acc_balance FROM acc_info WHERE user_name = %s"
        cursor.execute(query, (user[1],))
        sender_balance = cursor.fetchone()[0]
        if sender_balance < amount:
            print("Insufficient balance. Transaction aborted.")
            return

        # Consume any unread results before executing the update query
        cursor.fetchall()

        # Deduct the transferred amount from the sender's account balance
        new_sender_balance = sender_balance - amount
        update_sender_query = "UPDATE acc_info SET acc_balance = %s WHERE user_name = %s"
        cursor.execute(update_sender_query, (new_sender_balance, user[1]))
        connection.commit()  # Consume the result

        # Add the transferred amount to the beneficiary's account balance
        update_beneficiary_query = "UPDATE acc_info SET acc_balance = acc_balance + %s WHERE user_name = %s"
        cursor.execute(update_beneficiary_query, (amount, beneficiary[0]))

        # Insert transaction record
        insert_transaction_query = "INSERT INTO transaction (sender_acc_no, benf_acc_no, amount) VALUES (%s, %s, %s)"
        cursor.execute(insert_transaction_query, (user[0], beneficiary[2], amount))

        connection.commit()
        print("Funds transferred successfully.")

    except mysql.connector.Error as error:
        print("Error while Updating transaction:", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    show_options(user)
