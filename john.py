import openpyxl as op

workbook = op.load_workbook("excelDB.xlsx")
sheet = workbook.active

sheet ['A1'] = "ID"
sheet ['B1'] = "Customer Name"
sheet ['C1'] = "Product"
sheet ['D1'] = "Quantity"
sheet ['E1'] = "Price"
sheet ['F1'] = "Total"

sheet ['A1'] = 1"
sheet ['B1'] = "Juan Dela Cruz"
sheet ['C1'] = "Bruger"
sheet ['D1'] = "2"
sheet ['E1'] = "75"
sheet ['F1'] = "150"

sheet ['A1'] = "2"
sheet ['B1'] = "Maria Santos"
sheet ['C1'] = "Fries"
sheet ['D1'] = "3"
sheet ['E1'] = "50"
sheet ['F1'] = "150"

sheet ['A1'] = 1"
sheet ['B1'] = "Carlo Reyes"
sheet ['C1'] = "Pizza"
sheet ['D1'] = "2"
sheet ['E1'] = "350"
sheet ['F1'] = "350"

sheet ['A1'] = 1"
sheet ['B1'] = "Angela Lopez"
sheet ['C1'] = "Milktea"
sheet ['D1'] = "4"
sheet ['E1'] = "120"
sheet ['F1'] = "480"

sheet ['A1'] = 5"
sheet ['B1'] = "Kevin Ramos"
sheet ['C1'] = "Spaghetti"
sheet ['D1'] = "2"
sheet ['E1'] = "95"
sheet ['F1'] = "190"

workbook.save("ordersDB.xlsx")
