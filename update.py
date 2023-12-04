import pandas as pd
import xlwings as xw

# Function to copy data from CSV to Excel
def copy_csv_to_excel(csv_path, excel_path):
    print(f"Copying data from {csv_path} to {excel_path}")

    # Read data from CSV file
    data = pd.read_csv(csv_path)

    # Connect to the existing Excel workbook
    wb = xw.Book(excel_path)

    # Attempt to get the sheet; create it if it doesn't exist
    sheet_name = 'Code and RAM Size'
    code_ram_sheet = None
    
    for sheet in wb.sheets:
        if sheet.name.lower() == sheet_name.lower():
            code_ram_sheet = sheet
            break
    
    if code_ram_sheet is None:
        code_ram_sheet = wb.sheets.add(sheet_name, before=0)

    # Manually add a fixed header row at the beginning
    header = ['filename', 'text', 'data', 'bss', 'dec', 'hex']
    code_ram_sheet.range('A1').value = header

    # Clear existing content below the header (optional, depending on your requirements)
    code_ram_sheet.range('A2').expand('table').clear_contents()

    # Copy data to "Code and RAM Size" sheet, below the header
    code_ram_sheet.range('A2').options(index=False, header=False).value = data.values.tolist()

    # Copy images from the cover sheet to the cover sheet only
    cover_sheet = wb.sheets[0]
    if cover_sheet.name.lower() == 'cover':
        for picture in cover_sheet.pictures:
            picture.api.Copy()
            code_ram_sheet.api.Paste()

    # Close the workbook
    wb.save()
    wb.close()
    print("Copying complete.")

# Replace 'Memsize.csv' with the actual path to your CSV file
# Replace 'your_existing_excel_file.xlsx' with the path to your existing Excel file
copy_csv_to_excel('Memsize.csv', 'Report.xlsx')