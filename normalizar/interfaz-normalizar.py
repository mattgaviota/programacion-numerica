#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
from tkMessageBox import showinfo
import normalizar as nm

class Main_app:

    def __init__(self, master):
        
        self.main_frame = tk.Frame(master, bg='#c8c8c8')
        self.main_frame.grid(ipadx=2, ipady=2, padx=2, pady=2)
        self.numero = tk.StringVar()
        self.base = tk.StringVar()
        self.convert = tk.StringVar()
        self.flotante = tk.StringVar()
        self.normalized_simetria = tk.StringVar()
        self.normalized_corte = tk.StringVar()
        self.mantisa = tk.StringVar()
        
        ######CAJAS DE ENTRADA CON SUS CARTELES######
        '''Etiqueta del número'''
        self.num_label = tk.Label(self.main_frame, text="Número", bg='#c8c8c8')
        self.num_label.grid(row=1, column=1, sticky=tk.W)
        
        '''Caja de entrada del número'''
        self.ent_numero = tk.Entry(self.main_frame, width=10, 
            textvariable=self.numero, bd=2, relief=tk.GROOVE)
        self.ent_numero.grid(row=1, column=2, sticky=tk.W + tk.E)
        self.ent_numero.focus_set()
        
        '''Etiqueta de la base'''
        self.base_label = tk.Label(self.main_frame, text="Base", bg='#c8c8c8')
        self.base_label.grid(row=2, column=1, sticky=tk.W)
        
        '''Caja de entrada de la base'''
        self.ent_base = tk.Entry(self.main_frame, width=10, 
            textvariable=self.base, bd=2, relief=tk.GROOVE)
        self.ent_base.grid(row=2, column=2, sticky=tk.W + tk.E)
        
        '''Etiqueta de la mantisa'''
        self.mantisa_label = tk.Label(self.main_frame, text="mantisa",
            bg='#c8c8c8')
        self.mantisa_label.grid(row=3, column=1, sticky=tk.W)
        
        '''Caja de entrada de la mantisa'''
        self.ent_mantisa = tk.Entry(self.main_frame, width=10, 
            textvariable=self.mantisa, bd=2, relief=tk.GROOVE)
        self.ent_mantisa.grid(row=3, column=2, sticky=tk.W + tk.E)
        
        ###############ETIQUETAS CON LOS RESULTADOS################
        '''Etiqueta del resultado convertido'''
        self.result_label = tk.Label(self.main_frame, text='Resultado',
            bg='#c8c8c8')
        self.result_label.grid(row=1, column=3, sticky=tk.W)
        
        self.convert_label = tk.Label(self.main_frame,
            textvariable=self.convert,bg='#c8c8c8')
        self.convert_label.grid(row=2, column=3)
        
        '''Etiqueta del resultado en punto flotante'''
        self.flot_label = tk.Label(self.main_frame, text='Punto flotante',
            bg='#c8c8c8')
        self.flot_label.grid(row=3, column=3, sticky=tk.W)
        
        self.flotante_label = tk.Label(self.main_frame,
            textvariable=self.flotante,bg='#c8c8c8')
        self.flotante_label.grid(row=4, column=3)
        
        
        '''Etiqueta del resultado normalizado por corte'''
        self.norm_label = tk.Label(self.main_frame, text='Por corte:',
            bg='#c8c8c8')
        self.norm_label.grid(row=1, column=4, sticky=tk.W)
        
        self.normalized_label = tk.Label(self.main_frame,
            textvariable=self.normalized_corte,bg='#c8c8c8')
        self.normalized_label.grid(row=2, column=4)

        '''Etiqueta del resultado normalizado por simetría'''
        self.norm_label = tk.Label(self.main_frame, text='Por simetría:',
            bg='#c8c8c8')
        self.norm_label.grid(row=3, column=4, sticky=tk.W)
        
        self.normalized_label = tk.Label(self.main_frame,
            textvariable=self.normalized_simetria,bg='#c8c8c8')
        self.normalized_label.grid(row=4, column=4)

        ###########BOTONES############
        '''Boton para convertir a la base que se indica'''
        self.btn_convertir_a = tk.Button(self.main_frame, text="Convertir a",
            command=self.convert_to_x, relief=tk.FLAT, bg='#c8c8c8', bd=0)
        self.btn_convertir_a.grid(row=4, column=1)
        
        '''Boton para convertira base 10'''
        self.btn_convertir_de = tk.Button(self.main_frame, text="Convertir de",
            command=self.convert_to_10, relief=tk.FLAT, bg='#c8c8c8', bd=0)
        self.btn_convertir_de.grid(row=4, column=2)
        
        '''Boton para pasar a punto flotante'''
        self.btn_flotante = tk.Button(self.main_frame, text="Flotante",
            command=self.to_flotante, relief=tk.FLAT, bg='#c8c8c8', bd=0)
        self.btn_flotante.grid(row=5, column=1, sticky=tk.E + tk.W)
        
        '''Boton para normalizar'''
        self.btn_normalize = tk.Button(self.main_frame, text="Normalizar",
            command=self.normalize, relief=tk.FLAT, bg='#c8c8c8', bd=0)
        self.btn_normalize.grid(row=5, column=2, sticky=tk.E + tk.W)
        
        '''Boton para limpiar los resultados'''
        self.btn_limpiar = tk.Button(self.main_frame, text="Limpiar",
            command=self.clean, relief=tk.FLAT, bg='#c8c8c8', bd=0)
        self.btn_limpiar.grid(row=5, column=3, sticky=tk.E + tk.W)
        
        '''Boton Acerca de'''
        self.btn_normalize = tk.Button(self.main_frame, text="Acerca de",
            command=self.about, relief=tk.FLAT, bg='#c8c8c8', bd=0)
        self.btn_normalize.grid(row=5, column=4, sticky=tk.E + tk.W)
        
    
    #####METHODS#####          
    def convert_to_x(self):
        '''
            Función que convierte el numero ingresado a 
            la base que se indique 
        '''
        numero = self.numero.get()
        base = self.base.get()
        if nm.verificar_base(numero, '10'):
            resultado = nm.base_10_a_base_x(numero, base)
        else:
            resultado = 'NaN'
        self.convert.set(resultado)
    
    def convert_to_10(self):
        '''
            Función que convierte un número en base x con x en [2,16]
            a base 10
        '''
        numero = self.numero.get()
        base = self.base.get()
        if nm.verificar_base(numero, base):
            resultado = nm.base_x_a_base_10(numero, base)
        else:
            resultado = 'NaN'
        self.convert.set(resultado)
    
    def to_flotante(self):
        '''
            Función para pasar a punto flotante
            el numero indicado en la base deseada
        '''
        numero = self.numero.get()
        base = self.base.get()
        flotante, simetria, corte = nm.normalizar_num(numero, base, 0)
        self.flotante.set(flotante)
    
    def normalize(self):
        '''
            Función para normalizar el número, a t digitos
            por corte y simetría
        '''
        numero = self.numero.get()
        base = self.base.get()
        t = self.mantisa.get()
        flotante, simetria, corte = nm.normalizar_num(numero, base, t)
        self.normalized_corte.set(corte)
        self.normalized_simetria.set(simetria)
    
    def clean(self):
        '''
            Función para limpiar todos los campos
        '''
        self.normalized_corte.set('')
        self.normalized_simetria.set('')
        self.numero.set('')
        self.base.set('')
        self.mantisa.set('')
        self.convert.set('')
        self.flotante.set('')
        self.ent_numero.focus_set()
    
    def about(self):
        '''
            Función que muestra un dialogo con información del programa
        '''
        mensaje='Autor: Matias Novoa\nVersión: 0.01\nDescripción:\n\
        Convierte números a otras bases y los convierte a punto flotante normalizado'
        showinfo(title='Acerca de', message=mensaje)

def main():
    
    root = tk.Tk()
    root.title("Normalizar")
    app = Main_app(root)
    root.mainloop()
    return 0

if __name__ == '__main__':
	main()
