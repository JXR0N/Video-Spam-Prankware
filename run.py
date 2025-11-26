from subprocess import Popen
import sys, os

#reads file location of main.py
p = Popen(["python", "main.py"])
main_path = os.path.join(os.path.dirname(__file__), "main.py")
p = Popen([sys.executable, main_path])



#loops through main.py file a custom amount of times
for _ in range(1000): #set how many video-windows will be opened
    p = Popen(["python", "main.py"])

while True: #infinite loop so script won't stop
    input()




