'''



'''

import plotly.graph_objects as go

class tablaAmortizacion():

    def __init__(self):
        self.__deuda = 0
        self.__tasa = 0
        self.__num_periodos = 0
        self.__tasa_usura = 41.46


    def setDeuda(self, deuda):
        if deuda > 0:
            self.__deuda = deuda
            return True
        else: 
            return False

    def setTasa(self, tasa):
        if tasa > 0 and tasa< self.__tasa_usura:
            self.__tasa = tasa
            return True
        else:
            return False
    
    def setPeriodos(self, num_periodos):
        if num_periodos > 0 and num_periodos< 60:
            self.__num_periodos = num_periodos
            return True
        else:
            return False


    def InputVariables(self, **kwargs):

        if self.setDeuda(kwargs['D'])== True and self.setTasa(kwargs['T']) == True and  self.setPeriodos(kwargs['N']) == True:
            print('Las variables son Correctas')
            self.calculaTabla()
        else:
            print('Error')

    def calculaTabla(self):
        
        Rcuota = (self.__deuda * self.__tasa) / (1 - pow((1 + self.__tasa), -self.__num_periodos))
        Kperiodos = 0

        l_interes = []
        l_amortizacion = []
        l_deuda = []
        l_periodos = []

        while Kperiodos!=self.__num_periodos:
            Interes = round(self.__deuda * self.__tasa,2)
            Amortizacion = round(Rcuota - Interes,2)
            self.__deuda = round(self.__deuda - Amortizacion, 2)
            Kperiodos += 1

            l_interes.append(Interes)
            l_amortizacion.append(Amortizacion)
            l_deuda.append(self.__deuda)
            l_periodos.append(Kperiodos)

        fig = go.Figure(data=[go.Table(header=dict(values=['Interes', 
                                                                'Amortizacion',
                                                                'Deuda',
                                                                'Periodos']),
                            cells=dict(values=[l_interes,
                                                l_amortizacion,
                                                l_deuda,
                                                l_periodos]))
                                ])
        fig.show()

        
t = tablaAmortizacion()

Deuda = float(input('Ingrese la Deuda '))
Tasa = float(input('Ingrese la Tasa de prestamo '))
Nperiodos = int(input('Ingrese el numero de periodos '))

t.InputVariables(D=Deuda,T=Tasa,N=Nperiodos)   

