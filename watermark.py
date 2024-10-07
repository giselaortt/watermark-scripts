import cv2
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams['image.cmap'] = 'gray'
plt.rcParams['figure.figsize'] = (15, 15)
release_position = [0,0]
image = cv2.imread('image.jpg', cv2.IMREAD_UNCHANGED)
logo = cv2.imread('lua13.png', cv2.IMREAD_UNCHANGED)


def mouse_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global click_position
        click_position = [x, y]
    elif event == cv2.EVENT_LBUTTONUP:
        global release_position
        global heigth, width
        release_position = [x, y]
        heigth = (release_position[1]-click_position[1])
        width = (release_position[0]-click_position[0])
        logo_kleben()


def logo_kleben():
    roi = image[click_position[1]:click_position[1]+heigth,click_position[0]:click_position[0]+width]
    watermark = cv2.resize(logo,(width,heigth),interpolation=cv2.INTER_CUBIC)
    roi = cv2.addWeighted(roi, 1, watermark, 0.2, 0)
    image[click_position[1]:click_position[1]+heigth,click_position[0]:click_position[0]+width]=roi
    cv2.imshow('Main Image', image)
    cv2.imwrite('watermarked.jpg',image)


if __name__ == '__main__':
    logo_rgba = cv2.cvtColor(logo, cv2.COLOR_BGRA2RGBA)
    logo = logo_rgba[:, :, 0:3]
    cv2.namedWindow('Main Image')
    cv2.imshow('Main Image', image)
    cv2.imshow('logo', logo)
    cv2.setMouseCallback('Main Image', mouse_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


