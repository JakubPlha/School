from turtle import*
import colorsys

speed(0)
pensize(2)
bgcolor("black")
h = 0.5

for i in range(170):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    pencolor(c)
    h += 0.005
    circle(5 - 1, 100)
    lt(80)
    circle(5 - i, 100)
    rt(100)

mainloop()