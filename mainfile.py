import PIL
from PIL import Image
import pyautogui
from time import sleep
import numpy
from selenium import webdriver

path = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("chrome://dino")
driver.maximize_window()

def restart():
    pyautogui.click(x=678, y=376)

def play():
    sleep(1)
    pyautogui.press('up')                                                
    sleep(3)
    im1 = PIL.ImageGrab.grab(bbox = (210, 405, 320, 460))
    im1.save("im1.jpg")                                         
    grayim1 = PIL.ImageOps.grayscale(im1)
    pixelim1 = numpy.array(grayim1.getcolors())
    sum1=pixelim1.sum()
                                            
    while True:                                                    
        im2 = PIL.ImageGrab.grab(bbox = (210, 405, 320, 460))
        grayim2= PIL.ImageOps.grayscale(im2)                     
        pixelim2 = numpy.array(grayim2.getcolors())
        sum2 = pixelim2.sum()
        if sum2 > sum1:
            pyautogui.press('space')
if __name__ == '__main__':
    play()
