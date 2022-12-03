from indicadores import Indicadores
from calculadora import Calculadora



print('Hola buenas tardes por favor indique la operacion')
print('1. Calculadora')
print('2. Ver Indicadores Economicos')
print('3. Calcular Tabla amortizacion') 

respuesta = input('Opcion: ')

if respuesta == "1":

    c = Calculadora()

    print('1. suma')
    print('2. resta')
    print('3. multiplicacion')
    print('4. divicion')
    print('5. conversor de divisas')

    opcion = input('Opcion: ')

    print('su opcion fue', opcion)

    if opcion == '1':
        a = float(input('Ingrese A: '))
        b = float(input('Ingrese B: '))
        print('Respuesta')
        c.suma(a,b)

    if opcion == '2':
        a = float(input('Ingrese A: '))
        b = float(input('Ingrese B: '))
        print('Respuesta')
        c.subtract(a,b)

    if opcion == '3':
        a = float(input('Ingrese A: '))
        b = float(input('Ingrese B: '))     
        print('Respuesta')
        c.multiplicacion(a,b)

    if opcion == '4':
        a = float(input('Ingrese A: '))
        b = float(input('Ingrese B: '))     
        print('Respuesta')
        c.division(a,b)

    if opcion == '5':
        a = input('Ingrese la moneda: ')
        b = float(input('Ingrese B: '))     
        print('Respuesta')
        c.comversorDivisas(moneda = a ,valor = b)

elif respuesta == "2":

    indicadores = Indicadores().ExtraeData()

    print('1. trm')
    print('2. uvr')
    print('3. dtf')
    print('4. Salario Minimo')

    opcion = input('Opcion: ')

    print('su opcion fue', opcion)

    if opcion == '1':        
        print('uvr', indicadores['trm'])
    if opcion == '2':        
        print('uvr', indicadores['uvr'])
    if opcion == '3':        
        print('dtf', indicadores['dtf'])
    if opcion == '4':        
        print('salarioMinimo', indicadores['salarioMinimo'])

elif respuesta == "3":

   print('solicitar variables de la tabla')

else:
    print("no es una opcion valida")



