import pandas as pd
import csv
from datetime import datetime   #Built-in module for date and time purposes
from data_entry import get_date,get_amount,get_category,get_description


#Step1: Create a class CSV and a file which will store the data.
class CSV:
    CSV_file = "finance_data.csv"
    Columns = ["Date","Amount","Category","Description"]
    Format = "%d-%m-%Y"
    @classmethod     #Can access class methods but not the instance. Takes 'cls' as its parameter.
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_file)    #Using pandas read the CSV file 
        except FileNotFoundError:
            df = pd.DataFrame(columns= cls.Columns)
            df.to_csv(cls.CSV_file, index=False)   #Export dataframe into a csv file
            
    @classmethod
    def add_entry(cls, date,amount,category,description):
        
    # Store the data in a dictionary
        
        new_entry = {
            "Date": date,
            "Amount":amount,
            "Category":category,
            "Description":description
        }
        
        #Open the csv file and add the new entry
        with open(cls.CSV_file, "a", newline="") as csvfile:          #"a" is a append parameter.
            writer = csv.DictWriter(csvfile, fieldnames = cls.Columns)     #New entry added into the dictionary
            writer.writerow(new_entry)
        print("Entry added Successfully!")
        
    
    #Creating a function which provides summary information of the transactions according to
    #filtered dates in the dataframe.
           
    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_file)
        df["Date"] = pd.to_datetime(df["Date"] , format = CSV.Format )
        
        #Parsing a string into a datetime object .Datetime object helps us to filter out and search for different dates.
        start_date = datetime.strptime(start_date,CSV.Format)
        end_date = datetime.strptime(end_date,CSV.Format)  
    
    #Masking different rows inside the dataframe to see if we should select that row.
        mask = (df["Date"] >= start_date) & (df["Date"] <= end_date)
        filtered_df = df.loc[mask] 
    
        if filtered_df.empty:
            print("No transactions found between the given dates.")
        else:
            print(f"Transactions from {start_date.strftime(CSV.Format)} to {end_date.strftime(CSV.Format)}") 
            print(filtered_df.to_string(index = False, formatters = {"Date" : lambda x: x.strftime(CSV.Format)}))
            
            total_income = filtered_df[filtered_df["Category"] == "Income"]["Amount"].sum()
            total_expense = filtered_df[filtered_df["Category"] == "Expense"]["Amount"].sum()
            print("\nSummary") 
            print(f"Total Income: Rs{total_income:.2f}")        #.2f rounds the value to two decimal places.
            print(f"Total Expense: Rs{total_expense:.2f}") 
            print(f"Net Savings: Rs{total_income - total_expense:.2f}")
    
        return filtered_df  
    #Get_transaction function ended.    
    
def func():
    CSV.initialize_csv()
    date = get_date(
        "Enter the date of transaction (dd-mm-yyyy) or today's date: ",
        allow_default= True
    )
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date,amount,category,description)

#Creating a main function to run our functions properly and interact with our finance tracker.

def main():
    while True:
        print("\n1.Add a new transaction")
        print("2.View the transaction and summary within a date range")
        print("3.Exit")
        choice = input("Enter a choice(1-3): ")
       
        if choice == "1":
            func()
        
        elif choice == "2":
            start_date = get_date("Enter start date (dd-mm-yyyy): ")
            end_date = get_date("Enter end date (dd-mm-yyyy): ")
            CSV.get_transactions(start_date, end_date)
        
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter choice from 1-3.")
            
if __name__ == "__main__":
    main()
        
    


