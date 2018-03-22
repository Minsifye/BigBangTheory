#!/usr/bin/python
import webbrowser
import time

counter = 1
while counter <= 3:
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=fN6eaOR73SM")
    counter = counter + 1

print ("End of program")
print ("Testing github")