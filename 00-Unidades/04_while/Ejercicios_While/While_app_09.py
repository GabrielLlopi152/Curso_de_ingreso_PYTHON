import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Gabriel
apellido: Llopi
---
Ejercicio: while_09
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera 
hasta que presione el botón Cancelar (en el prompt). 
Luego determinar el máximo y el mínimo 
e informarlos en los cuadros de textos txt_maximo y txt_minimo respectivamente

'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.txt_minimo = customtkinter.CTkEntry(
            master=self, placeholder_text="Mínimo")
        self.txt_minimo.grid(row=0, padx=20, pady=20)

        self.txt_maximo = customtkinter.CTkEntry(
            master=self, placeholder_text="Máximo")
        self.txt_maximo.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20,
                              columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
         numero_a = prompt(title= "Atención", prompt= "Introduzca un número")
         numero_a = int(numero_a)

         maximo = numero_a
         minimo = numero_a

         while (True):
            numero_b = prompt(title= "Atención", prompt= "Introduzca un número")
            if (numero_b == None):
                break
            numero_b = int(numero_b)
           
            if(numero_b >= numero_a):
                maximo = numero_b
            if(numero_b <= numero_a):
                minimo = numero_b

            numero_a = numero_b
        
         maximo = str(maximo)
         minimo = str(minimo)
         self.txt_maximo.insert(0, maximo)
         self.txt_minimo.insert(0, minimo)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
