import matplotlib.pyplot as plt


def calc_speed_ups(time_p1, data):
    speed_ups = []
    for time in data:
        speed_ups.append(time_p1 / time)
    return speed_ups


time_p1_128 = 1.574162483215332
data_128 = [0.30016112327575684, 0.2930641174316406, 0.49961137771606445]

time_p1_512 = 110.90756726264954
data_512 = [17.266624927520752, 17.897562742233276, 31.755173444747925]

time_p1_1024 = 851.7835717201233
data_1024 = [140.77693152427673, 144.61570978164673, 252.8546233177185]

time_p1_2048 = 6597.449085474014
data_2048 = [1161.0003385543823, 1177.0072283744812, 2111.166804075241]


speed_up_128 = calc_speed_ups(time_p1_128, data_128)
speed_up_512 = calc_speed_ups(time_p1_512, data_512)
speed_up_1024 = calc_speed_ups(time_p1_1024, data_1024)
speed_up_2048 = calc_speed_ups(time_p1_2048, data_2048)

versions = ['p2', 'p3', 'p4']

plt.plot(versions, speed_up_128, marker='D', mfc='green', mec='green', ms='7')
plt.plot(versions, speed_up_512, marker='o', mfc='red', mec='red', ms='7')
plt.plot(versions, speed_up_1024, marker='v', mfc='blue', mec='blue', ms='7')
plt.plot(versions, speed_up_2048, marker='8', mfc='yellow', mec='yellow', ms='7')


plt.xlabel("Versão")
plt.ylabel("Speed-up")
plt.title("Gráfico Speed-up")

plt.legend(['matriz 128', 'matriz 512', 'matriz 1024', 'matriz 2048'])
plt.show()
