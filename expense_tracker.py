import csv
import os
from datetime import datetime

filename = "expenses.csv"

if not os.path.exists (filename):
    with open (filename, mode= 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["date","category","amount","remarks"])

def add_expenses():
    date = input("enter the date in (dd-mm-yyyy) or else leave blank if its today: ").strip()
    if not date:
        date = datetime.now().strftime("%d-%m-%Y")

    category = input("enter the category ex: like food,clothes,travel etc: ").strip()
    amount = input("enter the amount in numbers: ").strip()
    remarks = input("enter the remarks if any : ").strip()

    with open(filename, mode='a', newline='')as file:
        writer=csv.writer(file)
        writer.writerow([date,category,amount,remarks])
    print("you have successfully added your expenses \n")

def view_expense():
    with open(filename, mode='r') as file:
        reader= csv.reader(file)
        for row in reader:
            print("  ".join(row)) 
    print()
def main():
    while True:
        print("welocome to the expense tracker")
        print("1.add expense\n2.view expenses\n3.exit")
        choice= input("choose an option (1-3): ").strip()
        if choice == '1':
            add_expenses()
        elif choice == '2':
            view_expense()
        elif choice == '3':
            print("Thank you! see you later")
            break
        else:
            print("invalid input! try again later: ")

if __name__ == "__main__" :
    main()

