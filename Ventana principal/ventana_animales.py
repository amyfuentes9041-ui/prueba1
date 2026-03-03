import tkinter as tk
from PIL import Image, ImageTk

def abrir_seleccion():
    seleccion = var.get()
    if seleccion == 1:
        ventana_2()
    elif seleccion == 2:
        ventana_3()
    elif seleccion == 3:
        ventana_4()
    elif seleccion == 4:
        ventana_5()

def regresar_a_primera(ventana_actual):
    ventana_actual.destroy() #Cerrar la segunda ventana
    ventana_principal() #Volver a abrir la ventana principal

def ventana_principal():
    global vent1, var
    vent1 = tk.Tk()
    vent1.title("Reino Animal")
    vent1.geometry("600x450")
    vent1.config(bg="lightblue")

    etiq1=tk.Label(vent1, text="Reino Animal", 
        font=("Georgia", 20, "bold"), fg = "White", bg="skyblue", padx=10, pady=10)
    etiq1.grid(row = 0, column = 0, columnspan=2, padx = 15, pady=15)

    imagen = Image.open ("E:\Ventana principal\Animales.jpg")
    imagen = imagen.resize ((300, 200)) #Redimensionar si es necesario 
    imagen_tk = ImageTk.PhotoImage (imagen)
    label_imagen = tk.Label(vent1, image=imagen_tk)
    label_imagen.grid(row = 1, column = 0, rowspan=4, padx = 5, pady= 5)

    var = tk.IntVar(value=0)

    radiobutton1 = tk.Radiobutton(vent1, text="Jirafa", variable=var, value=1, bg="lightblue")
    radiobutton1.grid(row = 1, column = 1, sticky="w", padx = 5, pady= 5)

    radiobutton2 = tk.Radiobutton(vent1, text="Elefante", variable=var, value=2, bg="lightblue")
    radiobutton2.grid(row = 2, column = 1, sticky="w", padx = 5, pady= 5)

    radiobutton3 = tk.Radiobutton(vent1, text="León", variable=var, value=3, bg="lightblue")
    radiobutton3.grid(row = 3, column = 1, sticky="w", padx = 5, pady= 5)

    radiobutton4 = tk.Radiobutton(vent1, text="Castor", variable=var, value=4, bg="lightblue")
    radiobutton4.grid(row = 4, column = 1, sticky="w", padx = 5, pady= 5)

    boton = tk.Button(vent1, text="Ir a la opcion seleccionada", command=abrir_seleccion)
    boton.grid(row=5, column=0, columnspan=2, pady=20)

    vent1.mainloop()

def ventana_2 ():
    global vent2
    vent1.destroy()
    vent2 = tk.Tk()
    vent2.title("Jirafas")
    vent2.geometry("700x500")
    vent2.config(bg="lightblue")

    etiq2 = tk.Label(vent2, text="Las Jirafas", font=("Georgia", 18, "bold"), fg = "white", bg="skyblue")
    etiq2.grid(row=0, column=0, columnspan=2, pady=10)

    imagen = Image.open ("d:\Ventana principal\Jirafa.jpg")
    imagen = imagen.resize ((400, 300)) #Redimensionar si es necesario 
    imagen_tk = ImageTk.PhotoImage (imagen)
    label_imagen = tk.Label(vent2, image=imagen_tk)
    label_imagen.grid(row = 1, column = 1, padx = 5, pady= 5)

    Texto1= tk.Label (vent2, text= "La jirafa (Giraffa camelopardalis) es el mamífero terrestre más alto del mundo, alcanzando entre 4 y 6 metros de altura, nativa de las sabanas africanas. Se caracteriza por su cuello extremadamente largo, lengua prensil de hasta 45 cm y un pelaje moteado único. Son herbívoros, sociales, viven unos 25 años y están amenazadas por la pérdida de hábitat. ", wraplength=250, justify="left", font=("Ariel", 12, "bold"), fg = "black", bg="skyblue")
    Texto1.grid(row=1, column=2, padx=5, pady=5)

    boton2 = tk.Button(vent2, text="Regresar", command=lambda: regresar_a_primera(vent2), width=15)
    boton2.grid(row=2, column=0, columnspan=2, pady=30)

    vent2.mainloop()

def ventana_3 ():
    global vent3 
    vent1.destroy()
    vent3 = tk.Tk()
    vent3.title("Elefante")
    vent3.geometry("700x500")
    vent3.config(bg="lightblue")

    etiq3 = tk.Label(vent3, text="Los Elefantes", font=("Georgia", 18, "bold"), fg = "white", bg="skyblue")
    etiq3.grid(row=0, column=0, columnspan=2, pady=10)

    imagen = Image.open ("d:\Ventana principal\elefante.jpg")
    imagen = imagen.resize ((400, 300)) #Redimensionar si es necesario 
    imagen_tk = ImageTk.PhotoImage (imagen)
    label_imagen = tk.Label(vent3, image=imagen_tk)
    label_imagen.grid(row = 1, column = 1, padx = 5, pady= 5)

    Texto1= tk.Label (vent3, text= "Los elefantes son los mamíferos terrestres más grandes del mundo, conocidos por su gran inteligencia, memoria, trompa multifuncional y estructura social compleja (matriarcados). Son herbívoros, consumen más de 200 kg de comida al día y habitan en África y Asia, enfrentando serias amenazas como la caza furtiva y pérdida de hábitat.", wraplength=250, justify="left", font=("Ariel", 12, "bold"), fg = "black", bg="skyblue")
    Texto1.grid(row=1, column=2, padx=5, pady=5)

    boton3 = tk.Button(vent3, text="Regresar", command=lambda: regresar_a_primera(vent3), width=15)
    boton3.grid(row=2, column=1, padx= 30, pady=30)

    vent3.mainloop()

def ventana_4 ():
    global vent4, img4_tk
    vent1.destroy()
    vent4 = tk.Tk()
    vent4.title("León")
    vent4.geometry("700x500") 
    vent4.config(bg="lightblue")

    etiq4 = tk.Label(vent4, text="Los Leones", font=("Georgia", 18, "bold"), fg = "white", bg="skyblue")
    etiq4.grid(row=0, column=0, pady=10)

    imagen = Image.open("d:\Ventana principal\Leon.jpg")
    imagen = imagen.resize((400, 300)) 
    img4_tk = ImageTk.PhotoImage(imagen)
    label_imagen = tk.Label(vent4, image=img4_tk)
    label_imagen.grid(row=1, column=0, padx=10, pady=5)

    Texto1= tk.Label (vent4, text="El león (Panthera leo) es un mamífero carnívoro, el segundo félido más grande después del tigre, famoso por vivir en manadas sociales y habitar sabanas africanas y una pequeña zona en India. Los machos destacan por su imponente melena, pesan cerca de 190 kg y defienden el territorio, mientras que las hembras son las cazadoras principales, con un peso aproximado de 126 kg", wraplength=250, justify="left", font=("Ariel", 12, "bold"), fg = "black", bg="skyblue")
    Texto1.grid(row=1, column=1, padx=5, pady=5)

    boton4 = tk.Button(vent4, text="Regresar", command=lambda: regresar_a_primera(vent4), width=20)
    boton4.grid(row=2, column=0,  pady=30)

    vent4.mainloop()

def ventana_5 ():
    global vent5 
    vent1.destroy()
    vent5 = tk.Tk()
    vent5.title("Castor")
    vent5.geometry("700x500")
    vent5.config(bg="lightblue")

    etiq5 = tk.Label(vent5, text="Los Castores", font=("Georgia", 18, "bold"), fg = "white", bg="skyblue")
    etiq5.grid(row=0, column=0, columnspan=2, pady=10)

    imagen = Image.open ("d:\Ventana principal\castor.jpg")
    imagen = imagen.resize ((400, 300)) #Redimensionar si es necesario 
    imagen_tk = ImageTk.PhotoImage (imagen)
    label_imagen = tk.Label(vent5, image=imagen_tk)
    label_imagen.grid(row = 1, column = 1, padx = 5, pady= 5)

    Texto1= tk.Label (vent5, text="Los castores son roedores semiacuáticos, el segundo más grande del mundo tras el capibara, conocidos como ingenieros de la naturaleza por construir represas y madrigueras usando dientes afilados, ramas y lodo. Son nocturnos, herbívoros y cruciales para crear ecosistemas, aunque en zonas como Tierra del Fuego son considerados una plaga invasora", wraplength=250, justify="left", font=("Ariel", 12, "bold"), fg = "black", bg="skyblue")
    Texto1.grid(row=1, column=2, padx=5, pady=5)

    boton5 = tk.Button(vent5, text="Regresar", command=lambda: regresar_a_primera(vent5), width=20)
    boton5.grid(row=2, column=0, columnspan=2, pady=30)
    vent5.mainloop()

# Iniciar el bucle principal de la ventana
ventana_principal()