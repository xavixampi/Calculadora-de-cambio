from tkinter import *

#Crear ventana
ventana=Tk()
ventana.geometry('500x400')
ventana.title('Cambio')
ventana.configure(bg='black')

#Funcion para restar los dos valores: Importe recibido - Precio
def Resta():
    Resta=float(Entry2.get())-float(Entry1.get())
    return var.set(Resta)

var=StringVar()

#Label y entrada de texto para el precio
Label1=Label(ventana,text='Precio:',bg='White',fg='black')
Label1.place(x=20,y=75,width=120,height=60)

Entry1=Entry(ventana)
Entry1.place(x=145,y=75,width=180,height=60)

#Label y entrada de texto para el importe recibido
Label2=Label(ventana,text='Importe recibido',bg='white',fg='black')
Label2.place(x=20,y=150,width=120,height=60)

Entry2=Entry(ventana)
Entry2.place(x=145,y=150,width=180,height=60)

#Label para el cambio
Label3=Label(ventana,text='Cambio',bg='white',fg='black')
Label3.place(x=20,y=225,width=120,height=60)

#Label para mostrar por pantala el valor del cambio
Label4=Label(ventana,textvariable=var,bg='white',fg='black')
Label4.place(x=145,y=225,width=180,height=60)

#Boton para enviar los datos del precio y del importe recibido
boton1=Button(ventana,text='Confirmar',bg='lime',fg='black',command=Resta)
boton1.place(x=335,y=150,width=120,height=60)

ventana.mainloop()