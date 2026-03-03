import tkinter as tk
from PIL import Image, ImageTk 

def ventana_principal():
    global ven1
    ven1=tk.Tk()
    ven1.title("Esta es mi ventana principal")
    ven1.geometry("600x300")
    ven1.config(bg="lightblue")

    eti1=tk.Label(ven1,text="Reino Animal",bg="lightblue",font=("Arial",23,"bold"))
    eti1.pack()
    frame1= tk.Frame(ven1)
    frame1.pack(fill=tk.X, padx=10, pady=10)
    imagen = Image.open("D:\Ventana principal\Animales.jpg")
    imagen = imagen.resize((400, 200))  # Redimensionar si es necesario
    imagen_tk = ImageTk.PhotoImage(imagen) 
    label_imagen = tk.Label(frame1, image=imagen_tk)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)

    frame2=tk.Frame(frame1)
    frame2.grid(row=0, column=1, padx=5, pady=5)
    var=tk.IntVar()
    ele=tk.Radiobutton(frame2,text="Elefante",variable=var,value=1)
    ele.pack()
    jirafa=tk.Radiobutton(frame2,text="Jirafa",variable=var,value=2)
    jirafa.pack()
    castor=tk.Radiobutton(frame2,text="Castor",variable=var,value=3)
    castor.pack()
    leon=tk.Radiobutton(frame2,text="León",variable=var,value=4)
    leon.pack()

    def informacion():
        seleccion=var.get()
        if seleccion==1:
            ventana_elefante()
        elif seleccion == 2:
            ventana_jirafa()
        elif seleccion == 3:
            ventana_castor()
        elif seleccion == 4:
            ventana_leon()


    boton1=tk.Button(ven1,text="Ver info",command=informacion)
    boton1.pack()

    ven1.mainloop()

def regresar_a_primera(ventana_actual):
    ventana_actual.destroy()  # Cerrar la segunda ventana
    ventana_principal()  # Volver a abrir la ventana principal

def ventana_elefante():
    global ven2
    ven1.destroy()
    ven2=tk.Tk()
    ven2.title("Información del elefante")
    ven2.geometry("900x500")
    ven2.config(bg="lightblue")

    eti2=tk.Label(ven2,text="Elefante",bg="lightblue",font=("Algerian",24,"bold"))
    eti2.pack(pady=10)

    frame1= tk.Frame(ven2)
    frame1.pack(fill=tk.X, padx=10, pady=10)
    imagen = Image.open("d:\Ventana principal\elefante.jpg")
    imagen = imagen.resize((400, 200))  # Redimensionar si es necesario
    imagen_tk = ImageTk.PhotoImage(imagen) 
    label_imagen = tk.Label(frame1, image=imagen_tk)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)

    Texto1= tk.Label (frame1, text= "Los elefantes son los mamíferos terrestres más grandes del mundo, conocidos por su gran inteligencia, memoria, trompa multifuncional y estructura social compleja (matriarcados). Son herbívoros, consumen más de 200 kg de comida al día y habitan en África y Asia, enfrentando serias amenazas como la caza furtiva y pérdida de hábitat.", wraplength=250, justify="left")
    Texto1.grid(row=0, column=1, padx=5, pady=5)

    boton2=tk.Button(ven2,text="ir a ventana principak",command=lambda: regresar_a_primera(ven2) )
    boton2.pack(pady=30)

    ven2.mainloop()

def ventana_jirafa():
    global ven3
    ven1.destroy()
    ven3=tk.Tk()
    ven3.title("Información del jirafa")
    ven3.geometry("900x500")
    ven3.config(bg="lightblue")

    eti2=tk.Label(ven3,text="Jirafa",bg="lightblue",font=("Algerian",24,"bold"))
    eti2.pack(pady=10)

    frame1= tk.Frame(ven3)
    frame1.pack(fill=tk.X, padx=10, pady=10)
    imagen = Image.open("d:\Ventana principal\Jirafa.jpg")
    imagen = imagen.resize((400, 200))  # Redimensionar si es necesario
    imagen_tk = ImageTk.PhotoImage(imagen) 
    label_imagen = tk.Label(frame1, image=imagen_tk)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)

    Texto1= tk.Label (frame1, text= "La jirafa (Giraffa camelopardalis) es el mamífero terrestre más alto del mundo, alcanzando entre 4 y 6 metros de altura, nativa de las sabanas africanas. Se caracteriza por su cuello extremadamente largo, lengua prensil de hasta 45 cm y un pelaje moteado único. Son herbívoros, sociales, viven unos 25 años y están amenazadas por la pérdida de hábitat. ", wraplength=250, justify="left")
    Texto1.grid(row=0, column=1, padx=5, pady=5)

    boton2=tk.Button(ven3,text="ir a ventana principal",command=lambda: regresar_a_primera(ven3) )
    boton2.pack(pady=30)

    ven3.mainloop()

def ventana_castor():
    global ven4
    ven1.destroy()
    ven4=tk.Tk()
    ven4.title("Información del castor")
    ven4.geometry("900x500")
    ven4.config(bg="lightblue")

    eti2=tk.Label(ven4,text="Castor",bg="lightblue",font=("Algerian",24,"bold"))
    eti2.pack(pady=10)

    frame1= tk.Frame(ven4)
    frame1.pack(fill=tk.X, padx=10, pady=10)
    imagen = Image.open("d:\Ventana principal\castor.jpg")
    imagen = imagen.resize((400, 200))  # Redimensionar si es necesario
    imagen_tk = ImageTk.PhotoImage(imagen) 
    label_imagen = tk.Label(frame1, image=imagen_tk)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)

    Texto1= tk.Label (frame1, text="Los castores son roedores semiacuáticos, el segundo más grande del mundo tras el capibara, conocidos como ingenieros de la naturaleza por construir represas y madrigueras usando dientes afilados, ramas y lodo. Son nocturnos, herbívoros y cruciales para crear ecosistemas, aunque en zonas como Tierra del Fuego son considerados una plaga invasora", wraplength=250, justify="left")
    Texto1.grid(row=0, column=1, padx=5, pady=5)

    boton2=tk.Button(ven4,text="ir a ventana principal",command=lambda: regresar_a_primera(ven4) )
    boton2.pack(pady=30)

    ven4.mainloop()

def ventana_leon():
    global ven5
    ven1.destroy()
    ven5=tk.Tk()
    ven5.title("Información del leon")
    ven5.geometry("900x500")
    ven5.config(bg="lightblue")

    eti2=tk.Label(ven5,text="Leon",bg="lightblue",font=("Algerian",24,"bold"))
    eti2.pack(pady=10)

    frame1= tk.Frame(ven5)
    frame1.pack(fill=tk.X, padx=10, pady=10)
    imagen = Image.open("d:\Ventana principal\Leon.jpg")
    imagen = imagen.resize((400, 200))  # Redimensionar si es necesario
    imagen_tk = ImageTk.PhotoImage(imagen) 
    label_imagen = tk.Label(frame1, image=imagen_tk)
    label_imagen.grid(row=0, column=0, padx=5, pady=5)

    Texto1= tk.Label (frame1, text="El león (Panthera leo) es un mamífero carnívoro, el segundo félido más grande después del tigre, famoso por vivir en manadas sociales y habitar sabanas africanas y una pequeña zona en India. Los machos destacan por su imponente melena, pesan cerca de 190 kg y defienden el territorio, mientras que las hembras son las cazadoras principales, con un peso aproximado de 126 kg", wraplength=250, justify="left")
    Texto1.grid(row=0, column=1, padx=5, pady=5)

    boton2=tk.Button(ven5,text="ir a ventana principal",command=lambda: regresar_a_primera(ven5) )
    boton2.pack(pady=30)

    ven5.mainloop()

ventana_principal()