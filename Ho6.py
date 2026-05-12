from openpyxl import Workbook
from datetime import datetime

def favperson():
    wb = Workbook()
    ws = wb.active
    ws.title = "Favorite People"

    # Headers (same as screenshot)
    headers = ["ID", "First Name", "Last Name", "Birth Year", "Age"]
    ws.append(headers)

    current_year = datetime.now().year

    print("=== Favorite People Recorder ===")

    for i in range(1, 4):
        print(f"\nPerson {i}")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")

        birth_year = int(input("Birth Year: "))
        age = current_year - birth_year

        # Add to Excel
        ws.append([i, first_name, last_name, birth_year, age])

    # Save file
    wb.save("favorite_people.xlsx")

    print("\n✅ Data saved successfully!")
    print("Check your file: favorite_people.xlsx")

favperson()