import pyautogui,time, pywinauto
from pywinauto.application import Application

distance = 400
pyautogui.click()

app = Application().start('Mspaint.exe')
time.sleep(1)
app.UntitledPaint.set_focus()
time.sleep(1)
pyautogui.moveTo(400, 400)

while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)
    distance = distance - 50
    pyautogui.dragRel(0, distance, duration=0.2)
    pyautogui.dragRel(-distance, 0, duration=0.2)
    distance = distance - 50
    pyautogui.dragRel(0, -distance, duration=0.2)
