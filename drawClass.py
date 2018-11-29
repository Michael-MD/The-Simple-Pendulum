import turtle as tl
import numpy as np


class canvasSetup():
	def __init__(self , canvasDimensions , strokeThickness = 2):
		self.window = tl.Screen()		#initilize window size
		self.Dimensions = canvasDimensions
		self.defaultStroke = strokeThickness
		tl.setup(self.Dimensions[0],self.Dimensions[1])		#initilize color
		tl.pensize(strokeThickness)		#initilize thickness
		tl.ht()	#hide turtle
		tl.tracer(0,0)	# draw instanstaniously

	def move(self, coords):
		tl.penup()
		tl.setpos(coords[0] , coords[1])
		tl.pendown()

	def line(self, startCoords, endCoords):
		self.move(startCoords)
		tl.goto(endCoords[0] , endCoords[1])

		tl.update()

	def lineo(self, startCoords, endCoords):
		startCoords = self.coordConversion(startCoords)
		endCoords = self.coordConversion(endCoords)
		self.move(startCoords)
		tl.goto(endCoords[0] , endCoords[1])

		tl.update()

	def rectangle(self, center, w, h, rotAngle = 0, centalRot = False):
		center = self.coordConversion(center)
		segment = np.divide([w,h],2)
		rotMatrix = np.array((  (np.cos(rotAngle*np.pi/180),np.sin(-rotAngle*np.pi/180)) , (np.sin(rotAngle*np.pi/180),np.cos(rotAngle*np.pi/180))  ))
	
		S1 = [  [1,1],[-1,1],[-1,1],[-1,-1]  ]
		S2 = [  [1,-1],[-1,-1],[1,1],[1,-1]  ]
		if not centalRot:
			#  rotate about origin
			for S in range(0,len(S1)):	#draw sides
				self.line( np.matmul(rotMatrix, np.add(center,np.multiply(segment,S1[S])) ) , np.matmul(rotMatrix, np.add(center,np.multiply(segment,S2[S])) ) )
		else:
			#  rotate about objects center
			for S in range(0,len(S1)):	#draw sides
				self.line( np.add(np.matmul(rotMatrix, np.add([0,0],np.multiply(segment,S1[S])) ),center) , np.add(np.matmul(rotMatrix, np.add([0,0],np.multiply(segment,S2[S])) ),center) )


		tl.update()

	# def text(self, message):
	# 	tl.write("messi fan", font=("Arial", 16, "normal"))

	def triangle(self, center, sideLengths):
		pass


	def circle(self, center, radius):
		center = self.coordConversion(center)
		self.move([center[0], center[1]-radius])
		tl.circle(radius)

		tl.update()

	def beginFill(self, fillColor = "black"):
		tl.fillcolor(fillColor)
		tl.begin_fill()

	def endFill(self):
		tl.end_fill()

	def clearCanvas(self):
		tl.clear()

	def __del__(self):
		tl.mainloop()
		tl.exitonclick()



class cartesianCanvas(canvasSetup):
	def coordConversion(self, coords):	#do nothing if already in cartesian coordinates
		return coords

	def grid(self, spacings, grid = False):
		#vertical lines
		for spacing in range(-int(self.Dimensions[0]/2),int(self.Dimensions[0]/2),spacings):		#vetrical spacing
			self.line([-spacing,-self.Dimensions[1]/2],[-spacing,self.Dimensions[1]/2])
			tl.write(-spacing)
			
		#horizontal lines
		for spacing in range(-int(self.Dimensions[1]/2),int(self.Dimensions[1]/2),spacings):		#horizontal spacing
			self.line([-self.Dimensions[0]/2,-spacing],[self.Dimensions[0]/2,-spacing])
			tl.write(-spacing)

		if grid:
			tl.pensize(8)
			#horizontal axis
			self.line([-int(self.Dimensions[0]/2),0],[int(self.Dimensions[0]/2),0])
			#vertical axis
			self.line([0,-int(self.Dimensions[1]/2)],[0,int(self.Dimensions[1]/2)])
			tl.pensize(self.defaultStroke)
		tl.update()

	# def text(self, message):
	# 	tl.write("messi fan", font=("Arial", 16, "normal"))



class cylindricalCanvas(canvasSetup):
	def coordConversion(self, coords):	#convert cylindrical to cartesian coordinates
		ccoords = [None]*2
		ccoords[0] = coords[0]*np.cos(coords[1]*np.pi/180)	#x
		ccoords[1] = coords[0]*np.sin(coords[1]*np.pi/180)	#y
		return ccoords

	def grid(self, spacings, angleSpacing = 10):
		if self.Dimensions[0] < self.Dimensions[1]:
			maxrad = self.Dimensions[0]/2
		else:
			maxrad = self.Dimensions[1]/2

		for radius in range(0, int(maxrad), spacings):	#concentric circles
			self.circle([0,0], radius)
		
		for radius in range(0, int(maxrad), spacings):	#labels
			self.move([radius, 0])
			tl.write(-radius)

		for angle in range(0,180, angleSpacing):	#angles
			self.line(self.coordConversion([maxrad, angle+180]),self.coordConversion([maxrad, angle]))
			tl.write(angle)