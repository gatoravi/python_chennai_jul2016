import openpyxl

wb1 = openpyxl.load_workbook('example.xlsx')

print(wb1.get_sheet_names())

sheet = wb1.get_sheet_by_name('Sheet1')

print("The C1 value is ", sheet['C1'].value)
print("The A2 value is ", sheet['A2'].value)

sheet['C1'].value = 10000

wb.save("example.xlsx")

