import numpy as np#libreria encargada de realizar los calculos correspondientes para las señales
import matplotlib.pyplot as plt#esta libreria se encarga de graficar y visualizarlas 


#Crear las lineas de la grafica
t=np.linspace(-3,3,1000) #Vector de tiempo
dt = t[1]- t[0]
frecuencias = np.fft.fftshift(np.fft.fftfreq(len(t), t[1]-t[0]))

#Pulso rectangular
pulso = np.where(np.abs(t) <= 1,1,0)

#Escalonar
escalon = np.where(t >= 0,1,0)

#Senoidal
f=5 # frecuencia 
senoidal = np.sin(2*np.pi*f*t)


#Muestra las 3 graficas 
fig, ax = plt.subplots(1,3)

#Grafica rectangular
ax[0].plot(t,pulso, color="red")
ax[0].set_title("Pulso rectangular")
ax[0].set_xlabel("tiempo")
ax[0].set_ylabel("Amplitud")
ax[0].grid(True)

#Grafica escalon
ax[1].plot(t,escalon, color="blue")
ax[1].set_title("Escalon")
ax[1].set_xlabel("tiempo")
ax[1].set_ylabel("Amplitud")
ax[1].grid(True)

#Grafica senoidal
ax[2].plot(t,senoidal, color="orange")
ax[2].set_title("Señal senoidal")
ax[2].set_xlabel("Tiempo")
ax[2].set_ylabel("Amplitud")
ax[2].grid(True)

#mostrar graficas
plt.tight_layout()
plt.show()


#FFT para graficar las 3 en una sola ventana
#Tranformada de Fourier con fft, nos ayuda a convertir la señal del dominio del tiempo a dominio de frecuencia
#Usamos fftshift para centrar el espectro en 0 y visualizarlo de mejor forma
fft_pulso = np.fft.fftshift(np.fft.fft(pulso))
fft_escalon = np.fft.fftshift(np.fft.fft(escalon))
fft_senoidal = np.fft.fftshift(np.fft.fft(senoidal))

#magnitudes de las 3
#La magnitud nos indica que frecuencias estan presentes y su intensidad
magnitud_pulso = np.abs(fft_pulso)
magnitud_escalon = np.abs(fft_escalon)
magnitud_senoidal=np.abs(fft_senoidal)

#fase de las 3 
#La fase indica el desplazamiento temporal de cada componente de frecuencia en la señal
fase_pulso = np.angle(fft_pulso)
fase_escalon = np.angle(fft_escalon)
fase_senoidal = np.angle(fft_senoidal)

#figuras juntas
fig2, ax2 =plt.subplots(1,3, figsize=(12,4))

#pulso
ax2[0].plot(frecuencias,magnitud_pulso)
ax2[0].set_title("FFT pulso")
ax2[0].set_xlabel("Frecuencia")
ax2[0].set_ylabel("Magnitud")
ax2[0].grid(True)

#Escalon
ax2[1].plot(frecuencias,magnitud_escalon)
ax2[1].set_title("FFT escalon")
ax2[1].set_xlabel("Frecuencia")
ax2[1].set_ylabel("Magnitud")
ax2[1].grid(True)

#Senoidal
ax2[2].plot(frecuencias,magnitud_senoidal)
ax2[2].set_title("FFT senoidal")
ax2[2].set_xlabel("Frecuencia")
ax2[2].set_ylabel("Magnitud")
ax2[2].grid(True)

#mostrar graficas
plt.tight_layout()
plt.show()

#Mostrar fases
fig3, ax3=plt.subplots(1,3, figsize=(12,4))

ax3[0].plot(frecuencias, fase_pulso)
ax3[0].set_title("Fase rectangular")
ax3[0].set_xlabel("Frecuencia")
ax3[0].set_ylabel("Fase")
ax3[0].grid(True)

ax3[1].plot(frecuencias, fase_escalon)
ax3[1].set_title("Fase escalon")
ax3[1].set_xlabel("Frecuencia")
ax3[1].set_ylabel("Fase")
ax3[1].grid(True)

ax3[2].plot(frecuencias,fase_senoidal)
ax3[2].set_title("Fase senoidal")
ax3[2].set_xlabel("Frecuencia")
ax3[2].set_ylabel("Fase")
ax3[2].grid(True)


#mostrar graficas
plt.tight_layout()
plt.show()
