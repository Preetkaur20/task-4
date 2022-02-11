import cv2

#for importing a specific image

image = cv2.imread('Picture.jpg')

#name of a image

grey_img =cv2.cvtcolor(image, cv2.COLOR_BGR2GRAY)

#command for color selection

invert_img = cv2.bitwise_not(grey_img)

#inverting an image

blur_img = cv2.GaussianBlur(invert_img, (21,21),00)

#we used blur_img for the resizing of inverted img that we put up in command named as invert_img

inverted_img =cv2.bitwise_not(blur_img)

sketch = cv2.divide(grey_img, invert_img, scale=256.0)

cv2.imwrite('sketch.png', sketch)
