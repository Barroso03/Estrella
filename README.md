# Estrella
Mi dirección de github es la siguiente: [Github](https://github.com/Barroso03/Estrella.git)

Hemos creado un código en python que nos permite dibujar una estrella de muchos lados.

El diagrama de flujo es el siguiente:

![image](https://user-images.githubusercontent.com/91721590/146820257-09ec64b2-b168-494b-b448-d3b7604ebf46.png)

El código de la primera estrella es:
```
import turtle
turtle.fillcolor("pink")
turtle.begin_fill()
count = 1
while count <= 5:
    turtle.forward(100)
    turtle.right(144)
    count += 1

turtle.end_fill()
```
El código de la estrella2 es:
```
from turtle import *
color("yellow")
begin_fill()
while True:
    forward(300)
    left(170)
    if abs(pos())< 1:
        break

end_fill
done()
```
