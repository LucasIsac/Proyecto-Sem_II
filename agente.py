from agent import llm

from langchain.agents import initialize_agent, Tool
from herramientas import convertir_word_a_pdf, renombrar_archivo
# ... (código de carga de Gemma 3 del Paso 2)

# Definir las herramientas que el agente puede usar
herramientas = [
    Tool(
        name="ConvertidorPDF",
        func=convertir_word_a_pdf,
        description="Útil para convertir un documento de Microsoft Word (.docx) a formato PDF. La entrada debe ser la ruta al archivo .docx."
    ),
    Tool(
        name="Renombrador",
        func=renombrar_archivo,
        description="Útil para cambiar el nombre de un archivo. La entrada debe ser la ruta actual del archivo y el nuevo nombre deseado."
    ),
]

# Inicializar el agente
agente = initialize_agent(
    tools=herramientas,
    llm=llm, # Gemma 3
    agent="zero-shot-react-description",
    verbose=True,
    handle_parsing_errors=True
)