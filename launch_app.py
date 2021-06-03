## Script to automate conformance tester.

import pywinauto,time
from pywinauto.application import Application,findwindows
from pywinauto.keyboard import send_keys

## open the application
Application(backend="uia").start(cmd_line=u'C:\Program Files (x86)\OMS-Group\OMSConformanceTester\OMSConformanceTester.exe', wait_for_idle=False)
time.sleep(1)

# Connect to the application
app = Application().connect(title='OMSConformanceTester Version 4.4.5')

# Fetch the child windows
appWindow = app.window(title_re="OMSConformanceTester Version 4.4.5")

## Switch OMS mode
if appWindow.child_window(title="SettingsOMS").exists():
    settingsOmsButton = appWindow.child_window(title_re="SettingsOMS", class_name="Button")
    settingsOmsButton.click()
    time.sleep(1)

    w_handle = appWindow.child_window(title_re="OMSConformance Tester")
    # okButton = w_handle.child_window(title_re="OK", class_name="Button")
    # time.sleep(1)
    # okButton.click()

else:
  print("exit")

## Switch OMS mode
# if appWindow.child_window(title="Radio Mode").exists():
#     modeButton = appWindow.child_window(title_re="Radio Mode", class_name="Button")
#     modeButton.click()
# else:
#   print("exit")
