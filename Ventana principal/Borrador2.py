import tkinter as tk
from PIL import Image, ImageTk

def abrir_seleccion():
    seleccion = var.get()
    if seleccion == 0:
        return # No hace nada si no hay selección
    
    # IMPORTANTE: No destruyas vent1 aquí si lo vas a hacer dentro de cada función,
    # o asegúrate de que la lógica sea consistente. 
    # Lo mejor es destruirla justo antes de crear la nueva.
    if seleccion == 1:
        ventana_2()
    elif seleccion == 2:
        ventana_3()
    elif seleccion == 3:
        ventana_4()
    elif seleccion == 4:
        ventana_5()

def regresar_a_primera(ventana_actual):
    ventana_actual.destroy()
    ventana_principal()

def ventana_principal():
    global vent1, var, imagen_tk_principal # Mantenemos viva la imagen principal
    vent1 = tk.Tk()
    vent1.title("Reino Animal")
    vent1.geometry("600x450")
    vent1.config(bg="lightblue")

    # Título
    etiq1 = tk.Label(vent1, text="Reino Animal", 
                     font=("Georgia", 20, "bold"), fg="White", bg="lightpink", padx=10, pady=10)
    etiq1.grid(row=0, column=0, columnspan=2, padx=15, pady=15)

    # Imagen Principal
    try:
        img_p = Image.open("Animales.jpg").resize((300, 200))
        imagen_tk_principal = ImageTk.PhotoImage(img_p)
        tk.Label(vent1, image=imagen_tk_principal).grid(row=1, column=0, rowspan=4, padx=5, pady=5)
    except:
        tk.Label(vent1, text="Imagen no encontrada").grid(row=1, column=0, rowspan=4)

    var = tk.IntVar(value=0)

    # Radiobuttons
    tk.Radiobutton(vent1, text="Jirafa", variable=var, value=1, bg="lightblue").grid(row=1, column=1, sticky="w")
    tk.Radiobutton(vent1, text="Elefante", variable=var, value=2, bg="lightblue").grid(row=2, column=1, sticky="w")
    tk.Radiobutton(vent1, text="León", variable=var, value=3, bg="lightblue").grid(row=3, column=1, sticky="w")
    tk.Radiobutton(vent1, text="Castor", variable=var, value=4, bg="lightblue").grid(row=4, column=1, sticky="w")

    # Botón Cuadrado
    boton = tk.Button(vent1, text="Ir a la opción seleccionada", command=abrir_seleccion)
    boton.grid(row=5, column=0, columnspan=2, pady=20)

    vent1.mainloop()

# --- FUNCIONES DE VENTANAS (CORREGIDAS) ---

def ventana_2():
    global vent2, img_j1, img_j2 # Globales para que no desaparezcan
    vent1.destroy() # Cerramos la principal
    vent2 = tk.Tk()
    vent2.title("Jirafa")
    vent2.geometry("500x600")
    vent2.config(bg="lightblue")

    # ERROR CORREGIDO: Usamos vent2 en lugar de vent1
    tk.Label(vent2, text="Jirafa", font=("Arial", 18), bg="lightblue").pack(pady=10)

    try:
        img_j1 = ImageTk.PhotoImage(Image.open("Jirafa.jpg").resize((400, 200)))
        tk.Label(vent2, image=img_j1).pack(pady=5)
        
        img_j2 = ImageTk.PhotoImage(Image.open("Informacion Jirafa.jpg").resize((400, 200)))
        tk.Label(vent2, image=img_j2).pack(pady=5)
    except:
        tk.Label(vent2, text="Error al cargar imágenes").pack()

    tk.Button(vent2, text="Regresar", command=lambda: regresar_a_primera(vent2)).pack(pady=20)
    vent2.mainloop()

def ventana_3():
    global vent3, img_e1, img_e2
    vent1.destroy()
    vent3 = tk.Tk()
    vent3.title("Elefante")
    vent3.geometry("500x600")
    vent3.config(bg="lightblue")
    
    tk.Label(vent3, text="Elefante", font=("Arial", 18), bg="lightblue").pack(pady=10)
    
    try:
        img_e1 = ImageTk.PhotoImage(Image.open("elefante.jpg").resize((400, 200)))
        tk.Label(vent3, image=img_e1).pack(pady=5)
        
        img_e2 = ImageTk.PhotoImage(Image.open("Elefante informacion.jpg").resize((400, 200)))
        tk.Label(vent3, image=img_e2).pack(pady=5)
    except:
        tk.Label(vent3, text="Error al cargar imágenes").pack()

    tk.Button(vent3, text="Regresar", command=lambda: regresar_a_primera(vent3)).pack(pady=20)
    vent3.mainloop()

# NOTA: Debes aplicar la misma lógica (cambiar vent1 por vent4/vent5) 
# en las funciones de León y Castor.

ventana_principal()
