#!/usr/bin/python

from AppKit import NSWorkspace
import time
t = range(1,7200)
for i in t:
    time.sleep(3)
    activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    print activeAppName
