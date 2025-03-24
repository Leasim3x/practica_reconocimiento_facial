import cv2

# Leer la imagen desde el disco
image = cv2.imread("images\img1.jpg")

# Mostrar la imagen en una ventana
cv2.imshow('Imagen', image)

# Esperar a que el usuario cierre la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()