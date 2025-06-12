import pandas as pd 
import matplotlib.pyplot as plt



data = pd.read_csv('dados_limpos.csv', sep=';', encoding= 'cp1252')

#atendimentos por unidade
contagem = data['Código da Unidade'].value_counts()
mapa_codigos = data.drop_duplicates('Código da Unidade').set_index('Código da Unidade')['Descrição da Unidade'].to_dict()

unidade = []
total = []

for codigo, quantidade in contagem.head(20).items():
    descricao = mapa_codigos.get(codigo, 'Descrição não encontrada')
    print(f"Código: {codigo} - {descricao} - Quantidade: {quantidade}")

    unidade.append(descricao)
    total.append(quantidade)


plt.figure(figsize=(12, 8))
plt.barh(unidade, total, color='skyblue')
plt.xlabel('Quantidade')
plt.title('Top 20 Unidades por ATENDIMENTO')
plt.gca().invert_yaxis()  

for i, v in enumerate(total):
    plt.text(v + max(total)*0.01, i, str(v), va='center')

plt.tight_layout()
plt.show()


#Taxa de internação por unidade
contagem_df = data.groupby('Descrição da Unidade')['Desencadeou Internamento'].value_counts().unstack(fill_value=0)
top20_sim = contagem_df.sort_values(by='Nao', ascending=False).head(20)

top20_sim.plot(kind='barh', stacked=True, figsize=(10, 8))

plt.show()