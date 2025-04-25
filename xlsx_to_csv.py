import sys
import pandas as pd

import pandas as pd

def convert_xlsx_to_csv(xlsx_file, csv_file):
    # Read Excel
    df = pd.read_excel(xlsx_file)

    # Convert all values to strings and clean up float artifacts like '2020.0' → '2020'
    def clean_value(val):
        if pd.isna(val):
            return ''
        if isinstance(val, float) and val.is_integer():
            return str(int(val))
        return str(val).strip()

    # Apply cleanup to the entire DataFrame
    df = df.applymap(clean_value)

    # Remove rows where all columns are empty
    df = df[~df.apply(lambda row: all(cell == '' for cell in row), axis=1)]

    # Save as UTF-8 CSV with comma separator
    df.to_csv(csv_file, index=False, encoding='utf-8', sep=',')


if __name__ == "__main__":
    importFile = sys.argv[1]
    exportFile = importFile.replace('.xlsx', '.csv')
    print(f"Converting {importFile} to {exportFile}...")
    convert_xlsx_to_csv(importFile, exportFile)
    print(f"Converted {importFile} to {exportFile}")