import cv2
from deepface import DeepFace
import pandas as pd
import os

# Ruta de la base de datos de rostros
db_path = "faces_db"

# Capturar video desde la cámara
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    try:
        # Guardar temporalmente el frame como imagen
        temp_imp_path = "temp.jpg"
        cv2.imwrite(temp_imp_path, frame)

        # Analizar el rostro con FaceNet
        result = DeepFace.find(img_path=temp_imp_path, db_path=db_path, model_name="Facenet", enforce_detection=False)

        if isinstance(result, list) and len(result) > 0 and not result[0].empty:
            # Extraer el nombre de la carpeta (persona reconocida)
            identity_path = result[0]['identity'].iloc[0]  # Ruta de la imagen reconocida
            person_name = identity_path.split("/")[-2]  # Obtener nombre de la carpeta (persona)
        else:
            # Inicializar como "Desconocido"
            person_name = "Desconocido"

        # Dibujar la información en la imagen
        cv2.putText(frame, f"Nombre: {person_name}", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    except Exception as e:
        print("Error en detección:", str(e))

    # Reducir la escala de la imagen para mejorar el rendimiento
    scale_percent = 25  
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    frame_resized = cv2.resize(frame, (width, height))

    # Mostrar el video con la información
    cv2.imshow("Reconocimiento Facial con FaceNet", frame_resized)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar ventanas
capture.release()
cv2.destroyAllWindows()

# Eliminar la imagen temporal
if os.path.exists(temp_imp_path):
    os.remove(temp_imp_path)
