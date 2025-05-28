import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker

# Aplicar estilo 'whitegrid' do seaborn
sns.set_style('whitegrid')

# Dados do ranking
faculdades = ["USP", "UFMG", "Unesp", "Unicamp", "UFRGS", "UFRJ", "UFPR", "UFF", "UFSC", "UnB"]
ranking = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Criar degradê azul
colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(faculdades)))

fig, ax = plt.subplots(figsize=(10, 6))

# Barras horizontais com cores em degradê
bars = ax.barh(faculdades, ranking, color=colors)

# Mostrar valores do ranking ao lado das barras
for bar, value in zip(bars, ranking):
    ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height()/2,
            str(value), va='center', fontsize=12, fontweight='bold', color='navy')

# Inverter eixo Y para o 1º lugar ficar no topo
ax.invert_yaxis()

# Ajustar labels e título
ax.set_xlabel('Ranking', fontsize=14, fontweight='bold')
ax.set_ylabel('Faculdades', fontsize=14, fontweight='bold')
ax.set_title('Ranking das 10 Melhores Faculdades de Odontologia do Brasil', fontsize=16, fontweight='bold', pad=15)

# Deixar eixo X com ticks inteiros e limitar o range para dar espaço para os números
ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
ax.set_xlim(0, max(ranking) + 2)

# Mostrar grid
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Remover borda direita e superior
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# Exibir o gráfico no Streamlit
st.pyplot(fig)
st.markdown("<p style='text-align:center; font-size:12px; color:gray;'>Fonte: RUF 2023 | Folha de São Paulo</p>", unsafe_allow_html=True)