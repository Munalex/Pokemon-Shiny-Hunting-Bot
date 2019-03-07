import time
from pynput.keyboard import Key, Controller
import cv2
import numpy as np
import sys
import os
from funciones import *

teclado = Controller()
def reinicio():
	teclado.press('r')
	time.sleep(5)
	teclado.press('s')
	time.sleep(2)
	pantalla()
	time.sleep(2)
	teclado.press('s')
	time.sleep(2)
	pantalla()
	time.sleep(2)
	teclado.press('s')
	time.sleep(2)
	teclado.press(Key.up)
	shiny()



def shiny():
	time.sleep(20)
	pantalla()
	time.sleep(5)
	teclado.press("s")
	time.sleep(5)
	teclado.press("c")
	time.sleep(1)
	foto()
	time.sleep(1)
	shiny = cv2.imread("Suicune_Shiny.png") #open the image that has the Legendary shiny pokemon
	no_shiny = cv2.imread("suicune.png")  #open the image that has the Legendary normal pokemon
	diferencias = cv2.subtract(no_shiny, shiny)       #compare the differences of the two images
	resultado = not np.any(diferencias)               #the library returns false if it is equal this function makes it true
	if resultado == True: # does the condiction
			print("shiny encontrado tras",soft_reset,"soft reset") #print the number of restarts until reaching the shiny
		
	else:
			es()
			os.remove("suicune.png") #remove the screenshoot
			pantalla()
			time.sleep(3)
			reinicio()

time.sleep(5)
suicune()
archivo()
reinicio()