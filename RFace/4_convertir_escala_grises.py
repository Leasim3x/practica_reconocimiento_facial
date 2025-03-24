import cv2

# Leer la imagen desde el disco
image = cv2.imread("images\img1.jpg")

# Convertir la imagen a escala de grises
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Mostrar la imagen en escala de grises
cv2.imshow("Imagen en escala de grises", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()