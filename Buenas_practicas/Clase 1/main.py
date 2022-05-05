#Excepciones

# try:
#     numero = 10
#     divisor = int(input("Introduzca un divisor: "))
#     resultado = numero/divisor
#     file = open("myfile.txt", "w")

# except ZeroDivisionError:
#     print("Se ha producido una division entre 0")
# except ValueError:
#     print("Introduzca un número")
# except IOError:
#     print("Error obteniendo el fichero")    
# except Exception as error:
#     print(f"Ha ocurrido una excepción {error}")
# else: #se ejecutará siempre y cuando no se ejecute el except
#     print("No ha habido ninguna excepción")    
# finally:
#     file.close()

#raise - lanzar excepciones
# raise ZeroDivisionError("Informacion de la excepcion")

#creando una excepción personalizada:
# class MiExcepcion(Exception):
#     def __init__(self, param1,param2):
#         self.param1 = param1
#         self.param2 = param2

# try:
#     raise MiExcepcion("Valor parametro 1", "Valor parametro 2")
# except MiExcepcion as error:
#     p1,p2 = error.args
#     print(p1)
#     print(p2)


#assert - nos van a permitir comprobaciones

# assert(1==2)
#lanza una expcecion de tipo AssertionError

# if condicion:
#     raise AssertionError()                        


def suma(num1,num2):
    assert(type(num1) == int)
    assert(type(num2) == int)
    return num1 + num2

#assert en testing
# assert(suma(2,2) == 4)
# print("****************")
# assert(suma(2,2) == 3)

#assert en funciones
assert(suma(3,3))

#assert con clases
class Miclase():
    pass

class OtraClase():
    pass

obj1 = Miclase()
obj2 = OtraClase()

assert(isinstance(obj1,Miclase))
assert(isinstance(obj2,Miclase))

#deshabilitar assert
#python -O main.py PARA QUE NO SALTE NINGÚN ERROR

