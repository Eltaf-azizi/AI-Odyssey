import cv2

a = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

b = cv2.VideoCapture(0)


while True:
    c_rec, d_image = b.read()
    e = cv2.cvtColor(d_image, cv2.COLOR_BGR2GRAY)
    f = a.detectMultiScale(e, 1.3, 6)


    for(x1, y1, w1, h1) in f:
        cv2.rectangle(d_image, (x1, y1), (x1+w1, y1+h1), (255, 0, 0), 5)