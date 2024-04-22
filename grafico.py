import matplotlib.pyplot as plt
from matplotlib import style

# Anos de 2018 a 2024
anos = list(range(2017, 2025))

# Rentabilidade para CDI, IPCA e Fundo (em %)
cdi = [0, 6.43, 12.7, 15.88, 21, 36, 53.6, 58.5]
ipca = [0, 3.75, 8.22, 13.11, 24.4, 31.6, 36.9, 37.5]
fundo = [0, 5, -2, -6, -1, -7, -13, -24]

print(plt.style.available)

plt.style.use('seaborn-v0_8-pastel')

# Configurar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(anos, cdi, label='CDI')
plt.plot(anos, ipca, label='IPCA')
plt.plot(anos, fundo, label='Muraoka FIA')
plt.xlabel('Year')
plt.ylabel('Performance (%)')
plt.title('')
plt.xticks(anos)
plt.yticks(range(-30, 71, 10))
plt.grid(True)
plt.legend()

# Mostrar o gráfico
plt.tight_layout()
plt.show()