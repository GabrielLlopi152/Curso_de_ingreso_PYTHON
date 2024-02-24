import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
nombre: Gabriel
apellido: Llopi
---
Ejercicio: for_09
---
Enunciado:
Al comenzar el juego generamos un número secreto del 1 al 100, se pedira al usuario el ingreso de un numero por prompt y si el número ingresado es el mismo que el número secreto se dará por terminado el juego con un mensaje similar a este: 

En esta oportunidad el juego evaluará tus aptitudes a partir de la cantidad de intentos, por lo cual se informará lo siguiente:
    1° intento: “Usted es un psíquico”.
	2° intento: “Excelente percepción”.
	3° intento: “Esto es suerte”.
	4° hasta 6° intento: “Excelente técnica”.
	7 intentos: “Perdiste, suerte para la próxima”.

de no ser igual se debe informar si 
“Falta…”  para llegar al número secreto  o si 
“Se pasó…”  del número secreto.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_secreto = random.randint(1, 100)
        #print(numero_secreto)
        intento = 0

        for i in range(1, 7):
            intento += 1
            numero_jugador = prompt(title= "Atención", prompt= "Ingrese un número entre el 1 al 100")
            titulo = "Perdiste"
            mensaje = "Lo siento, suerte la próxima vez."

            if numero_secreto == int(numero_jugador):
                match(intento):
                    case 1:
                        titulo = "¡Sorprendente!"
                        mensaje = "Usted es todo un psíquico."
                    case 2:
                        titulo = "Increíble"
                        mensaje = "Excelente percepción."
                    case 3:
                        titulo = "Muy bien"
                        mensaje = "Esto es suerte."
                    case 4 | 5 | 6:
                        titulo = "Felicidades"
                        mensaje = "Excelente técnica."
                break

            else:
                if numero_secreto > int(numero_jugador):
                    alert(title= "¡Casi!", message= "Fallo, el número secreto es mayor al ingresado.")
                else:
                    alert(title= "¡Casi!", message= "Fallo, el número secreto es menor al ingresado.")
                
        mensaje_final =  "{0} El número secreto era: {1}".format(mensaje, numero_secreto)
        
        alert(title= titulo , message= mensaje_final)       



                

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()