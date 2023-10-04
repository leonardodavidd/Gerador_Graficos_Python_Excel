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
lucro_dos_vendedores = df_dia_1.groupby(['Nome']).sum()
relatorio_bonito = lucro_dos_vendedores.loc[:,"Valor do carro vendido": "Score de vendas"]
print(relatorio_bonito)
relatorio_bonito.plot(kind='bar')
plt.title('Valor que cada cliente vendeu')
plt.show()

lucro_dos_vendedores2 = df_dia_1.groupby(['Resultados']).sum()
relatorio_bonito2 = df_dia_1.loc[:,"Média de todas as vendas"]
relatorio_bonito2.plot(kind='box')
plt.title('Média de todas as vendas')
plt.show()

lucro_dos_vendedores2 = df_dia_1.groupby(['Resultados']).sum()
relatorio_bonito2 = lucro_dos_vendedores2.loc[:,"Mediana de todas as vendas"]
relatorio_bonito2.plot(kind='box')
plt.title('Mediana de todas as vendas')
plt.show()

lucro_dos_vendedores2 = df_dia_1.groupby(['Resultados']).sum()
relatorio_bonito2 = lucro_dos_vendedores2.loc[:,"Moda de todas as vendas"]
relatorio_bonito2.plot(kind='box')
plt.title('Moda de todas as vendas')
plt.show()

lucro_dos_vendedores2 = df_dia_1.groupby(['Resultados']).sum()
relatorio_bonito2 = lucro_dos_vendedores2.loc[:,"Desvio Padrão"]
relatorio_bonito2.plot(kind='area')
plt.title('Desvio Padrão')
plt.show()

lucro_dos_vendedores2 = df_dia_1.groupby(['Resultados']).sum()
relatorio_bonito2 = lucro_dos_vendedores2.loc[:,"Curtose"]
relatorio_bonito2.plot(kind='box')
plt.title('Curtose')
plt.show()

lucro_dos_vendedores2 = df_dia_1.groupby(['Resultados']).sum()
relatorio_bonito2 = lucro_dos_vendedores2.loc[:,"Assimetria"]
relatorio_bonito2.plot(kind='box')
plt.title('Assimetria')
plt.show()

lucro_dos_vendedores2 = df_dia_1.groupby(['Resultados']).sum()
relatorio_bonito2 = lucro_dos_vendedores2.loc[:,"Lucro Líquido"]
relatorio_bonito2.plot(kind='bar')
plt.title('Lucro Líquido')
plt.show()












