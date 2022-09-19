import pyautogui as pg
import time
limit = input("Enter limit: ")
message = input("Enter Message: ")
time.sleep(5)
i = 0

while i < int(limit):
    pg.typewrite(message)
    pg.press("enter")
    i += 1
    time.sleep(0.25)

