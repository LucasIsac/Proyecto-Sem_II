import streamlit as st
from agente import agente

st.set_page_config(page_title="FileMate AI", page_icon="🤖")
st.title("FileMate AI 🤖")
st.write("Tu asistente para gestionar archivos. ¡Háblale en español!")

comando = st.text_input("¿Qué necesitas hacer?")
if comando:
    with st.spinner('Pensando...'):
        try:
            respuesta = agente.run(comando)
            st.success(respuesta)
        except Exception as e:
            st.error(f"Oops, algo salió mal: {e}")