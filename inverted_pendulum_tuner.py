import matplotlib.pyplot as plt
import numpy as np

#lets take initial pendulum angle to be equal to 30 degrees
#lets assume dt = 0.01 and number of steps to be 10000
dt = 0.01
theta = np.radians(30)
error = theta
e1=error
e2=error
kp=90
ki=5
kd=10
acc_theta = 0
vel_theta = 0 
acc_x = 0 
vel_x = 0
x = 0
M = 5
m=1 
g = 10 
l = 1
steps = 10000 
sum_error = 0
angles = []
time = [i*0.01 for i in range(steps) ]

for i in range(steps):
    angles.append(theta)
    error = theta
    e1=e2
    e2=error
    sum_error+= error*dt
    f = kp*error + ki*sum_error + kd*(e2-e1)/0.01
    acc_theta = ((M+m)*g*np.sin(theta)  -f*np.cos(theta)-m*l*np.sin(theta)*np.cos(theta)*vel_theta**2 )/ ((M+m)*l - m*l*np.cos(theta)**2)
    vel_theta = vel_theta + dt*acc_theta
    theta += dt*vel_theta
    acc_x = (f-m*l*acc_theta*np.cos(theta) + m*l*vel_theta**2*np.sin(theta))/(M+m)
    vel_x +=dt*acc_x
    x+= dt*vel_x 

plt.plot(time,angles)
plt.show()
    

