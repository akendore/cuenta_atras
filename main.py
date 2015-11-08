__author__ = 'Daniel'

#Librerias y Módulos
from tkinter import *
from time import *
from tkinter.messagebox import *

#Funciones
def mostrar(v): v.deiconify()
def ocultar(v): v.withdraw()
def ejecutar(f): v0.after(200,f)
def m_error(Titulo,mensaje): showerror(Titulo,mensaje)

def cuentaatras(m,s):

    try:
         #h = int(h.get())
         m = int(m.get())
         s = int(s.get())
         s+=m*60
         for t in range(s, -1, -1):
            sf = "{:02d}:{:02d}".format(*divmod(t, 60))
            count.set(sf)
            v1a.update()
            sleep(1)
    except ValueError:
        v1a.withdraw()
        showerror("Rellena todos los campos","Rellena los campos con 0 para que sean invalidos")

def cronometrar():
    x=True
    s=0
    while(x==True):
            sf1 = "{:02d}:{:02d}".format(*divmod(s, 60))
            cron.set(sf1)
            v2.update()
            s+=1
            sleep(1)

#Ventana app
v0 = Tk()
v0.title("Cuenta atrás / Cronómetro")
v0.resizable(0,0)
f0 = Frame(v0)
f0.grid(column=0,row=0,padx=(10,10),pady=(10,10))

#ventana cuenta atrás
v1=Toplevel(v0)
v1.title("Cuenta atrás")
v1.withdraw()
v1.resizable(0,0)
f1=Frame(v1)
f1.grid(column=0,row=0,padx=(10,10),pady=(10,10))

#ventana cuenta atrás 2
v1a=Toplevel(v0)
v1a.title = v1.title
v1a.resizable(0,0)
v1a.withdraw()

#ventana cronómetro
v2 = Toplevel(v0)
v2.title("Cronómetro")
v2.resizable(0,0)
v2.withdraw()

#Elementos app
    #Labels
LEnApp = Label(f0,text="Selecciona una de las dos opciones:").grid(column=0,row=0,columnspan=2,pady=(0,5))#Instrucción vapp

    #Botones
Bcuenta = Button(f0,text="Cuenta atrás",command=lambda:ejecutar(mostrar(v1))).grid(column=0,row=1,padx=(10,10),sticky=E)
Bcrono = Button(f0,text="Cronómetro",command=lambda: ejecutar(mostrar(v2))).grid(column=1,row=1,sticky=W)

#Elementos Cuenta atrás
    #Labels
LEnCA = Label(f1,text="Introduce el tiempo que quieras contar.").grid(column=1,row=1,columnspan=2,pady=(0,5))
#Lh1 = Label(f1,text="Horas:").grid(column=1,row=2)
Lm1 = Label(f1,text="Minutos:").grid(column=1,row=2)
Ls1 = Label(f1,text="Segundos:").grid(column=2,row=2)

    #Entradas
#Eh = StringVar()
#Ehoras = Entry(f1,width=5,textvar=Eh).grid(column=1,row=3)
Em = StringVar()
Eminutos = Entry(f1,width=5,textvar=Em).grid(column=1,row=3)
Es = StringVar()
Esegundos = Entry(f1,width=5,textvar=Es).grid(column=2,row=3)
x=False

    #Botones
Bstart1 = Button(f1,text="Start",command=lambda:ejecutar(mostrar(v1a)or (cuentaatras(Em,Es)))).grid(column=4,row=3)
Bcerrar1= Button(f1,text="Cerrar",command=lambda:ejecutar(ocultar(v1))).grid(column=2,row=4)

#Elementos Cuenta atrás 2
    #Labels
count = StringVar()
label_font = ('helvetica', 40)
Label(v1a, textvariable=count, font=label_font,fg='blue', bd=3).grid(column=1,row=2)

    #Botones
Bparar = Button(v1a,text="Parar",command=()).grid(column=4,row=2)
Bcerrar1= Button(v1a,text="Cerrar",command=lambda:ejecutar(ocultar(v1a))).grid(column=2,row=3)

#Elementos cronómetro
    #Labels
        #Label enunciado
LEnCr = Label(v2,text="Pulsa en start para empezar a cronometrar").grid(column=1,row=1)

        #Labels contador
cron = StringVar()

label_font = ('helvetica', 40)
Label(v2, textvariable=cron, font=label_font, bg='white',
         fg='blue', relief='raised', bd=3).grid(column=1,row=2)

    #Botones
Bstart2 = Button(v2,text="Start",command=lambda: ejecutar(cronometrar())).grid(column=2,row=2)
Bcerrar2 = Button(v2,text="Cerrar",command=lambda: ejecutar(ocultar(v2))).grid(column=1,row=3)

v0.mainloop()
