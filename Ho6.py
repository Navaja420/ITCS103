from openpyxl import Workbook
from datetime import datetime

def favperson():
    current_year = datetime.now().year
    records = []

    print("--- Favorite People Recorder ---")
    print("Please enter information for 3 favorite persons.\n")

    for i in range(1, 4):
        print(f"Person {i}:")
        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()

        # Input validation
        while True:
            try:
                birth_year = int(input("Birth Year: ").strip())
                if 1900 <= birth_year <= current_year:
                    break
                else:
                    print(f"Enter a year between 1900 and {current_year}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        age = current_year - birth_year

        records.append({
            "ID": i,
            "First Name": first_name,
            "Last Name": last_name,
            "Birth Year": birth_year,
            "Age": age
        })
        print()

    #  Create Excel file properly
    wb = Workbook()
    ws = wb.active
    ws.title = "Favorite People"

    headers = ["ID", "First Name", "Last Name", "Birth Year", "Age"]
    ws.append(headers)

    for record in records:
        ws.append([
            record["ID"],
            record["First Name"],
            record["Last Name"],
            record["Birth Year"],
            record["Age"]
        ])

    # Save file safely
    try:
        excel_filename = "favorite_people.xlsx"
        wb.save(excel_filename)
        print(f"Data successfully saved to '{excel_filename}'.\n")
    except PermissionError:
        print("❌ Error: Close the Excel file before saving!")

    #  Display output
    print("=== Saved Records ===")
    print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Birth Year':<12} {'Age':<5}")
    print("-" * 55)

    for record in records:
        print(f"{record['ID']:<5} {record['First Name']:<15} {record['Last Name']:<15} {record['Birth Year']:<12} {record['Age']:<5}")

# Run program
favperson()
