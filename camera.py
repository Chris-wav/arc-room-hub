import cv2

cap = cv2.VideoCapture(0)
previous_gray = None

if not cap.isOpened():
    print("Camera didn't open")
    raise SystemExit

try:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("No picture taken")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if previous_gray is None:
            previous_gray = gray
            continue

        diff = cv2.absdiff(previous_gray, gray)

        _, mask = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

        cv2.imshow("Grayscale", gray)
        cv2.imshow("Difference", diff)
        cv2.imshow('Binary Mask', mask)

        previous_gray = gray

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    cv2.destroyAllWindows()
    cap.release()
