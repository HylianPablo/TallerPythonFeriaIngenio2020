#PARTES EXTERNAS
from turtle import *

#VARIABLES DEL PROGRAMA
color('green','blue')

#INICIO DE TURTLE
begin_fill()

#CUDARADO
lados=0
while(lados!=4):
    forward(100)
    right(90)
    lados=lados+1

#TEJADO
right(-45)
forward(70.71)
right(90)
forward(70.71)
right(45)

#FIN DEL PROGRAMA
end_fill()
done()
