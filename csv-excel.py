import pandas as pd

# Membaca file CSV
data_csv = pd.read_csv('example.csv', encoding='latin-1')

# Menyimpan data ke file Excel
data_csv.to_excel('file.xlsx', index=False)
