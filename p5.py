from vpython import *
import time
k=500
m=1
g=10
b=10
scene = graph( width=1000, height=400)
class bball():
    def __init__(self,pos=vec(0,0,0),v=vec(0,0,0),a=vec(0,0,0)):
        self.pos=pos
        self.v=v
        self.a=a
len0=0.2
class sspring():
    def __init__(self,len=0):
        self.len=len

        
balls=[bball(pos=vec(0,i*0.2,0)) for i in range(1001)]
springs=[sspring(len=(i))for i in range(1000)]
dt=0.01
t=0
f1 = gcurve(color=vec(101/255,213/255,196/255),graph=scene)
f2 = gcurve(color=color.red,graph=scene)
f3 = gcurve(color=color.orange,graph=scene)
state=0
#def keyinput(evt):
    #global state
    #s = evt.key
    #if s:
        #state+=1
#scene.bind('keydown', keyinput)
for i in reversed(range(1000)):
    balls[i].pos.y=balls[i+1].pos.y-m*(i+1)*g/k-len0
for i in range(1000):
    springs[i].len=balls[i+1].pos.y-balls[i].pos.y
#scene.waitfor('keydown')
t=0
while True:
    rate(2000000000)
    t+=dt
    balls[0].a=vec(0,-g+(springs[0].len-len0)*k,0)/m
    for i in range(1,1000):
        balls[i].a=vec(0,-g+(springs[i].len-len0)*k-((springs[i-1].len-len0))*k,0)/m
    balls[1000].a=vec(0,-g-(springs[999].len-len0)*k,0)
    #for i in range(20):
        #if balls[i].pos.y>balls[i+1].pos.y:
            #balls[i].v,balls[i+1].v=balls[i+1].v,balls[i].v
    for ball in balls:
        ball.v+=ball.a*dt
        ball.pos+=ball.v*dt
    for i in range(1000):
        springs[i].len=balls[i+1].pos.y-balls[i].pos.y
    f1.plot(pos=(t,-balls[0].v.y))
    #f2.plot(pos=(t,sum(-ball.v.y for ball in balls)/1001))
    f2.plot(pos=(t,-balls[500].v.y))
    f3.plot(pos=(t,-balls[1000].v.y))