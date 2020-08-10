import pandas as pd

df = pd.read_excel('fatura.xlsx', sheet_name='xml')

df = df.groupby(by=["Logo Cari", "Alt Müşteri"])

k = 0
m = 0
for i in df:
    k += 1
    for j in i[1].index:
        m += 1

print(k)
print(m)
