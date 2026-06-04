import matplotlib.pyplot as plt
import numpy as np

f=0
a=0
u=0
v=0
x=0
kp=0.15
ki=0.005
kd=1
sum_error=0
error = 10-x
e1=0
e2=error
velocities =[]
acceleration = []
distance = []
steps =10000
times = [i*0.01 for i in range(steps)]

for dt in range(0,10000):
    velocities.append(u)
    acceleration.append(a)
    distance.append(x)
    e1=e2
    error = 10-x
    e2=error
    sum_error+=error*0.01
    a = kp*error + ki*sum_error + kd*((e2-e1)/0.01)
    
    v = u + a*0.01
    u=v
    x = x+ u*0.01 

print(velocities)
print(acceleration)
print(distance)

plt.plot(times,distance)


plt.xlabel("time")

plt.show()
    