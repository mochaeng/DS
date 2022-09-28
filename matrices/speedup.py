import matplotlib.pyplot as plt

time_p1_128 = 1.574162483215332
data_128 = [1.543799638748169, 1.4495034217834473, 1.4765193462371826]

time_p1_512 = 110.90756726264954
data_512 = [119.84167861938477, 99.50273489952087, 98.60044288635254]

speed_up_128 = []
for time in data_128:
    speed_up_128.append(time_p1_128 / time)

speed_up_512 = []
for time in data_512:
    speed_up_512.append(time_p1_512 / time)

# numberofemp_A = [13, 200, 250, 300, 350, 400]
# numberofemp_B = [10, 100, 150]
year = ['p2', 'p3', 'p4']

# plot a line chart
plt.plot(year, speed_up_128, marker='D', mfc='green', mec='yellow', ms='7')
plt.plot(year, speed_up_512, marker='o', mfc='red', mec='green', ms='7')

# set label name of x-axis title
plt.xlabel("Versão")

# set label name of x-axis title
plt.ylabel("Speed-up")

# set label name of chart title
plt.title("Gráfico Speed-up")

plt.legend(['matriz 128', 'matriz 512'])
plt.show()
