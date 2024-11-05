#GuitarFlash - Somewhere I Belong - Fácil

import pyautogui
import keyboard
import webbrowser
from time import sleep
webbrowser.open('http://guitarflash.com')
sleep(5)

pyautogui.click(679,475)
sleep(3)
pyautogui.click(1165,697)
sleep(2)
pyautogui.typewrite('Somewhere I Belong')
sleep(2)
pyautogui.click(665,746)
sleep(3)
pyautogui.scroll(-500)
sleep(15)
pyautogui.press('a')

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(725,704,(0,152,0)): #verifica se em determinada coordenada, determinada cor está presente
        pyautogui.press('a')
        sleep(0.05)

    if pyautogui.pixelMatchesColor(830,707,(255,0,0)): #verifica se em determinada coordenada, determinada cor está presente
        pyautogui.press('s')
        sleep(0.05)
    
    if pyautogui.pixelMatchesColor(949,707,(244,244,2)): #verifica se em determinada coordenada, determinada cor está presente
        pyautogui.press('j')
        sleep(0.05)


