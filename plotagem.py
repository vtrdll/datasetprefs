import matplotlib.pyplot as plt
import pandas as pd 

data = pd.read_csv('dados_limpos.csv', sep=';', encoding='cp1252')

data['Data do Atendimento']= pd.to_datetime(data['Data do Atendimento'], dayfirst=True)
meses_numeros = data['Data do Atendimento'].dt.month.unique()
meses = data['Data do Atendimento'].dt.month_name().unique()

dict_meses = {}
cont = 1 

for i in range (len(meses)):
    
    mes = data[data['Data do Atendimento'].dt.month == cont]
   
    dict_meses[meses[i]] = len(mes)
    cont +=1 

meses_x = list(dict_meses.keys())
total_y =  [dict_meses[meses_x[i]] for i in range(len(meses_x)) ]

#grafico horizontal
plt.barh(meses_x, total_y, color='#70BBFF')
plt.xlabel('TOTAL ATENDIMENTOS')
plt.ylabel('MES')
plt.title('ATENDIMENTO POR MÊS')


#grafico redondo 
contagem = data['Desencadeou Internamento'].value_counts()
size = [(contagem['Sim']/len(data)*100), (contagem['Nao']/len(data)*100)]
labels = (f'Desencadeou Internamento {size[0]:.1f}% ({contagem['Sim']})', f'Não Internamento {size[1]:.1f}% ({contagem["Nao"]})')
c = ['#118DFF','#12239E']
fig1, ax1 = plt.subplots()
ax1.set_title('PERCENTUAL DE ATENDIMENTOS QUE GERARAM INTERNAÇÃO', fontsize=10, pad=30)
ax1.pie(size, labels=labels, startangle= 90, colors =c, pctdistance=1.2)
ax1.axis('equal')
plt.show()
