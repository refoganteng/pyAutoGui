import pyautogui
import time

            
print("Tekan Ctrl + C untuk keluar")

while True:
    x, y = pyautogui.position()
    print(f"X: {x} Y: {y}", end="\r")  # \r biar tetap di 1 baris
    time.sleep(0.1)

                