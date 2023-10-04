import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

arquivo_excel_1 = 'Book3.xlsx'
#arquivo_excel_2 = 'Pasta 3.xlsx'#
df_dia_1 = pd.read_excel(arquivo_excel_1, sheet_name='Sheet1')
#df_dia_2 = pd.read_excel(arquivo_excel_2, sheet_name='exemplo')#
#df_todas_as_planilhas = pd.concat([df_dia_1,df_dia_2])#
#aqui em baixo estamos a mostrar os dados das 2 planilhas concatenadas#
#print(df_todas_as_planilhas['MARCA'])#
print(df_dia_1)
lucro_dos_vendedores = df_dia_1.groupby(['Nome']).mean()
relatorio_bonito = lucro_dos_vendedores.loc[:,"Valor do carro vendido": "Score de vendas"]

print(relatorio_bonito)
relatorio_bonito.plot(kind='bar')
plt.show()

