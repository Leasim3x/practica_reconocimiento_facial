import cv2
from deepface import DeepFace

# Capturar video desde la cámara
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    try:
        # Analizar el rostro con DeepFace en la imagen original
        analysis = DeepFace.analyze(frame, actions=['age', 'gender', 'emotion'], enforce_detection=False)

        # Extraer datos de reconocimiento
        age = analysis[0]['age']
        gender = analysis[0]['dominant_gender']
        emotion = analysis[0]['dominant_emotion']

        # Reducir la escala de la imagen para mejorar la visualización
        scale_percent = 25  # Ajusta el tamaño mostrado (50% de la imagen original)
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        frame_resized = cv2.resize(frame, (width, height))

        # Dibujar la información en la imagen escalada
        cv2.putText(frame_resized, f"Edad: {age}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)
        cv2.putText(frame_resized, f"Genero: {gender}", (10, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)
        cv2.putText(frame_resized, f"Emocion: {emotion}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)

        # Mostrar el video con la información
        cv2.imshow("Reconocimiento Facial con DeepFace", frame_resized)

    except:
        pass

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar ventanas
capture.release()
cv2.destroyAllWindows()
