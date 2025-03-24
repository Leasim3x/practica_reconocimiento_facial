import cv2

# Cargar el clasificador de rostros preentrenado
cascade_path = "models\haarcascade_frontalface_default.xml"
classify = cv2.CascadeClassifier(cascade_path)

#Leer la imagen
image = cv2.imread("images\img1.jpg")

# Convertir a escala de grises
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectar rostros en la imagen
faces = classify.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=5)

# Dibujar rectangulos alrededor de los rostros detectados}
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Mostrar la imagen con los rostros detectados
cv2.imshow("Deteccion de Rostros", image)
cv2.waitKey(0)
cv2.destroyAllWindows()