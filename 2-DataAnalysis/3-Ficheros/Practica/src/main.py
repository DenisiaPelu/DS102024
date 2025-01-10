from pathlib import Path
from auto_importer import AutoImporter

# Inicializa el AutoImporter, utilizando la carpeta 'src' como base
# auto_importer = AutoImporter(base_dir='src') 

base_dir = Path(__file__).parent
auto_importer = AutoImporter(base_dir=base_dir)

# Ahora puedes importar los módulos directamente por su nombre
import mi_utilidad
import mi_modelo
import procesador_texto

modelo = mi_modelo.Modelo('modelo')
resultado = modelo.multiplicar(1, 2)
print(resultado)

texto = "hola mundo"
texto_procesado = procesador_texto.procesar_texto(texto)
print(texto_procesado)


# ¿y si no fuese src sino 3-Ficheros?
# En ese caso solo cambariamos la base_dir por:
# base_dir = Path(__file__).parent / '3-Ficheros' / 'Practica' / 'src'
