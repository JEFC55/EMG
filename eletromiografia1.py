#falta(zoom de eixo)
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#from matplotlib.widgets import Cursor, Button
from matplotlib.widgets import Slider
from matplotlib.widgets import RadioButtons

x =pd.read_excel(r'C:\Users\royal\Desktop\iniciacao_cientifica\Target 51.xlsx')
fig,varx=plt.subplots(1,2,sharex=False,figsize=(9,6),facecolor="LightSteelBlue")


#def set_visible(nome_linha):#caixa
#    opcao=labels.index(nome_linha)#caixa
#   for indx, val in enumerate(armazenadata):#caixa
#        if indx ==opcao:#caixa
#            armazenadata[i].set_visible(True)#caixa
#        else:#caixa
#                       armazenadata[i].set_visible(False)#caixa
#        plt.draw()#caixa

dedo1=x['R TRAPEZIUS MIDDLE FIBERS [V]']
dedo2=x['R ANTERIOR DELTOID  [V]']
dedo3=x['R MEDIAL DELTOID [V]']
dedo4=x['R POSTERIOR DELTOID [V]']
dedo5=x['R PECTORALIS MAJOR [V]']
dedo6=x['R INFRASPINATIS [V]']
dedo7=x['R BICEPS BRACHII [V]']
dedo8=x['R TRICEPS BRACHII [V]']
tempo=x['TIME ANALISYS [s]']
armazenadata=[dedo1,dedo2,dedo3,dedo4,dedo5,dedo6,dedo7,dedo8]

varx[0].plot(tempo,dedo1, label="R TRAPEZIUS MIDDLE FIBERS [V]",color="#00FF7F")
varx[1].plot(tempo,dedo1,color="red")
#varx[0].scatter(tempo,dedo1, label="R TRAPEZIUS MIDDLE FIBERS [V]",color="#00FF7F")
#varx[1].scatter(tempo,dedo1,color="red",s=5)
#deixou bonito só quando está ampliado ;-;

#varx.plot(tempo,dedo2, label="R ANTERIOR DELTOID  [V]")
#varx.plot(tempo,dedo4, label="R POSTERIOR DELTOID [V]")
#varx.plot(tempo,dedo5, label="R PECTORALIS MAJOR [V]")
#varx.plot(tempo,dedo6, label="R INFRASPINATIS [V]")
#varx.plot(tempo,dedo7, label="R BICEPS BRACHII [V]")
#varx.plot(tempo,dedo8, label="R TRICEPS BRACHII [V]")

#plt.subplots_adjust(left=0.25)#caixa

#labels=('[V] R TRAPEZIUS MIDDLE FIBERS','[V]R ANTERIOR DELTOID','[V] R MEDIAL DELTOID','[V] R POSTERIOR DELTOID','[V] R PECTORALIS MAJOR','[V]	R INFRASPINATIS',' [V]	R BICEPS BRACHII',' [V]	R TRICEPS BRACHII')
#varx_caixa = plt.axes([0.01,0.5,0.2,0.4])#caixa
#verifique_estado=(True,False,False,False,False,False,False,False)#caixa
#varx_botoes=RadioButtons(varx_caixa,labels)#caixa

#cursor= Cursor(varx,#cursor
#                vertOn=True,#cursor
#                horizOn=True,#cursor
#                color="red",#cursor
#                linewidth=2.0)#cursor
def onclick(event):#cursor
    x1, y1=event.xdata,event.ydata#cursor
    print(x1,y1)#cursor
fig.canvas.mpl_connect("button_press_event", onclick)#cursor

varx[0].set_title(dedo1.name)
varx[0].set_xlabel("Segundos[s]")
varx[0].set_ylabel("Volts[V]")
varx[1].set_title(dedo1.name+" (ampliado)")
varx[1].set_xlabel("Segundos[s]")
varx[1].set_ylabel("Volts[V]")

plt.subplots_adjust(bottom=0.25)#slider
varx_slider=plt.axes([0.1,0.1,0.8,0.04],facecolor="black")#slider
vary_slider=plt.axes([0.1,0.05,0.8,0.04],facecolor="black")#slider

def update_line(indx):#slider
    varx[0].clear()#slider
    varx[0].plot(tempo,armazenadata[indx-1],label=armazenadata[indx-1].name,color="#00FF7F")#slider
    varx[0].set_title(armazenadata[indx-1].name)#slider
    #slider
    varx[1].clear()#slider
    varx[1].plot(tempo,armazenadata[indx-1],label=armazenadata[indx-1].name,color="red")#slider
    varx[1].set_title(armazenadata[indx-1].name+" (ampliado)")#slider
    #slider
    
    varx[0].set_xlabel("Segundos[s]")
    varx[0].set_ylabel("Volts[V]")

    varx[1].set_xlabel("Segundos[s]")
    varx[1].set_ylabel("Volts[V]")

    plt.draw()#slider
    varx[0].set_ylim(-350, 401)  # Define o limite do eixo y
    varx[1].set_ylim(-350, 401)  # Define o limite do eixo y
    varx[1].set_xlim(0, (2595115/2))
    slidertamanho.reset()

def update_size(tamanho):
#tamanho vai ser a variavel puxada pelo slider e este irá executar altomaticamente o código e filtra-lo entre 20000 no gráfico de x
    slidermax=tamanho+(2595115/2)
    varx[1].set_xlim(tamanho,slidermax)

slider=Slider(varx_slider,"Category",valmin=1 , valmax=8 , valinit=1 , valstep=1)#slider
print(slider)
slider.on_changed(update_line)#slider

slidertamanho=Slider(vary_slider,"tempo(µs)",valmin=0 , valmax=(56443500-(2595115/2)) , valinit=1 , valstep=(2595115/2))#slider
print(slidertamanho)
slidertamanho.on_changed(update_size)#slider

varx[0].set_ylim(-350, 401)  # Define o limite do eixo y
varx[1].set_ylim(-350, 401)  # Define o limite do eixo y
varx[1].set_xlim(0, (2595115/2))
#varx.legend()#legendas
plt.show()#mostre as tabelas