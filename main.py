import random
import numpy as np
import time
import matplotlib.pyplot as plt



mas1 = [random.randint(1, 10) for i in range(10**6)]
mas2 = [random.randint(1, 10) for i in range(10**6)]

time_start = time.perf_counter()
mas3 = [mas1[i]*mas2[i] for i in range(0, 10**6)]
all_time = time.perf_counter() - time_start
print(all_time)

mas1 = np.array(mas1)
mas2 = np.array(mas2)
time_start = time.perf_counter()
np.multiply(mas1, mas2)
all_time = time.perf_counter() - time_start
print(all_time)


arr = np.genfromtxt('data1.csv', delimiter=';')
time = arr[1:100, 0]
time = time[:, np.newaxis]
percent = arr[1:100, 3]
percent = percent[:, np.newaxis]
fuel_consumption = arr[1:100, 17]
fuel_consumption = fuel_consumption[:, np.newaxis]
correlation = np.subtract(fuel_consumption, percent)

plt.plot(time, percent, 'green', label='percent(time)')
plt.plot(time, fuel_consumption, 'purple', label='fuel_consumption(time)')
plt.plot(time, correlation, 'orange', label='correlation')
plt.title('Задание 2')
plt.xlabel('Время, с')
plt.ylabel('Положение дроссельной заслонки (%)\nЧасовой расход топлива (л\час)')
plt.grid()
plt.legend(loc='lower right')
plt.show()


x = np.linspace(-5*np.pi, 5*np.pi)
y = np.cos(x)
z = np.sin(x)
fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, 'indigo')
plt.title('Задание 3')
plt.show()

