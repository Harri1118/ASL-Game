import cv2

cv2.namedWindow("preview")
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed")
        break
    cv2.imshow('camera', frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        print("closing app...")
        break

cam.release()
cam.destroyAllWindows()
cv2.waitKey(1) 