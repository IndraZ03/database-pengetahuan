import pandas as pd

# Membuat DataFrame contoh
df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})

# Baris baru yang ingin ditambahkan
new_row = {'A': 4, 'B': 'd'}

# Menambahkan baris baru menggunakan append
df = df._append(new_row, ignore_index=True)

print(df)

