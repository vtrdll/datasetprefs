
import pandas as pd

data = pd.read_csv('2025-05-06_Sistema_E-Saude_Medicos_-_Base_de_Dados (1).csv',sep=';', encoding='cp1252') 

   
#remove as colunas que não necessárias. 
colum = [3,5,7,9,10,11,14,15,16,18,21,22,23,24,
         25,26,27,28,29,30,31,32,33,34,35,36,37,39,40]
colum_remove = [data.columns[i] for i in colum]

data = data.drop(columns=colum_remove)



#preenche com Na padrao do pandas as linhas vazias
colum = [data.columns[i] for i in range (len(data.columns))]
data [colum] = data[colum].apply(lambda x: x.str.strip() if x.dtype=='object' else x).replace('', pd.NA)



#limpagem no campo data  de 17/08/1986 00:00:00 para --> 17/08/1986
data['Data de Nascimento'] = data['Data de Nascimento'].str[0:10]
data['Data de Nascimento'] = pd.to_datetime(data['Data de Nascimento'], dayfirst=True)



#analise correlação Desencadeou Internamento & Data do Internamento.
contagem = ((data['Desencadeou Internamento'] == 'Sim') & (data['Data do Internamento'].isna())).sum()


data.to_csv('dados_limpos.csv', sep=';', index=False, encoding='latin-1')



