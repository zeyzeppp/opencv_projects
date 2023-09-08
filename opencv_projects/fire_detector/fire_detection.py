import cv2
import numpy as np

video_path = "fire.mp4"
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()

    if ret == False:
        break

    #print(frame.shape)
    frame = cv2.resize(frame, (640, 480))
    frame = cv2.bilateralFilter(frame, 9, 75, 75)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_fire = [0, 50, 50]
    upper_fire = [35, 255, 255]

    lower_fire = np.array(lower_fire, dtype='uint8')
    upper_fire = np.array(upper_fire, dtype='uint8')

    fire_mask = cv2.inRange(hsv, lower_fire, upper_fire)
    fire_output = cv2.bitwise_and(frame, hsv, mask=fire_mask)

    contours, hierarchy = cv2.findContours(fire_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    x, y, w, h = 0, 0, 0, 0
    if contours:
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)

        x_c = ((2 * x) + w) / 2
        y_c = ((2 * y) + h) / 2
        center = (x_c, y_c)

        print("[INFO].. center is calculated", center)

    cv2.imshow("fire", frame)
    #cv2.imshow("fire_mask", fire_mask)
    cv2.imshow("fire_output", fire_output)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()