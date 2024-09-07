import matplotlib.pyplot as plt

data_128 = {
    "p1": 1.574162483215332,
    "p2": 0.30016112327575684,
    "p3": 0.2930641174316406,
    "p4": 0.49961137771606445,
}
data_512 = {
    "p1": 110.90756726264954,
    "p2": 17.266624927520752,
    "p3": 17.897562742233276,
    "p4": 31.755173444747925,
}
data_1024 = {
    "p1": 851.7835717201233,
    "p2": 140.77693152427673,
    "p3": 144.61570978164673,
    "p4": 252.8546233177185,
}
data_2048 = {
    "p1": 6597.449085474014,
    "p2": 1161.0003385543823,
    "p3": 1177.0072283744812,
    "p4": 2111.166804075241,
}

versions = data_2048.keys()
values = data_2048.values()

fig = plt.figure()

plt.bar(
    versions,  # type: ignore
    values,  # type: ignore
    color=["black", "red", "green", "blue"],
    width=0.4,
)
plt.axis = 1

plt.xlabel("versão do programa")
plt.ylabel("Velocidade em [s]")
plt.title("Gráfico de comparação de tempo para a multiplicação de 2048.txt")
plt.show()
