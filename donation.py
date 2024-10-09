import pyodbc
import datetime
from abc import ABC, abstractmethod
from util.db_conn_util import connect_db
# from entity.cash_donation import CashDonation

class Donation(ABC):
    def __init__(self, donor_name: str, amount: float):
        self.donor_name = donor_name
        self.amount = amount

    @abstractmethod
    def record_donation(self):
        pass

def display_donations():
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM donations")
            donations = cursor.fetchall()
            if not donations:
                print("No donations recorded.")
            else:
                print("Donations:")
                for donation in donations:
                    print(f"ID: {donation[0]}, Donor: {donation[1]}, Amount: ${donation[2]}")
        except pyodbc.Error as e:
            print(f"Error retrieving donations: {e}")
        finally:
            connection.close()

def record_donation(donor_name: str, amount: float):
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            # Check if the donation already exists
            cursor.execute("SELECT * FROM donations WHERE donor_name = ? AND amount = ?", (donor_name, amount))
            existing_donation = cursor.fetchone()
            if existing_donation:
                print("This donation has already been recorded.")
                return
            
            # Insert the new donation
            cursor.execute("INSERT INTO donations (donor_name, amount) VALUES (?, ?)", (donor_name, amount))
            connection.commit()
            print("Donation recorded successfully.")
        except pyodbc.Error as e:
            print(f"Error recording donation: {e}")
        finally:
            connection.close()

def make_donation():
    try:
        donor_name = input("Enter donor's name: ")
        amount = float(input("Enter donation amount: "))
        if amount < 10:
            raise ValueError("Minimum donation amount is $10.")
        donation = CashDonation(donor_name, amount, datetime.date.today())
        print(donation.record_donation())
        # Record the donation in the database
        record_donation(donor_name, amount)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

class CashDonation(Donation):
    def __init__(self, donor_name: str, amount: float, donation_date: datetime.date):
        super().__init__(donor_name, amount)
        self.donation_date = donation_date

    def record_donation(self):
        return f"Recorded cash donation of ${self.amount} by {self.donor_name} on {self.donation_date}"