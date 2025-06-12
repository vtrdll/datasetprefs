import pandas as pd 
import matplotlib.pyplot as plt
from datetime import datetime



data = pd.read_csv('dados_limpos.csv', sep=';', encoding= 'cp1252')

current_dateTime = datetime.now()
data['Data de Nascimento'] = pd.to_datetime(data['Data de Nascimento'])
delta = current_dateTime - data['Data de Nascimento'] 
data['Idade'] = delta.dt.days / 365.25
total_idade = data['Idade'].value_counts().head(20).to_dict()
idades = [f"{k:.1f}" for k in total_idade.keys()]  
quantidades = list(total_idade.values())




plt.figure(figsize=(12, 6))
plt.bar(idades, quantidades, color='skyblue')
plt.xticks(rotation=45)
plt.xlabel('Idade (anos)')
plt.ylabel('Quantidade')
plt.title('10 Idades dominantes. ')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()