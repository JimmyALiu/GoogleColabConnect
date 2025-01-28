import pyautogui
import time
import random


width, height = pyautogui.size()
x, y = width // 2, height // 2
x_var, y_var = int(width * 0.18), int(height * 0.12)

while True:
    # form delay
    delay = random.randint(8, 10)  # 8 - 10 minutes
    time.sleep(delay)

    # pick a spot
    x_noise = random.randint(-x_var, x_var)
    y_noise = random.randint(-y_var, y_var)

    # move the mouse
    duration = random.randint(1, 10)
    pyautogui.moveTo(x + x_noise, y + y_noise, duration=duration)

