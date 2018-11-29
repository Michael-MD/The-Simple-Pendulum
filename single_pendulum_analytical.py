import numpy as np
from drawClass import *
import time

#note: initial angle cannot be zero when t is 0
t_n = 0	#t0
x_n = 180	#amplitde i.e. max angle
y_n = 0	#starting velocity	theta dot 0


L = 2
g = 9.8
w = np.sqrt(g/L)	#where g is gravity and L is length of pendulum

theta0 = x_n*np.pi/180
thetadot0 = y_n*np.pi/180
t0 = t_n

phi = np.arctan( -thetadot0/(theta0*w) )-w*t0
A0 = theta0 / np.cos( w*t0 + phi )

def theta(t):
	return A0*np.cos(w*t + phi)

canvas = cylindricalCanvas([500,500])


while True:
	# print(t_n,x_n,y_n)

	x_n = theta(t_n)

	canvas.clearCanvas()	#clear previous frame
	canvas.lineo([0,0],[L*100, x_n*(180/np.pi)-90 ])	#draw pendulum
	# canvas.circle([L*100, x_n*(180/np.pi)-90 ],10)	#draw mass on end of pendulum
	time.sleep(0.04)

	t_n+=0.1
