import cv2

# Leer la imagen
image = cv2.imread('images\img1.jpg')

# Convertir a escala de grises
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar la detección de bordes de Canny
edge = cv2.Canny(image_gray, 100, 200)

# Mostrar la imagen con bordes detectados
cv2.imshow('Bordes con Canny', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()