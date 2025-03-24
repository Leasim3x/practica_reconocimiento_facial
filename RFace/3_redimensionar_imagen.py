import cv2

# Leer la imagen desde el disco
image = cv2.imread("images\img1.jpg")

# Redimensionar la imagen (pixeles de ancho, pixeles de alto)
#image_redi = cv2.resize(image, (300, 300))
image_redi = cv2.resize(image, (150, 150))

# Mostrar la imagen redimensionada
cv2.imshow("Imagen Redimensionada", image_redi)
cv2.waitKey(0)
cv2.destroyAllWindows()