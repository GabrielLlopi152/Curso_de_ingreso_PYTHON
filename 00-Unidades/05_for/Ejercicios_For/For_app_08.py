import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Gabriel
apellido: Llopi
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = prompt(title= "Atención", prompt= "Ingrese un número")
        numero= int(numero)
        primos= ""
        contador_primos = 0

        for i in range(1, numero+1):
            es_primo= "si"
            for j in range(2, i):
                if i % j == 0:
                    es_primo = "no"
                    break

            if es_primo == "si":
                primos += "{0}, ".format(i)
                contador_primos += 1
        
        mensaje = "Los números primos son {0}. En total son {1}".format(primos, contador_primos)
        alert(title= "Atención", message= mensaje)
        
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()