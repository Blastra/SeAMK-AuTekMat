import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import *



fig1 = plt.figure()

#Määritellään tyhjät pohjakuviot
line1, = plt.plot([],[],'r-')
line2, = plt.plot([],[],'r-')
line3, = plt.plot([],[],'r-')

puoliVäliKuvio, = plt.plot([],[])

#Loppukäyrien piirtämistä varten varattu lista
plottiLista = [[],[]]
puoliVäliLista = [[],[]]

#Määritellään animaatioaskeleen tilanne
def update_line(i, fig1, line1, line2, line3):

    global plottiListaBool
    
    ADPituus = 1
    DCPituus = 4
    CBPituus = 4
    
    alfaKulma = i*2*pi/360
    DPiste = [cos(alfaKulma)*ADPituus,sin(alfaKulma)*ADPituus]

    BPiste = [3,0]

    DBPituus = sqrt((DPiste[0]-BPiste[0])**2+(DPiste[1]-BPiste[0])**2)

    #Betakulma, B-pisteestä vasemmalle avautuva    

    beta1Kulma = asin(sin(alfaKulma)/DBPituus)
    beta2Kulma = acos((-4**2+DBPituus**2+4**2)/(2*DBPituus*4))

    betaTotalKulma = pi-(beta1Kulma+beta2Kulma)

    CPiste = [CBPituus*cos(betaTotalKulma)+BPiste[0],BPiste[1]+CBPituus*sin(betaTotalKulma)]
    
    line1xPoints = [0,DPiste[0]]
    line1yPoints = [0,DPiste[1]]
    line1.set_xdata(line1xPoints)
    line1.set_ydata(line1yPoints)

    
    line2xPoints = [DPiste[0],CPiste[0]]
    line2yPoints = [DPiste[1],CPiste[1]]
    line2.set_xdata(line2xPoints)
    line2.set_ydata(line2yPoints)

    
    line3xPoints = [CPiste[0],3]
    line3yPoints = [CPiste[1],0]
    line3.set_xdata(line3xPoints)
    line3.set_ydata(line3yPoints)

    rataPiste = [(CPiste[0]+DPiste[0])/2,(CPiste[1]+DPiste[1])/2]

    if len(plottiLista[0]) < 361:
        plottiLista[1].append(180-betaTotalKulma/2/pi*360)
        plottiLista[0].append(alfaKulma/2/pi*360)
        puoliVäliLista[0].append(rataPiste[0])
        puoliVäliLista[1].append(rataPiste[1])
        puoliVäliKuvio.set_data(puoliVäliLista[0],puoliVäliLista[1])
        
        

    if len(plottiLista[0]) == 361 and plottiListaBool == False:
        
        plt.figure(2)
        plt.plot(plottiLista[0],plottiLista[1])        
        plottiListaBool = True
        plt.xlim(0, 360)
        plt.ylim(35, 90)
        plt.xlabel('alfaKulma')
        plt.ylabel('betakulma')
        plt.show()
    
    return line1,line2,line3

#Plotin käynnistysboolean
plottiListaBool = False

plt.xlim(-2, 6)
plt.ylim(-1.5, 4)
plt.xlabel('x')
plt.title('test')

line_ani = animation.FuncAnimation(fig1, update_line, fargs=(fig1, line1,line2,line3),interval=25, blit=False)


plt.show()
