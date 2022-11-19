class Empleado():

    def __init__(self):
        #Iniciador, constructor
        self.nombre = ''
        self.apellido = ''
        self.__sueldo = 0
        self.cargo = ''

    def saludar(self):
        print(str("Hola {} {} como estas?").format(self.apellido,self.nombre))

    def setSueldo(self, sueldo):
        try:
            float(sueldo)
            self.__sueldo = float(sueldo)
        except:
            self.__sueldo = 0

    def salarioDevengado(self):
        dias_liquidados = 30
        return (self.__sueldo/ 30) * dias_liquidados

    def salud(self):
        retencion = 0.04
        return (self.salarioDevengado()) * retencion

    def pension(self):
        retencion = 0.04
        return (self.salarioDevengado()) * retencion

    def totalDevengado(self):
        total = self.salarioDevengado() - self.salud() - self.pension()
        return total, self.salarioDevengado(), self.salud(),self.pension()

    def __str__(self):
        return str(
            "nombre: {} \n"
            "apellido: {} \n"
            "sueldo: {} \n"
            "cargo: {} \n"
            "totalDevengado: {} \n"
        ).format(
            self.nombre,
            self.apellido,
            self.__sueldo,
            self.cargo,
            self.totalDevengado()
        )
