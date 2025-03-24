import cv2
import os
from pathlib import Path

# Ruta absoluta a la carpeta de modelos
model_dir = Path(r"C:\Users\m3_le\Documents\Proyectos_de_programación\Python\RFace\models")

# Rutas de los archivos
prototxt_path = os.path.join(model_dir, "deploy.prototxt")
model_path = os.path.join(model_dir, "res10_300x300_ssd_iter_140000_fp16.caffemodel")

# Verificar si los archivos existen
if not os.path.exists(prototxt_path):
    raise FileNotFoundError(f"Archivo no encontrado: {prototxt_path}")

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Archivo no encontrado: {model_path}")

# Cargar el modelo
net = cv2.dnn.readNetFromCaffe(str(prototxt_path), str(model_path))
print("Modelo cargado correctamente ✅")

# Capturar video desde la cámara del celular (ajusta la IP según IP Webcam)
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # Obtener dimensiones del frame
    h, w = frame.shape[:2]

    # Preprocesar la imagen para la red neuronal
    blob = cv2.dnn.blobFromImage(frame, scalefactor=1.0, size=(300, 300), mean=(104.0, 177.0, 123.0))

    # Pasar la imagen por la red neuronal
    net.setInput(blob)
    detections = net.forward()

    # Dibujar los rectángulos en los rostros detectados
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.5:  # Umbral de confianza
            box = detections[0, 0, i, 3:7] * [w, h, w, h]
            (x, y, x2, y2) = box.astype("int")

            cv2.rectangle(frame, (x, y), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"Conf: {confidence:.2f}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Mostrar la imagen con detecciones
    cv2.imshow("Detección con CNN (OpenCV)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
