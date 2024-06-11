import random
import mysql.connector
from f_list_cards import list_cards


# 5. Add Card
def add_card(user):
    while True:
        card_type = int(input("Choose the card type, 1.Debit or 2.Credit: "))
        temp_num = ''.join(random.choices('0123456789', k=12))
        if card_type == 1:
            ct = "DEBIT"
            card_numb = '4126 ' + temp_num
        elif card_type == 2:
            ct = "CREDIT"
            card_numb = '4141 ' + temp_num
        else:
            print("Wrong Option. Choose the right option.")
            continue
        pin = ''.join(random.choices('0123456789', k=4))
        cvv = ''.join(random.choices('0123456789', k=3))

        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="root", database="BankDB")

            cursor = connection.cursor()

            # Insert the card into the card table
            sql = "INSERT INTO card (card_no, card_type, cvv, pin, user_name) VALUES (%s, %s, %s, %s, %s)"
            val = (card_numb, ct, cvv, pin, user[1])
            cursor.execute(sql, val)
            connection.commit()
            print(f"{ct} added successfully!")

        except mysql.connector.Error as error:
            print("Error while adding card:", error)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

        list_cards(user)
