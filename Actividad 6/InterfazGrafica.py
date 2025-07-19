class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.id},{self.nombre},{self.precio},{self.cantidad}"

import os

ARCHIVO = "productos.txt"

def crear_producto(producto):
    with open(ARCHIVO, "a") as file:
        file.write(str(producto) + "\n")

def leer_productos():
    productos = []
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as file:
            for linea in file:
                id, nombre, precio, cantidad = linea.strip().split(",")
                productos.append(Producto(id, nombre, float(precio), int(cantidad)))
    return productos

def actualizar_producto(producto_actualizado):
    productos = leer_productos()
    with open(ARCHIVO, "w") as file:
        for producto in productos:
            if producto.id == producto_actualizado.id:
                file.write(str(producto_actualizado) + "\n")
            else:
                file.write(str(producto) + "\n")

def eliminar_producto(id_a_eliminar):
    productos = leer_productos()
    with open(ARCHIVO, "w") as file:
        for producto in productos:
            if producto.id != id_a_eliminar:
                file.write(str(producto) + "\n")

import tkinter as tk
from tkinter import messagebox

# Ventana principal
ventana = tk.Tk()
ventana.title("Inventario de Productos")
ventana.geometry("500x500")

# Etiquetas y entradas
tk.Label(ventana, text="ID").pack()
entrada_id = tk.Entry(ventana)
entrada_id.pack()

tk.Label(ventana, text="Nombre").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(ventana, text="Precio").pack()
entrada_precio = tk.Entry(ventana)
entrada_precio.pack()

tk.Label(ventana, text="Cantidad").pack()
entrada_cantidad = tk.Entry(ventana)
entrada_cantidad.pack()

# Área de salida
salida = tk.Text(ventana, height=10)
salida.pack(pady=10)

# Funciones para botones
def crear():
    try:
        producto = Producto(
            entrada_id.get(),
            entrada_nombre.get(),
            float(entrada_precio.get()),
            int(entrada_cantidad.get())
        )
        crear_producto(producto)
        messagebox.showinfo("Éxito", "Producto creado.")
        limpiar()
    except:
        messagebox.showerror("Error", "Datos inválidos.")

def leer():
    salida.delete("1.0", tk.END)
    productos = leer_productos()
    for p in productos:
        salida.insert(tk.END, f"{p.id} | {p.nombre} | ${p.precio} | {p.cantidad} unidades\n")

def actualizar():
    try:
        producto = Producto(
            entrada_id.get(),
            entrada_nombre.get(),
            float(entrada_precio.get()),
            int(entrada_cantidad.get())
        )
        actualizar_producto(producto)
        messagebox.showinfo("Éxito", "Producto actualizado.")
        limpiar()
    except:
        messagebox.showerror("Error", "Datos inválidos.")

def eliminar():
    id_ = entrada_id.get()
    if id_:
        eliminar_producto(id_)
        messagebox.showinfo("Éxito", "Producto eliminado.")
        limpiar()
    else:
        messagebox.showerror("Error", "Debes ingresar un ID.")

def limpiar():
    entrada_id.delete(0, tk.END)
    entrada_nombre.delete(0, tk.END)
    entrada_precio.delete(0, tk.END)
    entrada_cantidad.delete(0, tk.END)
    leer()

# Botones
tk.Button(ventana, text="Crear", command=crear).pack(pady=2)
tk.Button(ventana, text="Leer", command=leer).pack(pady=2)
tk.Button(ventana, text="Actualizar", command=actualizar).pack(pady=2)
tk.Button(ventana, text="Eliminar", command=eliminar).pack(pady=2)

ventana.mainloop()
