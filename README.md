# 📂 FileMate AI - Estructura del Proyecto

Este documento explica la estructura del proyecto **FileMate AI**, así como el propósito de cada archivo y carpeta.

---

## 📂 Estructura del proyecto

```
📂 FileMate-AI/
 ┣ 📂 filemate-env/        # Entorno virtual (contiene binarios, librerías, dependencias)
 ┣ 📜 agent.py             # Configuración del modelo Gemma (LLM)
 ┣ 📜 agente.py            # Inicialización del agente con el LLM y las herramientas
 ┣ 📜 herramientas.py      # Funciones utilitarias (convertir, renombrar, mover archivos, etc.)
 ┣ 📜 app.py               # Interfaz principal con Streamlit
 ┣ 📜 requirements.txt     # Dependencias del proyecto
 ┗ 📜 README.md            # Documentación básica del proyecto
```

---

## 📄 Explicación de cada archivo

### 📂 `filemate-env/`
- Carpeta del **entorno virtual de Python** creado con `python -m venv filemate-env`.
- Contiene todas las librerías y dependencias instaladas con `pip install ...`.
- **No se modifica manualmente**. VS Code detecta este entorno y lo usa para ejecutar tu proyecto.  

---

### 📜 `agent.py`
- Se encarga de **cargar y preparar el modelo de lenguaje (LLM)** que se usará en LangChain.
- Define el modelo **Gemma** (Google) usando HuggingFace y lo encapsula con `HuggingFacePipeline`.
- Expone la variable `llm` que luego se importa en otros archivos.

---

### 📜 `agente.py`
- **Inicializa el agente de LangChain**.
- Importa el modelo (`llm`) desde `agent.py` y define las **herramientas** disponibles.
- Usa `initialize_agent()` con enfoque **"zero-shot-react-description"**.
- Permite interpretar instrucciones en español y decidir qué herramienta ejecutar.

---

### 📜 `herramientas.py`
- Contiene las **funciones utilitarias** que el agente puede ejecutar como "herramientas".
- Ejemplos:
  - `convertir_word_a_pdf`: convierte documentos `.docx` a `.pdf`.
  - `renombrar_archivo`: cambia el nombre de un archivo en el sistema.
- Se pueden agregar más funciones (mover archivos, listar archivos, buscar texto, etc.).

---

### 📜 `app.py`
- Es la **interfaz con Streamlit**.
- Muestra un campo de texto donde el usuario escribe comandos en español.
- Envía el comando al agente (`agente.run(comando)`) y muestra la respuesta o errores.
- Se ejecuta con:
  ```bash
  streamlit run app.py
  ```

---

### 📜 `requirements.txt`
- Lista todas las dependencias necesarias para el proyecto.
- Ejemplo de librerías:
  ```
  streamlit
  langchain
  transformers
  torch
  docx2pdf
  pillow
  ```
- Se instalan con:
  ```bash
  pip install -r requirements.txt
  ```

---

### 📜 `README.md`
- Documentación general del proyecto.
- Explica qué es **FileMate AI**, cómo instalarlo, cómo ejecutarlo y qué funcionalidades tiene.
- Útil si compartes el proyecto en GitHub o con colegas.

---
