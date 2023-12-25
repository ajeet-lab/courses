import mysql.connector
import tkinter as tk
from tkinter import messagebox
import random

class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit of ${amount} successful. New balance: ${self.balance}"
        else:
            return "Invalid amount for deposit."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal of ${amount} successful. New balance: ${self.balance}"
        else:
            return "Invalid amount for withdrawal."

    def check_balance(self):
        return f"Account Balance for {self.owner}: ${self.balance}"

#password='2239094467@'
class BankAccountSystem:
    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost', password='root', user='root', database='anonymous')
        if self.conn.is_connected():
            print("Connection established...")
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def create_account(self):
        random_value = random.randint(100000, 999999)
        self.account_number_var.set(f"Your Bank Account Number is: {random_value}")
        account_name = self.account_name_entry.get()
        initial_balance = int(self.initial_balance_entry.get())

        insert_query = "INSERT INTO bankaccount(Account_no_, Account_name_, Total_balance) VALUES (%s, %s, %s)"
        self.cursor.execute(insert_query, (random_value, account_name, initial_balance))
        self.conn.commit()

        account = BankAccount(random_value, account_name, initial_balance)
        messagebox.showinfo("Account Created", f"Account created successfully your account number is : {random_value}\n{account.check_balance()}")

    def check_account(self):
        account_number = int(self.account_number_entry.get())
        select_query = "SELECT * FROM bankaccount WHERE Account_no_=%s"
        self.cursor.execute(select_query, (account_number,))
        result = self.cursor.fetchall()

        self.account_info_text.config(state=tk.NORMAL)
        self.account_info_text.delete("1.0", tk.END)

        for row in result:
            self.account_info_text.insert(tk.END, f"{row}\n")

        self.account_info_text.config(state=tk.DISABLED)

    def delete_account(self):
        account_number = int(self.delete_account_entry.get())
        print("Delete account for : ", account_number)
        delete_query = "DELETE FROM bankaccount WHERE Account_no_=%s"
        self.cursor.execute(delete_query, (account_number,))
        #self.cursor.execute(delete_query)
        self.conn.commit()
        messagebox.showinfo("Account Deleted", "Account deleted successfully")

    def deposit_money(self):
            account=int(self.deposit_account_entry.get())
            amount=int(self.deposit_amount_entry.get())
            print("Amount :::: ${amount} and account :::: ${account}")

            if amount > 100:
                #self.balance += amount
                select_query=f"SELECT Total_balance FROM bankaccount WHERE Account_no_=%s"
                self.cursor.execute(select_query,(account,))
                result=self.cursor.fetchone()
            
                value_to_modify=result[0]
                modified_value=value_to_modify+ amount          
                update_query = "UPDATE bankaccount SET Total_balance = %s WHERE Account_no_=%s"
                self.cursor.execute(update_query, (modified_value,account,))
                self.conn.commit()
                messagebox.showinfo("Deposit Amount", f"Deposit of ${amount} successful. New balance: ${modified_value}")
            else:
                messagebox.showerror("Invalid amount", f"Amount is Greater then $100.")

            

    def withdrawl_money(self):
        account=int(self.withdrawl_account_entry.get())
        amount=int(self.withdrawl_amount_entry.get())

        select_query=f"SELECT Total_balance FROM bankaccount WHERE Account_no_=%s"
        self.cursor.execute(select_query,(account,))
        result=self.cursor.fetchone()
        total_amount=result[0]

        if 0 < amount <= total_amount:           
            print("Total amount :: ${value_to_modify}", total_amount)
            modified_value=total_amount - amount
            update_query = "UPDATE bankaccount SET Total_balance = %s WHERE Account_no_=%s"
            self.cursor.execute(update_query, (modified_value,account,))
            self.conn.commit()
            messagebox.showinfo("Withdrowl Amount", f"Withdrawal of ${amount} successful. New balance: ${modified_value}")
        else:
            messagebox.showerror("Invalid amount", f"Amount is Greater then $100 and less or equal total amount, Your Total amount is ${total_amount}")

    def main_menu(self):
        self.main_window = tk.Tk()
        self.main_window.title("Bank Account System")

        self.account_number_var = tk.StringVar()

        
        # Create new account Account
        tk.Label(self.main_window, text="Account Name:").grid(row=0)
        self.account_name_entry = tk.Entry(self.main_window)
        self.account_name_entry.grid(row=0, column=1, pady = 5)

        tk.Label(self.main_window, text="Initial Balance:").grid(row=0, column=2, pady = 5)
        self.initial_balance_entry = tk.Entry(self.main_window)
        self.initial_balance_entry.grid(row=0, column=3, pady = 5)

        create_account_button = tk.Button(self.main_window, text="Create Account", command=self.create_account)
        create_account_button.grid(row=0, column=4,  columnspan = 2, rowspan=2, padx=5, pady=5)

        tk.Label(self.main_window, textvariable=self.account_number_var).grid(row=5)        

        # Check Account detail
        tk.Label(self.main_window, text="Account Number:").grid(row=2)
        self.account_number_entry = tk.Entry(self.main_window)
        self.account_number_entry.grid(row=2, column=1)
        print(self.account_number_entry)

        # Check button
        check_account_button = tk.Button(self.main_window, text="Check Account", command=self.check_account)
        check_account_button.grid(row=2, column=2, padx=4, pady=5)
        
         # Show all details
        self.account_info_text = tk.Text(self.main_window, height=3, width=50, state=tk.DISABLED)
        self.account_info_text.grid(row=3, column=1, columnspan=3)

        # Delete account
        tk.Label(self.main_window, text="Account Number to Delete:").grid(row=4)
        self.delete_account_entry = tk.Entry(self.main_window)
        self.delete_account_entry.grid(row=4, column=1, pady=10)

        delete_account_button = tk.Button(self.main_window, text="Delete Account", command=self.delete_account).grid(row=4, column=2, pady=10)


        # Deposit money
        tk.Label(self.main_window, text="Enter Account Number:").grid(row=5)
        self.deposit_account_entry = tk.Entry(self.main_window)
        self.deposit_account_entry.grid(row=5, column=1, pady = 5)

        tk.Label(self.main_window, text="Enter Amount:").grid(row=5, column=2)
        self.deposit_amount_entry = tk.Entry(self.main_window)
        self.deposit_amount_entry.grid(row=5, column=3, pady = 5)
        
        deposit_money_button = tk.Button(self.main_window, text="Deposit Money", command=self.deposit_money)
        deposit_money_button.grid(row=5, column=4, pady=10)
       

       # Widthrawl money
        tk.Label(self.main_window, text="Enter Account Number:").grid(row=6)
        self.withdrawl_account_entry = tk.Entry(self.main_window)
        self.withdrawl_account_entry.grid(row=6, column=1, pady = 5)

        tk.Label(self.main_window, text="Enter Amount:").grid(row=6, column=2)
        self.withdrawl_amount_entry = tk.Entry(self.main_window)
        self.withdrawl_amount_entry.grid(row=6, column=3, pady = 5)

        withdrawl_money_button = tk.Button(self.main_window, text="Withdrawl Amount", command=self.withdrawl_money).grid(row=6, column=4, pady=10)

        self.main_window.mainloop()

if __name__ == "__main__":
    bank_system = BankAccountSystem()
    bank_system.main_menu()

