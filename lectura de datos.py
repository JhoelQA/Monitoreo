import numpy as np
import matplotlib.pyplot as plt
def graficar_acel(v):
  #Aquí se coloca la dirección de los archivos
  file = open("C:\\Users\\Win\\Documents\\Arduino\\PI_1\\acelerómetro ODR = "+ str(v)+"Hz.txt", 'r')
  a_x = []
  a_y = []
  a_z = []
  i = 0
  for line in file:
      aux = line.replace("\n",'')
      aux = aux.split('\t')
      try:
        a_x.append(float(aux[0]))
        a_y.append(float(aux[1]))
        a_z.append(float(aux[2]))
      except ValueError:
        print("error","on line",i)
      i = i+1
  file.close()
  t = np.linspace(0, 20, len(a_x))
  #plt.figure()
  plt.plot(t, a_x)
  plt.plot(t, a_y)
  plt.plot(t, a_z)
  plt.title("ODR = "+ str(v) + " Hz")
  plt.xlabel("Tiempo [s]")
  plt.ylabel("Aceleración [g]")
  plt.legend(["a_x", "a_y", "a_z"])
  plt.grid()
  plt.show()

#graficar_acel(476) -> tiene problemas en el txt
freq = [10, 50, 119, 238, 476, 952] #conjunto de frecuencias utilizadas - ODR 
for i in freq:
   graficar_acel(i) 