from pynput.keyboard import Key, Controller
import os
import time

def suicune():
    if os.path.isfile("suicune.png"):
        os.remove("suicune.png")

def foto():
    archivos = os.listdir(".")

    for nombres in archivos:
        if nombres.endswith(".bmp"):
            os.rename(nombres,"suicune.png")


def pantalla():
    cambio = Controller()
    with cambio.pressed(Key.cmd_r):
        cambio.press(Key.tab)
    time.sleep(2)
    cambio.press(Key.enter)

def archivo():
    global soft_reset
    if os.path.isfile('log.txt'):
        f = open("log.txt",'r')
        leer = f.readline()
        leer = int(leer)
        soft_reset = leer

    else:
        nuevo = open("log.txt",'w')
        nuevo.write("0")
        nuevo.close()
        leer = open("log.txt",'r')
        leer = leer.readline()
        leer = int(leer)
        soft_reset = leer


def es():
    global soft_reset
    log = open("log.txt",'w')
    soft_reset = int(soft_reset)
    soft_reset += 1
    soft_reset = str(soft_reset)
    log.write(soft_reset)
    log.close()
