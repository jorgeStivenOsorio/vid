import os

# Directorios base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PUBLICACIONES_DIR = os.path.join(BASE_DIR, "publicaciones")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")
IMAGES_DIR = os.path.join(ASSETS_DIR, "images")
USED_IMAGES_DIR = os.path.join(IMAGES_DIR, "usadas")
MUSIC_DIR = os.path.join(ASSETS_DIR, "musica")

# Archivos de frases
FRASES_FILE_EN = os.path.join(BASE_DIR, "frases_ingles.txt")
FRASES_FILE_ES = os.path.join(BASE_DIR, "frases_espanol.txt")

# Configuración de timeouts (en segundos)
TIMEOUT_API = 30
TIMEOUT_VIDEO = 300  # 5 minutos máximo por video
TIMEOUT_PROCESS = 600  # 10 minutos máximo para todo el proceso

# Asegúrate de que los directorios existan
for dir_path in [PUBLICACIONES_DIR, ASSETS_DIR, FONTS_DIR, IMAGES_DIR, USED_IMAGES_DIR, MUSIC_DIR]:
    os.makedirs(dir_path, exist_ok=True)
