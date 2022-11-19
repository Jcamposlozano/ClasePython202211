import pandas as pd
from empleado import Empleado


df_empleado = pd.read_csv('./Empleados.csv')

for i in df_empleado.values.tolist():
    empleado = Empleado()
    empleado.nombre = i[0]
    empleado.apellido = i[1]
    empleado.setSueldo(i[2])
    empleado.cargo = i[3]
    print(empleado)




