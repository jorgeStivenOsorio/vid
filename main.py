import textwrap
from src.generador_contenido import Generador_contenido
import random
from src.utils import Utils as utl
from PIL import Image, ImageDraw, ImageFont
import os
from src.generador_imagenes import Generador_imagen
from config import PUBLICACIONES_DIR, ASSETS_DIR, FONTS_DIR, IMAGES_DIR, MUSIC_DIR
from src. generador_video import Generador_video
import multiprocessing

# Obtener imagen y frases
imagen_path = utl.obtener_imagen()
frases = utl.obtener_frases()
audio = utl.obtener_audio()

# Inicializar generador de imágenes
generador = Generador_imagen()

# Generar y guardar imagen en inglés
imagen_en = generador.generar_imagen(imagen_path, str(frases[0]))
generador.guardar_imagen(imagen_en, f"{PUBLICACIONES_DIR}/imagen_motivacional_en.jpg")

# Generar y guardar imagen en español
imagen_es = generador.generar_imagen(imagen_path, str(frases[1]))
generador.guardar_imagen(imagen_es, f"{PUBLICACIONES_DIR}/imagen_motivacional_es.jpg")



Generador_contenido.generar_contenido(frases)


#generador_video = Generador_video()
# Ejecutar generación de video
#generador_video.generar_video_motivacional(imagen_path=imagen_path, texto=str(frases[0]), audio_path=audio)
#generador_video.generar_video_motivacional(imagen_path=imagen_path, texto=str(frases[1]), audio_path=audio)



# Configuración para evitar problemas de multiprocesamiento en Windows
multiprocessing.freeze_support()

generador = Generador_video()
generador.generar_video_motivacional(
    imagen_path=imagen_path, 
    texto=frases,
    audio_path=audio
)