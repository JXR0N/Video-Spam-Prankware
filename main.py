import cv2
import pygame
import win32gui
import win32con
import threading
import time
import random
from PyQt5 import QtWidgets
import sys, os


#reads the screen size/resolution of user and sets it to x and y
app = QtWidgets.QApplication(sys.argv)
screen = app.primaryScreen()
size = screen.size()
x = size.width()
y = size.height()


#function that puts video in front (topmost)
def set_window_topmost(window_name):
    hwnd = win32gui.FindWindow(None, window_name)
    if hwnd:
        win32gui.SetWindowPos(
            hwnd,
            win32con.HWND_TOPMOST,
            0, 0, 0, 0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE
        )


#reads maximum screen size and randomizes it
def getcoords():
    randomxcoord = random.randint(1, x)
    randomycoord = random.randint(1, y)
    return randomxcoord, randomycoord


#plays video in a loop
def play_video():
    for i in range(1, 500): #how many times the video is played over and over. you can customize it
        cap = cv2.VideoCapture("./Verstand.mp4") #you can put custom video file in here
        framename = "JayVirus" #set name and titlename of your prankware/video
        x, y = getcoords()
        cv2.namedWindow(framename)
        cv2.moveWindow(framename, x, y)
        while (cap.isOpened()):


            ret, frame = cap.read()
            if ret == True:
                cv2.imshow(framename, frame)
                set_window_topmost(framename)
                cv2.waitKey(18)

            else:
                break

    cap.release()
    cv2.destroyAllWindows()


#plays sound in a loop. it's synchronized with the video
def play_sound():
    for i in range(1, 500):
        pygame.mixer.init()
        pygame.mixer.music.load("./Verstand.mp3") #custom audio file
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0)
            pygame.time.Clock().tick(1)



t2 = threading.Thread(target=play_video)
t1 = threading.Thread(target=play_sound)


#starts video and audio simultaneously
def main():
    t1.start()
    t2.start()


main()
