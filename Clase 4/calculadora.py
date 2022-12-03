from indicadores import Indicadores

class Calculadora():

    def suma (self, a, b):
        print(a+b)

    def subtract (self, a, b):
        print(a-b)

    def multiplicacion (self, a,b):
        print (a*b)

    def division(self, a,b):
        if b == 0: 
            print("error base 0")
        else:
            print(str(a/b))

    def comversorDivisas(self, **kwargs):
        i = Indicadores().ExtraeData()
        try:
            valor = float(kwargs['valor'])

            if kwargs['moneda'] == 'Peso':
                print('El valor del dolar es: ', str(valor / i['trm']) )
            else:
                print('El valor del peso es: ', str(valor * i['trm'])) 
        except:
            print('error')
        
        
        