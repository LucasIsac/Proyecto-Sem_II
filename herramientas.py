import os
import shutil
from docx2pdf import convert
from pathlib import Path

def convertir_word_a_pdf(ruta_entrada, ruta_salida=None):
    """Convierte un archivo .docx a .pdf"""
    if ruta_salida is None:
        ruta_salida = Path(ruta_entrada).with_suffix('.pdf')
    convert(ruta_entrada, ruta_salida)
    return f"✅ Documento convertido a PDF: {ruta_salida}"

def renombrar_archivo(ruta_actual, nuevo_nombre):
    """Renombra un archivo"""
    directorio = Path(ruta_actual).parent
    nueva_ruta = directorio / nuevo_nombre
    os.rename(ruta_actual, nueva_ruta)
    return f"✅ Archivo renombrado a: {nuevo_nombre}"
# ... más herramientas para mover, buscar, etc.