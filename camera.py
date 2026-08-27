import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera didn't open")
    raise SystemExit

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print('No picture taken')
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Grayscale', gray)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    cv2.destroyAllWindows()
    cap.release()
