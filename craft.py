import time
import threading
import os

import pyautogui
from pynput import keyboard


def craft():
    i = 1
    y = 450
    for _ in range(3):
        x = 865
        for _ in range(3):
            pyautogui.moveTo(x=x, y=y)
            pyautogui.press(str(i))

            x = x + 30
            i = i + 1

        y = y + 30

    time.sleep(0.2)
    with pyautogui.hold('shift'):
        pyautogui.moveTo(x=1050, y=490)
        pyautogui.leftClick()


def start():
    y = 590
    craft()
    for _ in range(3):
        time.sleep(0.5)
        x = 820
        for i in range(1, 10):
            pyautogui.moveTo(x=x, y=y)
            pyautogui.press(str(i))
            time.sleep(0.01)

            x = x + 35

        time.sleep(0.5)
        craft()

        y = y + 30


def on_press(key):
    try:
        k = key.char
    except:
        k = key.name

    craft_thread = threading.Thread(target=start)
    if k == "left":
        craft_thread.start()
        return False

    if key == keyboard.Key.down:
        os._exit(0)


print("Для начала крафта нажмите стрелку влево. Для резкого выключения стрелку вниз.")

while True:
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
