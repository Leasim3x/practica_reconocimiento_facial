import cv2

# Cargar el clasificador en cascada para detección de rostros
cascade_path = "models\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

# Abrir un archivo de video
capture = cv2.VideoCapture("video\\video1.mp4")

# Leer el video cuadro por cuadro
while True:
    ret, frame = capture.read()

    if not ret:
        break

    # Convertir a escala de grises para mejorar la detección
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostros en el cuadro
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Dibujar rectángulos alrededor de los rostros detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar el video con la detección de rostros
    cv2.imshow("Detección de Rostros", frame)

    # Salir del bucle cuando se presione la tecla "q"
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Liberar la captura de video
capture.release()
cv2.destroyAllWindows()
