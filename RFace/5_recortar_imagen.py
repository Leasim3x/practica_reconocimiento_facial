import cv2

# Leer la imagen
image = cv2.imread("images\img1.jpg")

# Definir el área de recorte seleccionando una área especifica (y1:y2, x1,x2) (largo, ancho)
cutting = image[25:250, 100:300]

# Mostrar la imagen recortada
cv2.imshow("Imagen recortada", cutting)
cv2.waitKey(0)
cv2.destroyAllWindows()