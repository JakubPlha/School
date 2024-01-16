import turtle as t

#nastaveni asi?
t.home()
t.shape("turtle")
t.title("minecraft svet")
t.bgcolor("blue")

#nebe
t.pencolor("blue")
t.fillcolor("blue")
t.rt(90)
t.fd(200)


#udelani zeme
t.speed(0.1)
t.pencolor("green")
t.fillcolor("green")
t.begin_fill()
t.rt(90)
t.fd(1000)
t.left(180)
t.fd(2000)
t.rt(90)
t.fd(500)
t.rt(90)
t.fd(2000)
t.rt(90)
t.fd(500)
t.end_fill()
t.color("blue")

#dostani se na x = 0, y = -200
t.home()
t.pencolor("blue")
t.fillcolor("blue")
t.rt(90)
t.fd(200)
t.speed(0.5)

#delani domecku
t.pencolor("black")
t.fillcolor("#964B00")
t.begin_fill()
t.left(180)
for x in range(0, 4):
    t.fd(90)
    t.rt(90)
    if x == 3:
        t.fd(90)
        for y in range(0, 4):
            t.fd(90)
            t.rt(90)
            if y == 3:
                t.fd(90)
                for z in range(0, 4):
                    t.fd(90)
                    t.rt(90)
                    if z == 3:
                        t.fd(90)
t.end_fill()

#strecha
t.fillcolor("gray")
t.begin_fill()
for a in range(0, 4):
    t.fd(90)
    t.rt(90)
t.end_fill()

#dsotani se dolu
t.left(180)
t.fd(270)
t.left(90)
t.fd(90)
t.left(90)

#delani domecku
t.pencolor("black")
t.fillcolor("#964B00")
t.begin_fill()
for x in range(0, 4):
    t.fd(90)
    t.rt(90)
    if x == 3:
        t.end_fill()
        t.fd(90)
        t.fillcolor("#ADD8E6")
        t.begin_fill()
        for y in range(0, 4):
            t.fd(90)
            t.rt(90)
            if y == 3:
                t.end_fill()
                t.fillcolor("#964B00")
                t.begin_fill()
                t.fd(90)
                for z in range(0, 4):
                    t.fd(90)
                    t.rt(90)
                    if z == 3:
                        t.fd(90)
t.end_fill()

#strecha
t.fillcolor("gray")
t.begin_fill()
for a in range(0, 4):
    t.fd(90)
    t.rt(90)
    if a == 3:
        t.fd(90)
        for b in range(0, 4):
            t.fd(90)
            t.rt(90)
t.end_fill()


#dsotani se dolu
t.left(180)
t.fd(360)
t.left(90)
t.fd(90)
t.left(90)

#delani domecku
t.pencolor("black")
t.fillcolor("#964B00")
t.begin_fill()
for x in range(0, 4):
    t.fd(90)
    t.rt(90)
    if x == 3:
        t.fd(90)
        for y in range(0, 4):
            t.fd(90)
            t.rt(90)
            if y == 3:
                t.fd(90)
                for z in range(0, 4):
                    t.fd(90)
                    t.rt(90)
                    if z == 3:
                        t.fd(90)
t.end_fill()

#strecha
t.fillcolor("gray")
t.begin_fill()
for a in range(0, 4):
    t.fd(90)
    t.rt(90)
    if a == 3:
        t.fd(90)
        for b in range(0, 4):
            t.fd(90)
            t.rt(90)
            if b == 3:
                t.fd(90)
                for c in range(0, 4):
                    t.fd(90)
                    t.rt(90)
t.end_fill()


#dsotani se dolu
t.left(180)
t.fd(450)
t.left(90)
t.fd(90)
t.left(90)

#delani domecku
t.pencolor("black")
t.fillcolor("#D2B48C")
t.begin_fill()
for x in range(0, 4):
    t.fd(90)
    t.rt(90)
    if x == 3:
        t.fd(90)
        for y in range(0, 4):
            t.fd(90)
            t.rt(90)
            if y == 3:
                t.end_fill()
                t.fillcolor("#964B00")
                t.begin_fill()
                t.fd(90)
                for z in range(0, 4):
                    t.fd(90)
                    t.rt(90)
                    if z == 3:
                        t.fd(90)
t.end_fill()

#strecha
t.fillcolor("gray")
t.begin_fill()
for a in range(0, 4):
    t.fd(90)
    t.rt(90)
    if a == 3:
        t.fd(90)
        for b in range(0, 4):
            t.fd(90)
            t.rt(90)
t.end_fill()


#dsotani se dolu
t.left(180)
t.fd(360)
t.left(90)
t.fd(90)
t.left(90)

#delani domecku
t.pencolor("black")
t.fillcolor("#964B00")
t.begin_fill()
for x in range(0, 4):
    t.fd(90)
    t.rt(90)
    if x == 3:
        t.fd(90)
        for y in range(0, 4):
            t.fd(90)
            t.rt(90)
            if y == 3:
                t.fd(90)
                for z in range(0, 4):
                    t.fd(90)
                    t.rt(90)
                    if z == 3:
                        t.fd(90)
t.end_fill()

#strecha
t.fillcolor("gray")
t.begin_fill()
for a in range(0, 4):
    t.fd(90)
    t.rt(90)

t.end_fill()



#konec
t.mainloop()