import pandas as pd

df = pd.read_excel('fatura.xlsx', sheet_name='xml')

df = df.groupby(by=["Logo Cari", "Alt Müşteri"])

#df = df.index.values.tolist()

xml = ''
k = 0
for i in df:
    transaction = ''
    bill = ''
    k = 0
    for j in i[1].index:
        print(i[1].iloc[k]['Kaynak']) 
        k += 1