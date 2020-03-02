#PARTES EXTERNAS
from turtle import *

#VARIABLES DEL PROGRAMA
color('green', 'blue')

#INICIO DE TURTLE
begin_fill()

#CUADRADO
lados = 0
while(lados != 4):
    forward(100)
    right(90)
    lados = lados+1

#FIN DEL PROGRAMA    
end_fill()
done()
