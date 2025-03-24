import cv2

# Usa el índice de la cámara de DroidCam (normalmente 0 o 1)
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()

    if not ret:
        break

    cv2.imshow("Camara Android - OpenCV", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
