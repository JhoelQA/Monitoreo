#Prueba de git
import serial
import time
archivo = open("C:\\Users\\Win\\Documents\\Arduino\\PI_1\\acelerómetro ODR = 952Hz.txt",'w')
serialArduino = serial.Serial('COM4', 9600)
time.sleep(1)
start_time = time.time()
while True:
    datos = serialArduino.readline().decode("ascii")
    print(datos)
    archivo.write(datos)
    if(time.time() - start_time > 20):
        print("Conexión terminada")
        break

archivo.close()
serialArduino.close()