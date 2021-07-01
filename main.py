import PIL
import numpy as np
from selenium import webdriver
import pyautogui
from webdriver_manager.chrome import ChromeDriverManager
import time

drive = webdriver.Chrome(ChromeDriverManager().install())
drive.get("https://elgoog.im/t-rex/")
drive.maximize_window()
time.sleep(2)
pyautogui.press('up')

Game_over = False

while not Game_over:
    img = PIL.ImageGrab.grab(bbox=(630,590,730,710), include_layered_windows=False, all_screens=False, xdisplay=None)
    pix = np.array(img.getdata()).reshape(img.size[0], img.size[1], 3)
    white_pix = 0
    all = img.size[0]*img.size[1]
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if sum([pix[i][j][0], pix[i][j][1], pix[i][j][2]]) > 600:
                white_pix += 1


    if (white_pix/all) <= 0.9752:
        pyautogui.press('up')

    if (white_pix/all) < 0.85:
        Game_over = True
#




# while True:
#     img = PIL.ImageGrab.grab(bbox=(610,610,700,710), include_layered_windows=False, all_screens=False, xdisplay=None)
#     pix = np.array(img.getdata()).reshape(img.size[0], img.size[1], 3)
#     color_list = []
#     white_pix = 0
#     for i in range(img.size[0]):
#         for j in range(img.size[1]):
#             color_list.append((pix[i][j][0]+pix[i][j][1]+pix[i][j][2]))
#
#
#     for color in color_list:
#         if color > 600:
#             white_pix += 1
#
#     print(len(color_list))
#     print(white_pix)
#     print(white_pix/len(color_list))
#     img.show()
#     time.sleep(1)