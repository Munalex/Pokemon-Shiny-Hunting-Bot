import time
from pynput.keyboard import Key, Controller
import cv2
import numpy as np
import sys

time.sleep(5)
def Combate():
	teclado = Controller()
	teclado.press('a') #start the fight
	time.sleep(10)
	teclado.press(Key.f12) #make a ScreenShoot

	

Combate()

def Comparar():
	shiny = cv2.imread("/Images/registeel_shiny.png") #open the image that has the Legendary shiny pokemon
	no_shiny = cv2.imread("Pokemon_Esmeralda-0.png")  #open the image that has the Legendary normal pokemon
	diferencias = cv2.subtract(no_shiny, shiny)       #compare the differences of the two images
	resultado = not np.any(diferencias)               #the library returns false if it is equal this function makes it true
	soft_reset = 0 #soft reset counter
	if resultado == True: # does the condiction
		print("shiny encontrado tras",soft_reset,"soft reset") #print the number of restarts until reaching the shiny
		
	else:
		++soft_reset # increase the counter
		os.remove("Pokemon_Esmeralda-0.png") #remove the screenshoot
		


def reinicio():
	with teclado.pressed(Key.ctrl): #reboot the emulator
		teclado.press('r')
	time.sleep(5)
	teclado.press('a') 
	time.sleep(2)
	teclado.press('a')
	time.sleep(8)
	teclado.press('s') #press start
	time.sleep(5)
	time.press('a')



