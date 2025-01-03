from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

def get_date(prompt,allow_default=False):
    date_str = input(prompt)
    
    
    # If no input is provided by the user
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)   # String format time returns todays date with the given format
    try:
        #Check for valid date input and return the required format.
        valid_date = datetime.strptime(date_str, date_format)  #Parses string into a datetime format.
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid Date format. Please enter the date in 'dd-mm-YYYY'.")
        return get_date(prompt , allow_default)     #Recursive call so that function keeps repeating until correct input is provided

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative & non-zero value")
        return amount
    except ValueError as e:
        print(e)
        return get_amount      # Recursive call

def get_category():
    category = input("Enter the category ('I' for Income or 'E' for expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
      
    print("Invalid Category. Please enter 'I' for Income or 'E' for expense.")
    return get_category()     #Recursive call

def get_description():
    return input("Enter a description(optional):")