import os

prototxt_path = r"C:\Users\m3_le\Documents\Proyectos de programación\Python\RFace\models\deploy.prototxt"

if os.path.exists(prototxt_path):
    print("✅ El archivo existe.")
else:
    print("❌ El archivo NO existe.")
