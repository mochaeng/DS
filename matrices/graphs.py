import matplotlib.pyplot as plt

# data = {'p1': 1.574162483215332, 'p2': 1.543799638748169, 'p3': 1.4495034217834473, 'p4': 1.4765193462371826}
data = {'p1': 110.90756726264954, 'p2': 119.84167861938477, 'p3': 99.50273489952087, 'p4': 98.60044288635254}

versions = data.keys()
values = data.values()

fig = plt.figure(figsize=(10, 5))

plt.bar(versions, values, color=['black', 'red', 'green', 'blue'],
        width=0.4)

plt.xlabel("versão do programa")
plt.ylabel("Velocidade em [s]")
plt.title("Gráfico de comparação de tempo para a multiplicação de 128.txt")
plt.show()
