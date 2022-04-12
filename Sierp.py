import random
import turtle as tur

#Quick fun way of creating a Sierpiński triangle through random dot placements
#Say a video saying it would work so wanted to test it myself, fairly slow as it uses turtle
#to goto then use dot for each dot, more just fun to test what I saw

#Turtle object t, rep int for how many repetitions, int size of dots
def drawTri(t, rep, size):
    #Place 3 points in near edge of window
    p1 = [0,tur.screensize()[1]-100]
    p2 = [-tur.screensize()[0]+100, -tur.screensize()[1]+100]
    p3 = [tur.screensize()[0] - 100, -tur.screensize()[1] + 100]

    t.penup()
    t.goto(p1[0],p1[1])
    t.dot(size, 'black')
    t.goto(p2[0], p2[1])
    t.dot(size, 'black')
    t.goto(p3[0], p3[1])
    t.dot(size, 'black')

    p = [0,0] #temp starting point

    #Places point halfway between starting point and one of the 3 set points randomly
    for i in range(rep):
        rand = random.randint(0,2)
        if(rand == 0):
            t.goto((p[0]+p1[0])/2,(p[1]+p1[1])/2)
            p = [(p[0] + p1[0]) / 2, (p[1] + p1[1]) / 2]
            t.dot(size, 'black')
        elif(rand == 1):
            t.goto((p[0] + p2[0]) / 2, (p[1] + p2[1]) / 2)
            p = [(p[0] + p2[0]) / 2,(p[1] + p2[1]) / 2]
            t.dot(size, 'black')
        else:
            t.goto((p[0] + p3[0]) / 2, (p[1] + p3[1]) / 2)
            p = [(p[0] + p3[0]) / 2, (p[1] + p3[1]) / 2]
            t.dot(size, 'black')
        if((i+1)%1000 == 0): #Simple way to display how far its progressed by the 1000s
            t.goto(p2[0],-p2[1])
            t.color('white')
            t.write(i-999,font=("Calibri", 8, "bold"))
            t.color('black')
            t.write(i+1, font=("Calibri", 8, "bold"))

    print('Done!!')

#Setup turtle and window
tri = tur.Turtle()
tri.hideturtle()
tri.speed(0)
tur.screensize(canvwidth=400, canvheight=400)

rep = input("Number of dots: ")
size = input("Dot size: ")

drawTri(tri, int(rep), int(size))
tur.mainloop()