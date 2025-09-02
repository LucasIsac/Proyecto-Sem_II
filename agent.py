from langchain.llms import HuggingFacePipeline
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

# Reemplaza 'google/gemma-3-5b-it' con el identificador correcto del modelo
model_id = "google/gemma-2b"

# Cargar el tokenizador y el modelo
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

# Crear el pipeline de generación de texto
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=128
)

# Encapsular en LangChain
llm = HuggingFacePipeline(pipeline=pipe)