import cv2
import os

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
name = 'Jack'
i = 1
os.makedirs(name, exist_ok=True)
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 1600, 900)
while True:
    ret, frame = cap.read()
    cv2.rectangle(frame, (465,135), (815,585), (0,0,255), 2)
    face = cv2.cvtColor(frame[135:585, 465:815, :], cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    cv2.imshow('face', face)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite(f'{name}/{i}.jpg', face)
        print(f'Saved {name}/{i}.jpg')
        i += 1
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()