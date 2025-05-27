import streamlit as st
import matplotlib.pyplot as plt

# Dados do ranking
faculdades = ["USP", "UFMG", "Unesp", "Unicamp", "UFRGS", "UFRJ", "UFPR", "UFF", "UFSC", "UnB"]
ranking = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Criando o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(faculdades, ranking, color='skyblue')
ax.set_xlabel('Ranking')
ax.set_ylabel('Faculdades')
ax.invert_yaxis()  # Invertendo o eixo Y para mostrar o 1º lugar no topo
ax.set_title('Ranking das 10 Melhores Faculdades de Odontologia do Brasil')

# Exibindo o gráfico no Streamlit
st.pyplot(fig)

# Fonte
st.write("Fonte: RUF 2023 | Folha de São Paulo")