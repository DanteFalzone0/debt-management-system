#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import json


def get_total_amount_due(loan_list: list):
    result = 0
    for loan in loan_list:
        result += loan["loan_amount"] - loan["amount_paid"]
    return result


def add_loan_to_list(loan_list_path: str):
    existing_data = json.loads(open(loan_list_path).read())
    new_loan = {}
    print("Input the date of the loan as MM/DD/YYYY.")
    new_loan["loan_date"] = input("> ")
    print("Input the amount of the loan in dollars as a whole number without decimals.")
    new_loan["loan_amount"] = int(float(input("> ")))
    new_loan["amount_paid"] = 0
    print("Saving entered data...")
    existing_data.append(new_loan)
    f = open(loan_list_path, "w")
    f.write(json.dumps(existing_data, indent=4))
    f.close()


def print_summary(loan_list_path: str):
    loans = json.loads(open(loan_list_path).read())
    print("")
    print("Index | Date     | Amount loaned | Amount paid")
    print("------+----------+---------------+------------")
    total_amount_owed = 0
    for i in range(len(loans)):
        print("%5i |%s| $%12i | $%10i" % (i, loans[i]["loan_date"], loans[i]["loan_amount"], loans[i]["amount_paid"]))
        total_amount_owed += loans[i]["loan_amount"]
        total_amount_owed -= loans[i]["amount_paid"]
    print("------+----------+---------------+------------")
    print(f"Total amount owed: ${total_amount_owed}\n")


def make_payment(loan_list_path: str):
    print("Input the index of the loan on which you would like to log a payment.")
    index = int(input("> "))
    loans = json.loads(open(loan_list_path).read())
    print("Input the number of dollars you have paid on that loan.")
    payment = int(float(input("> ")))
    loans[index]["amount_paid"] += payment
    f = open(loan_list_path, "w")
    f.write(json.dumps(loans, indent=4))
    f.close()    


def process_user_input():
    print("What would you like to do?")
    print("(Input one of the following numbers to select an operation)")
    print("1 - Add a loan to the list")
    print("2 - View summary of existing loans")
    print("3 - Make a payment to a specific loan")
    print("0 - exit")
    user_choice = input("> ")
    while user_choice not in ['1', '2', '3', '0']:
        print("Invalid selection.")
        user_choice = input("> ")
    if user_choice == '1':
        add_loan_to_list("loans.json")
    elif user_choice == '2':
        print_summary("loans.json")
    elif user_choice == '3':
        make_payment("loans.json")
    elif user_choice == '0':
        print("Goodbye.")
        exit(0)


def main():
    if "--dump-data" in sys.argv:
        loans = json.loads(open("loans.json").read())
        print(json.dumps(loans, indent=4))
    print("Welcome to Dante's loan and debt management system.")
    while True:
        process_user_input()


if __name__ == "__main__":
    main()
