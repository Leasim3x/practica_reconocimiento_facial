import cv2

# Cargar el clasificador de rostros
cascade_path = "models\haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

# Capturar video desde la cámara del celular
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()

    if not ret:
        break

    # Reducir la escala de la imagen (por ejemplo, a un 50% de su tamaño original)
    scale_percent = 50  # Porcentaje de reducción
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    frame_resized = cv2.resize(frame, (width, height))

    # Convertir a escala de grises
    gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)

    # Detectar rostros
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Dibujar rectángulos en los rostros detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame_resized, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar el video con detección en escala reducida
    cv2.imshow("Detección de Rostros - Escalado", frame_resized)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar ventanas
capture.release()
cv2.destroyAllWindows()
