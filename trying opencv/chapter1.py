import cv2

img = cv2.imread("capture.jpg")
cv2.imshow("Output", img)

# convert to grayscale
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", imggray)

# blur the image
imgblur = cv2.GaussianBlur(img, (9, 9), 0)
cv2.imshow("Blur Image", imgblur)
cv2.waitKey(0)

#capture videocam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
