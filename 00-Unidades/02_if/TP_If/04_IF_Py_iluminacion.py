import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Gabriel
apellido: Llopi
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
         lamparitas = int(self.combobox_cantidad.get())
         precio_lamp_num = lamparitas * 800
         precio_lamp_txt = str(precio_lamp_num)
         marca = self.combobox_marca.get()
        

         if(lamparitas >= 6 and lamparitas <= 12):
            precio_oferta_A_num = round(precio_lamp_num / 2)
            precio_oferta_A_txt = str(precio_oferta_A_num)
            if(precio_oferta_A_num >= 4000):
                importe_E = str(round(precio_oferta_A_num * 0.95))
                alert(title= "Atención", message= "El total es de $" + importe_E)
            else:
                alert(title= "Atención", message= "El total es de $" + precio_oferta_A_txt)


         elif(lamparitas == 5):
            if(marca == "ArgentinaLuz"):
                precio_oferta_1B = str(round(precio_lamp_num * 0.6))
                alert(title= "Atención", message= "El total es de $" + precio_oferta_1B)
            else:
                precio_oferta_2B = str(round(precio_lamp_num * 0.7))
                alert(title= "Atención", message= "El total es de $" + precio_oferta_2B)


         elif(lamparitas == 4):
            if(marca == "ArgentinaLuz" or marca == "FelipeLamparas"):
                precio_oferta_1C = str(round(precio_lamp_num * 0.75))
                alert(title= "Atención", message= "El total es de $" + precio_oferta_1C)
            else:
                precio_oferta_2C = str(round(precio_lamp_num * 0.8))
                alert(title= "Atención", message= "El total es de $" + precio_oferta_2C)


         elif(lamparitas == 3):
            if(marca == "ArgentinaLuz"):
                precio_oferta_1D = str(round(precio_lamp_num * 0.85))
                alert(title= "Atención", message= "El total es de $" + precio_oferta_1D)
            elif(marca == "FelipeLamparas"):
                precio_oferta_2D = str(round(precio_lamp_num * 0.9))
                alert(title= "Atención", message= "El total es de $" + precio_oferta_2D)
            else:
                precio_oferta_3D = str(round(precio_lamp_num * 0.95))
                alert(title= "Atención", message= "El total es de $" + precio_oferta_3D)


         else:
            alert(title= "Atención", message= "El total es de $" + precio_lamp_txt)
            

             

        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()