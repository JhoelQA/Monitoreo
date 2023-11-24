import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#EN COLAB
#file = open("data.log",'r')
#data = pd.read_csv(file, sep = ";", usecols = ["Time[us]", "Voltage[V]", "Current[mA]","Energy[mAh]"])

#En PC
file = open("C:\\Users\\Win\\Desktop\\IB2023-2\\PI\\data.log", 'r')
data = pd.read_csv(file, sep = ";", usecols = ["Time[us]", "Voltage[V]", "Current[mA]","Energy[mAh]"])

#Convierto el tiempo a segundos
data["Time[us]"] = data["Time[us]"]/10**6
#Este vector ya tiene la escala de tiempo en segundos
t = np.array(data["Time[us]"])
#Voltaje
v = data["Voltage[V]"]

#Valor donde comienza el consumo de energía
idx_E_min = np.where(data["Energy[mAh]"] != 0)[0][0]
print("A partir de este índice empieza el consumo: ", idx_E_min)

t_max = max(t)
t_min = t[idx_E_min]
print("Valor máximo del tiempo: ", t_max)
idx_tmax = np.where(t == t_max)[0][0]
print("Índice del valor máximo: ", idx_tmax)
t_medicion = t_max - t_min
print("Segundos invertidos: ", t_medicion)
print("En horas: ", t_medicion/3600)


fig, ax = plt.subplots(1,2)
fig.set_size_inches(12,3)
ax[0].plot(t[idx_E_min:idx_tmax], v[idx_E_min:idx_tmax])
ax[0].set(xlabel='Tiempo [s]', ylabel='Tensión [V]')
ax[0].set_xlim(90, 100)
ax[0].grid()

ax[1].plot(t[idx_E_min:idx_tmax], data["Current[mA]"][idx_E_min:idx_tmax])
ax[1].set(xlabel='Tiempo [s]', ylabel='Corriente [mA]')
ax[1].set_xlim(90, 100)
ax[1].grid()
fig, ax = plt.subplots()
t_horas = t/3600
ax.plot(t_horas[idx_E_min:idx_tmax], data["Energy[mAh]"][idx_E_min:idx_tmax])
ax.set(xlabel='Tiempo [h]', ylabel = "Energy[mAh]")
plt.grid()
#Aporte final 
idx_t1h = np.where((t_horas - 1)>0.0001)[0][0]
print("\nÍndice en aproximadamente t = 1h :   ", idx_t1h)
print("t[", idx_t1h, "] = ", t_horas[idx_t1h])
print("Corriente conumida promedio: ", data["Energy[mAh]"][idx_t1h], "mA")



plt.show()