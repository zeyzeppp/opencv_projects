import cv2
import numpy as np

video_path = "../sources/last.mp4"
video_copy_path = "../sources/last.mp4"
bg_path = "../results/bg.jpg"

cap = cv2.VideoCapture(video_path)
cap1 = cv2.VideoCapture(video_copy_path)

number_of_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

random_numbers = np.random.uniform(size=30)

random_frames = (number_of_frames * random_numbers)

ret, frame = cap.read()

frames = []
for random_frame in random_frames:
    cap.set(cv2.CAP_PROP_POS_FRAMES, random_frame)
    ret, frame = cap.read()
    frames.append(frame)

#background_frame = np.median(frames, axis=0).astype(dtype=np.uint8)
#background_frame = cv2.resize(background_frame, (640, 480))

if frames:
    background_frame = np.median(frames, axis=0).astype(dtype=np.uint8)
    background_frame = cv2.resize(background_frame, (640, 480))

    cv2.imwrite(bg_path, background_frame)

    cv2.imshow("Background", background_frame)
else:
    print("ERROR.. Video frames are not found.")


while True:
    ret, frame1 = cap1.read()

    if not ret:
        break

    print(frame1.shape)
    frame1 = cv2.resize(frame1, (640, 480))

    cv2.imshow("video", frame1)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
