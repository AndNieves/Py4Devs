from openpyxl import load_workbook

xls_url = 'Workbook.xlsx'

wb = load_workbook(xls_url)
ws = wb['ASheet']

for idx, row in enumerate(ws.rows):
    values = [cell.value for cell in row[1::]]
    for value in values:
        print(value)
