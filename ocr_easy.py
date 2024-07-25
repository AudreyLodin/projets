import easyocr
import cv2
import numpy as np

img = cv2.imread('test1.png')
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# dilation
def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


# opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)


# skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)

    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


# template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

#custom_config = r'-l fr --psm 6'
gray = get_grayscale(img)
thresh = thresholding(gray) #good result
opening = opening(gray) #bad correction
canny = canny(gray)# same thing
reader = easyocr.Reader(['fr'])
resultat=reader.readtext(opening)
for (droite,gauche,haut,bas) ,mot,p in resultat :
    print(mot)
    print(" ")
#print(resultat)
"""
from PIL import Image, ImageDraw
img = Image.open('image.jpg')
draw = ImageDraw.Draw(img)
for (haut, droite, bas, gauche), mot, p in resultat:
  draw.rectangle([haut[0],haut[1],bas[0],bas[1]],fill=(0,0,255))
  largeur_texte, hauteur_texte = draw.textsize(mot)
  draw.rectangle([haut[0],bas[1]-hauteur_texte -10, bas[0], bas[1]], fill=(0,0,0))
  draw.text((haut[0]+6,bas[1] - hauteur_texte - 5), mot, fill=(255,255,255))
"""

