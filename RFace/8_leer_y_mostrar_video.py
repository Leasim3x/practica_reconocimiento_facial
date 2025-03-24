import cv2

# Abrir un archivo de video
capture = cv2.VideoCapture("video\\video1.mp4")

# Leer el video cuadro por cuadro
while True:
    ret, frame = capture.read()

    if not ret:
        break

    # Mostrar cada cuadro
    cv2.imshow("Video", frame)

    # Salida del bucle cuando se presione la tecla "q"
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Liberar la captura de video
capture.release()
cv2.destroyAllWindows()