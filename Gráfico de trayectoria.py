import numpy as np
import matplotlib.pyplot as plt
import folium
import pandas as pd
#Nombre de todas las columnas
column_names = ["accx", "accy", "accz",
                "girox", "giroy", "giroz",
                "magx", "magy", "magz",
                "Eaccx", "Eaccy", "Eaccz",
                "Egirox", "Egiroy", "Egiroz",
                "Emagx", "Emagy", "Emagz",
                "nacc", "ngiro", "nmag",
                "lat", "lon", "sat",
                "hdop", "fecha", "hora"]

#Se pega la dirección del archivo en cuestión
file = open("C:\\Users\\Win\\Desktop\\IB2023-2\\PI\\GPSLOG_2.txt", 'r')
data = pd.read_csv(file, names = column_names, usecols = ["lat", "lon"])

#Relleno datos con 0 para controlar mejor la lista
data = data.fillna(0)
latitud = []
longitud = []
for i, j in zip(data["lat"], data['lon']):
  latitud.append(float(i)/10**6) if (i !=0) else None
  longitud.append(float(j)/10**6) if (j !=0) else None
coordenadas = [(i, j) for i,j in zip(latitud, longitud)]

#Convierto en arrays de numpy para utilizar las funciones asociadas
latitud = np.array(latitud)
longitud = np.array(longitud)
m = folium.Map(location = (latitud.mean(), longitud.mean()), zoom_start = 17)
folium.PolyLine(coordenadas, tooltip="Coast").add_to(m)
#Dependiendo el entorno en el que se ejecuta el programa
#para mostrar el mapa se puede probar con las siguientes dos opciones
# m
m.show_in_browser()