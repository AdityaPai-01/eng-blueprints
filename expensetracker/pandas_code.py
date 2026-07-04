import pandas as pds
from pathlib import Path
import csv, random, os, time
from datetime import datetime

# Initializing CSV File, to make sure that the data is stored locally and properly.
CSV_Path = Path(f"{Path.cwd()}\\expenses.csv")
if not CSV_Path.exists():
    CSV_Path.touch()
    with open("expenses.csv", "w") as datafile:
        writer = csv.writer(datafile)
        writer.writerow(["Transaction_ID", "Transaction_Note", "Transaction_Amount", "Transaction_Date"])

# Clears terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return "1: clear terminal executed"

def save_dataframe(df, csv_path):
    """
    Save the DataFrame back to the original CSV file.
    
    Parameters:
        df (pd.DataFrame): The DataFrame you want to save.
        csv_path (str): Path to the original CSV file.
    """
    try:
        df.to_csv(csv_path, index=False)
    except Exception as e:
        print(f"Error saving DataFrame: {e}")

# Initializing dataframe
rootdataframe = pds.read_csv(CSV_Path) 

def main(condition):
    global rootdataframe
    while condition:
        print("Welcome to Py-Expensor")
        print("For help, enter command: '.h'")
        print("-"*50)
        command = input("Enter your command >>>: ")

        # Exit the application
        if command == '.q':
            clear()
            print("You exited the application.")
            break

        # Add new data entry
        elif command == '.ne':
           while True:
            try:
                # Collect new transaction details
                transaction_id = random.randint(1000, 9999)
                transaction_note = input("Enter transaction_note: ").upper()
                transaction_amount = float(input("Enter transaction amount: "))
                transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Create a new row as a DataFrame
                new_entry = pds.DataFrame([{
                    "Transaction_ID": transaction_id,
                    "Transaction_Note": transaction_note,
                    "Transaction_Amount": transaction_amount,
                    "Transaction_Date": transaction_date
                }])

                # Append the new row to the existing DataFrame
                rootdataframe = pds.concat([rootdataframe, new_entry], ignore_index=True)

                print("Data entry added successfully.\n")
                exitconf1 = input("Do you want to exit?(Y/N): ").upper()
                if exitconf1 == "Y":
                    save_dataframe(rootdataframe, CSV_Path)
                    time.sleep(3)
                    clear()
                    break
                elif exitconf1 == "N":
                    clear()
                    continue
                else:
                    print("Invalid command entered!")
                    continue
            except Exception as e:
                print(f"Data entry could not be updated: {e}\n")
                exitconf3 = input("Do you want to exit?(Y/N): ").upper()
                if exitconf3 == 'Y':
                    clear()
                    break
                time.sleep(3)
                clear()
                continue

        # Display all the data
        elif command == '.dd':
            alldata = rootdataframe
            if not alldata.empty:
                print(alldata)
            else:
                print("There is no data.")
            costs = list(rootdataframe["Transaction_Amount"])
            total = 0
            for amount in costs:
                total += amount
            print(f"TOTAL EXPENSES OF THE MONTH: {total}\n")
            exit_opt1 = input("Enter something to exit: ")
            clear()

        # Delete data entry
        elif command == '.re':
            print(rootdataframe)
            print()
            while True:
                try:
                    del_entry_ID = int(input("Enter transaction_ID to delete the entry: "))
                    rootdataframe = rootdataframe[rootdataframe["Transaction_ID"] != del_entry_ID]
                    print("Data entry removed successfully.\n")
                    exitchoice2 = input("Do you want to exit?(Y/N):").upper()
                    if exitchoice2 == "Y":
                        save_dataframe(rootdataframe, CSV_Path)
                        clear()
                        break
                    elif exitchoice2 == "N":
                        print()
                        continue
                    else:
                        print("Invalid command entered!")
                        continue
                except Exception as e:
                    print(f"Data entry could not be removed: {e}\n")
                    exitconf2 = input("would you like to exit?(Y/N): ").upper()
                    if exitconf2 == "Y":
                        clear()
                        break
                    time.sleep(3)
                    clear()
                    continue
        
        elif command == ".st":
            keyword = input("Enter transaction keyword: ").upper()
            result = rootdataframe[rootdataframe["Transaction_Note"].str.contains(keyword, case=False, na=False)]
            if not result.empty:
                print("Transaction found.")
                print(result)
            else:
                print("Transaction not found.")
            exit2 = input("Enter anything to exit: ")
            clear()

        elif command == ".h":
            allcommands = {".ne": "Add new data entry", ".re": "Remove a data entry", ".st": "Search transaction", ".dd" : "Display all data"}
            for k, v in allcommands.items():
                print(f"{k}: {v}")
            exit3 = input("Enter anything to exit: ")
            clear()

if __name__ == "__main__":
    main(True)