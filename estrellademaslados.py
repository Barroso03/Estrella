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