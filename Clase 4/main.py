from indicadores import Indicadores
from calculadora import Calculadora



print('Hola buenas tardes por favor indique la operacion')
print('1. Calculadora')
print('2. Ver Indicadores Economicos')
print('3. Calcular Tabla amortizacion') 
respuesta = input('Opcion: ')

if respuesta == "1":

    print('1. suma')
    print('2. resta')
    print('4. multiplicacion')
    print('5. divicion')
    print('6. conversor de divisas')

    opcion = input('Opcion: ')

    print('su opcion fue', opcion)

elif respuesta == "2":

    print('1. trm')
    print('2. uvr')
    print('4. dtf')
    print('5. Salario Minimo')

    opcion = input('Opcion: ')
    
    print('su opcion fue', opcion)

elif respuesta == "3":

   print('solicitar variables de la tabla')

else:
    print("no es una opcion valida")



