from turtle import color
from matplotlib.patches import Shadow
import matplotlib.pyplot as plt
import matplotlib.patches as patches
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

plt.barh(meses_x, total_y, color='#70BBFF')
plt.xlabel('TOTAL ATENDIMENTOS')
plt.ylabel('MES')
plt.title('ATENDIMENTO POR MÊS')






contagem = data['Desencadeou Internamento'].value_counts()
size = [(contagem['Sim']/len(data)*100), (contagem['Nao']/len(data)*100)]
labels = (f'Desencadeou Internamento {size[0]:.1f}% ({contagem['Sim']})', f'Não Internamento {size[1]:.1f}% ({contagem["Nao"]})')
c = ['#118DFF','#12239E']
fig1, ax1 = plt.subplots()
ax1.set_title('PERCENTUAL DE ATENDIMENTOS QUE GERARAM INTERNAÇÃO', fontsize=10, pad=30)
ax1.pie(size, labels=labels, startangle= 90, colors =c, pctdistance=1.2)
ax1.axis('equal')



fig, ax = plt.subplots(figsize=(5, 3))

card = patches.FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0.05", 
                              linewidth=2, edgecolor='blue', facecolor='#f0f0f0', zorder=0)
ax.add_patch(card)


ax.text(0.5, 0.85, 'Atendimentos', ha='center', va='center', fontsize=14, fontweight='bold', zorder=1)

# Adicionando texto dentro do "card"
ax.text(0.5, 0.5, f'{len(data)}', ha='center', va='center', fontsize=12, zorder=1)

# Removendo os eixos para que o card tenha uma aparência limpa
ax.set_axis_off()

# Ajustando os limites do gráfico para corresponder ao tamanho do card
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)








plt.show()

