import cv2

# Leer la imagen desde el disco
image = cv2.imread("images\img1.jpg")

# Verificar si la imagen se cargó correctamente
if image is None:
    print("Error al cargar la imnagen.")
else:
    print("Imagen cargada correctamente.")