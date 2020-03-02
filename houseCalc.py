#PARTES EXTERNAS
from turtle import *
import math

#VARIABLES DEL PROGRAMA
color('green', 'blue')
tam = float(input("Introduzca un tamaño por favor: \n"))
roof = math.sqrt((tam/math.sqrt(2))**2)

#INICIO DE TURTLE
begin_fill()

#CUADRADO
lados = 0
while(lados != 4):
    forward(tam)
    right(90)
    lados = lados+1

#TEJADO
right(-45)
forward(roof)
right(90)
forward(roof)
right(45)

#FIN DEL PROGRAMA
end_fill()
done()
