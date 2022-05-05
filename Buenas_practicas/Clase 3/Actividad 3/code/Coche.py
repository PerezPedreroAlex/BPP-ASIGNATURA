"""
Definición: con esta clase podremos simular en Python las características
de un coche y sus funcionalidades.

Componentes
^^^^^^^^^^^

* Clase: Coche

* Métodos:

  * Velocidad

  * Acelerar

  * Frenar

  * Marca

  * Modelo

  * Color

* Objeto: coche

Author(s)
---------
- Created by Alex Pérez on 05/01/2022.
- Modified by Alex Pérez on 05/01/2022.
- Copyright (c) 2022 Woolsey Workshop.  All rights reserved.

"""
class Coche:
    """Esta es la descripción de de la clase "Coche". A esta clase, le he añadido unos atributos fijos y unos métodos para definir un coche. 
    Con estos métodos y un objeto permitimos que la clase pueda acelerar y frenar por ejemplo.
    """
    
    marca = "Ferrari"
    velocidad = 300
    """Estos serían los atributos (características) predefinidos de la clase, en este caso del Coche.
    """
    def setColor(self, color):
        """Función que define el color de la clase.
        """   
        self.color = color

    def getColor(self):
        """Función que devuelve el color de la clase.
        """        
        return self.color

    def setModelo(self, modelo):
        """Función que define el modelo de la clase.
        """
        self.modelo = modelo 

    def getModelo (self):
        """Función que devuelve el modelo de la clase.
        """        
        return self.modelo            


    def acelerar(self):
        """Función que hace acelerar al Coche.
        """    
        self.velocidad += 1

    def frenar(self):
        """Función que hace frenar al Coche.
        """          
        self.velocidad -= 1

    def getVelocidad(self):
        """Función que devuelve la velocidad del Coche.
        """        
        return self.velocidad

coche = Coche()
"""Aquí creamos el objeto coche dentro de la clase Coche.
Con este objeto podremos realizar las funciones antes definidas.
"""
coche.setColor("amarillo")
coche.setModelo("Murcielago")
"""De esta forma aplicamos las funciones al objeto. Así podremos cambiar o poner Color y Modelo a la clase.
"""


    