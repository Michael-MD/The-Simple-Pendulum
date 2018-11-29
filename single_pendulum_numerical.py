import numpy as np
from drawClass import *
import time

t_n = 0	#t0
x_n = 0	#starting angle from verical degrees
y_n = 90	#starting velocity	degree/sec

x_n = x_n * np.pi/180	#convert to rad
y_n = y_n * np.pi/180


# t_f = 100
h = 0.001

L = 2
g = 9.8
w = np.sqrt(g/L)	#where g is gravity and L is length of pendulum


canvas = cylindricalCanvas([500,500])
while True:
	# print(t_n,x_n,y_n)

	t_temp = t_n + h
	x_temp = x_n + h*y_n	#angle from vertical
	y_temp = y_n + h*(-w*np.sin(x_n))	#velocity

	t_n = t_temp
	x_n = x_temp
	y_n = y_temp

	canvas.clearCanvas()	#clear previous frame
	canvas.lineo([0,0],[L*100, x_n*(180/np.pi)-90 ])	#draw pendulum
	#	canvas.circle([L*100, x_n*(180/np.pi)-90 ],10)	#draw mass on end of pendulum
	time.sleep(0.00001)
