from vpython import *
import time
k=500
m=1
g=10
spring_l=0.2
b=10
scene = canvas(width=600, height=600,background=color.white)
balls=[sphere(radius=0.01, color=color.red, pos=vector(0,5+0.2*i,0),m=m,v=vec(0,0,0),a=vec(0,0,0)) for i in range(21)]
springs=[helix(radius=0.5,pos=vec(0,5+0.2*i,0),axis=vec(0,0.2,0),coils=1,color=color.orange)for i in range(20)]
dt=0.001
t=0
g1=graph( width=600, height=200,align='right')
f1 = gcurve(color=vec(101/255,213/255,196/255),graph=g1)
f2 = gcurve(color=color.red,graph=g1)
state=0
def keyinput(evt):
    global state
    s = evt.key
    if s:
        state+=1
scene.bind('keydown', keyinput)

while True:
    rate(10000)
    scene.center=balls[10].pos
    balls[0].a=vec(0,-g+(springs[0].axis.y-spring_l)*k-b*balls[0].v.y,0)/m
    for i in range(1,20):
        balls[i].a=vec(0,-g+(springs[i].axis.y-spring_l)*k-(springs[i-1].axis.y-spring_l)*k-b*balls[i].v.y,0)/m
    #balls[100].a=vec(0,-g-(springs[99].axis.y-spring_l)*k,0)
    for ball in balls:
        ball.v+=ball.a*dt
        ball.pos+=ball.v*dt
    for i in range(20):
        springs[i].pos=balls[i].pos
        springs[i].axis=balls[i+1].pos-balls[i].pos
    t+=dt
    if state!=0:
        state=0
        break
time.sleep(2)
t=0
while True:
    rate(200)
    t+=dt
    scene.center=balls[10].pos
    balls[0].a=vec(0,-g+(springs[0].axis.y-spring_l)*k,0)/m
    for i in range(1,20):
        balls[i].a=vec(0,-g+(springs[i].axis.y-spring_l)*k-(springs[i-1].axis.y-spring_l)*k,0)/m
    balls[20].a=vec(0,-g-(springs[19].axis.y-spring_l)*k,0)
    #for i in range(20):
        #if balls[i].pos.y>balls[i+1].pos.y:
            #balls[i].v,balls[i+1].v=balls[i+1].v,balls[i].v
    for ball in balls:
        ball.v+=ball.a*dt
        ball.pos+=ball.v*dt
    for i in range(20):
        springs[i].pos=balls[i].pos
        springs[i].axis=balls[i+1].pos-balls[i].pos
    f1.plot(pos=(t,-balls[20].v.y))
    f2.plot(pos=(t,sum(-ball.v.y for ball in balls)/20))
