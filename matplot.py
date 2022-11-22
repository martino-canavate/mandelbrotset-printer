import numpy as np 
import matplotlib.pyplot as plt
#in this file you find the coded used to represent a mandelbrot graph

class mandelbrot(object):
	#This is the class you need to import in order to print the graph
	def __init__(self, width, height):
		self.width = width
		self.height = height
		#The parameters needed to generate an object are wifth and height

	def iterator(self, a, b):
		c = np.complex(a, b)
		z = 0
		for n in range(0,255):
			if np.absolute(z)>2:
				return n
			z = z*z +c
		return 255
		#This function is used to generate the matrix fiormed by proving if a number is in the set

	def represent(self):
		matrix = np.empty((self.width, self.height))
		a = np.linspace(-2.025, 0.6, self.width)
		b = np.linspace(-1.125, 1.125, self.height)
		for x in range(self.width):
			for y in range(self.height):
				matrix[y,x] = self.iterator(a[x], b[y])
		plt.imshow(matrix)
		plt.show()
		#This function is used to actuyally represent and print the matrix calculated in iterator


		