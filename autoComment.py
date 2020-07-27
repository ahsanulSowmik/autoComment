import pyautogui
import time

comments = [ "are mama auto comment kora shikhe gechi"]

time.sleep(5)

for i in range(10):
    pyautogui.typewrite(comments[i%1])
    pyautogui.typewrite("\n")
    time.sleep(15)

