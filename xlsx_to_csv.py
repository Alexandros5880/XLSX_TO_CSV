import sys
import pandas as pd

def convert_xlsx_to_csv(xlsx_file, csv_file):
    # Read the Excel file
    df = pd.read_excel(xlsx_file)
    # Export to CSV with UTF-8 encoding and comma delimiter
    df.to_csv(csv_file, index=False, encoding='utf-8', sep=',')

if __name__ == "__main__":
    importFile = sys.argv[1]
    exportFile = importFile.replace('.xlsx', '.csv')
    print(f"Converting {importFile} to {exportFile}...")
    convert_xlsx_to_csv(importFile, exportFile)
    print(f"Converted {importFile} to {exportFile}")