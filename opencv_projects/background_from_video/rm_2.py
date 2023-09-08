import cv2
import numpy as np

video_path = "../sources/dv2.mp4"
bg_path = "../results/bg_1.jpg"

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
print(frame.shape)


number_of_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(number_of_frames)

random_numbers = np.random.uniform(size = 30)
print(random_numbers)

random_frames = (number_of_frames * random_numbers)
print(random_frames)

frames = []
for random_frame in random_frames:
    cap.set(cv2.CAP_PROP_POS_FRAMES, random_frame)
    ret, frame = cap.read()
    frames.append(frame)

background_frame = np.median(frames, axis = 0).astype(dtype = np.uint8)
background_frame = cv2.resize(background_frame, (640, 480))


cv2.imwrite(bg_path, background_frame)

cv2.imshow("BG", background_frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
