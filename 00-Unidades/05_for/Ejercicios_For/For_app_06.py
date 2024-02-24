import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Gabriel
apellido: Llopi
---
Ejercicio: for_06
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = prompt(title="Atención", prompt= "Ingrese un número")
        numero= int(numero)
        divisores = ""
        cantidad_divisores= 0

        for i in range(1, numero+1, 1):
            if numero % i == 0:
                divisores += "{0}, ".format(i)
                cantidad_divisores += 1

        mensaje= "Los divisores del número {0}, son {1}. En total son {2}.".format(numero, divisores, cantidad_divisores)
        alert(title="Atención", message= mensaje)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()