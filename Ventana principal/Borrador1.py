import tkinter as tk
from PIL import Image, ImageTk

def abrir_seleccion():
    seleccion = var.get()
    if seleccion == 0:
        return
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
        font=("Georgia", 20, "bold"), fg = "White", bg="lightpink", padx=10, pady=10)
    etiq1.grid(row = 0, column = 0, columnspan=2, padx = 15, pady=15)

    imagen = Image.open ("D:\Ventana principal\Animales.jpg")
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
    vent2.geometry("900x500")
    vent2.config(bg="lightblue")

    etiq2 = tk.Label(vent2, text="Las Jirafas", font=("Georgia", 18, "bold"), bg="lightpink")
    etiq2.grid(row=0, column=0, columnspan=2, pady=10)

    imagen = Image.open ("D:\Ventana principal\Jirafa.jpg")
    imagen = imagen.resize ((400, 300)) #Redimensionar si es necesario 
    imagen_tk = ImageTk.PhotoImage (imagen)
    label_imagen = tk.Label(vent2, image=imagen_tk)
    label_imagen.grid(row = 1, column = 1, padx = 5, pady= 5)

    imagen2 = Image.open ("D:\Ventana principal\Informacion Jirafa.jpg")
    imagen2 = imagen2.resize ((400, 300)) #Redimensionar si es necesario 
    imagen2_tk = ImageTk.PhotoImage (imagen2)
    label_imagen2 = tk.Label(vent2, image=imagen2_tk)
    label_imagen2.grid(row = 1, column = 2, padx = 5, pady= 5)

    boton2 = tk.Button(vent2, text="Regresar", command=lambda: regresar_a_primera(vent2), width=15)
    boton2.grid(row=2, column=0, columnspan=2, pady=30)

    vent2.mainloop()

def ventana_3 ():
    global vent3 
    vent1.destroy()
    vent3 = tk.Tk()
    vent3.title("Elefante")
    vent3.geometry("900x500")
    vent3.config(bg="lightblue")

    etiq3 = tk.Label(vent3, text="Los Elefantes", font=("Georgia", 18, "bold"), bg="lightpink")
    etiq3.grid(row=0, column=0, columnspan=2, pady=10)

    imagen = Image.open ("D:\Ventana principal\elefante.jpg")
    imagen = imagen.resize ((400, 300)) #Redimensionar si es necesario 
    imagen_tk = ImageTk.PhotoImage (imagen)
    label_imagen = tk.Label(vent3, image=imagen_tk)
    label_imagen.grid(row = 1, column = 1, padx = 5, pady= 5)

    imagen3 = Image.open ("Elefanteinformacion.jpg")
    imagen3 = imagen3.resize ((400, 300)) #Redimensionar si es necesario 
    imagen3_tk = ImageTk.PhotoImage (imagen3)
    label_imagen3 = tk.Label(vent3, image=imagen3_tk)
    label_imagen3.grid(row = 1, column = 2, padx = 5, pady= 5)

    boton3 = tk.Button(vent3, text="Regresar", command=lambda: regresar_a_primera(vent3), width=15)
    boton3.grid(row=2, column=1, padx= 30, pady=30)

    vent3.mainloop()

def ventana_4 ():
    global vent4, img4_tk
    vent1.destroy()
    vent4 = tk.Tk()
    vent4.title("León")
    vent4.geometry("900x500") 
    vent4.config(bg="lightblue")

    etiq4 = tk.Label(vent4, text="Los Leones", font=("Georgia", 18, "bold"), bg="lightpink")
    etiq4.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

    imagen = Image.open("Leon.jpg")
    imagen = imagen.resize((400, 250)) 
    img4_tk = ImageTk.PhotoImage(imagen)
    label_imagen = tk.Label(vent4, image=img4_tk)
    label_imagen.grid(row=1, column=0, padx=10, pady=5)

    imagen4 = Image.open("Leon.jpg") 
    imagen4 = imagen4.resize((400, 250)) 
    img4_info_tk = ImageTk.PhotoImage(imagen4)
    label_imagen2 = tk.Label(vent4, image=img4_info_tk)
    label_imagen2.grid(row=1, column=1, padx=10, pady=5)

    boton4 = tk.Button(vent4, text="Regresar", command=lambda: regresar_a_primera(vent4), width=20)
    boton4.grid(row=2, column=0, columnspan=2, pady=30)

    vent4.mainloop()

def ventana_5 ():
    global vent5 
    vent1.destroy()
    vent5 = tk.Tk()
    vent5.title("Castor")
    vent5.geometry("900x500")
    vent5.config(bg="lightblue")

    etiq5 = tk.Label(vent5, text="Los Castores", font=("Georgia", 18, "bold"), bg="lightpink")
    etiq5.grid(row=0, column=0, columnspan=2, pady=10)

    imagen = Image.open ("castor.jpg")
    imagen = imagen.resize ((400, 300)) #Redimensionar si es necesario 
    imagen_tk = ImageTk.PhotoImage (imagen)
    label_imagen = tk.Label(vent5, image=imagen_tk)
    label_imagen.grid(row = 1, column = 1, padx = 5, pady= 5)

    imagen5 = Image.open ("Castorinformacion.jpg")
    imagen5 = imagen5.resize ((400, 300)) #Redimensionar si es necesario 
    imagen5_tk = ImageTk.PhotoImage (imagen5)
    label_imagen5 = tk.Label(vent5, image=imagen5_tk)
    label_imagen5.grid(row = 1, column = 2, padx = 5, pady= 5)

    boton5 = tk.Button(vent5, text="Regresar", command=lambda: regresar_a_primera(vent5), width=20)
    boton5.grid(row=2, column=0, columnspan=2, pady=30)
    vent5.mainloop()


# Iniciar el bucle principal de la ventana
ventana_principal()