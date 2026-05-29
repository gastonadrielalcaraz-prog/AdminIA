import streamlit as st

# CONFIGURACIÓN
st.set_page_config(
    page_title="AdminIA",
    page_icon="🤖",
    layout="centered"
)

# TÍTULO
st.title("🤖 AdminIA")
st.subheader("Asistente Inteligente para Gestión Administrativa")

# DESCRIPCIÓN
st.write("""
AdminIA permite generar notas administrativas formales utilizando Inteligencia Artificial.
El usuario ingresa información básica y la aplicación genera automáticamente un documento profesional.
""")

# ENTRADA DEL USUARIO
texto_usuario = st.text_area(
    "Ingrese la información para redactar la nota:",
    height=200
)

# BOTÓN
if st.button("Generar Nota"):

    if texto_usuario:

        resultado = f"""
San Luis, Argentina

Por medio de la presente, se solicita la adquisición de computadoras destinadas al área administrativa, con el objetivo de optimizar las tareas operativas y mejorar el rendimiento del personal.

Detalle ingresado por el usuario:
{texto_usuario}

La incorporación de nuevos recursos permitirá agilizar procesos internos y mejorar la eficiencia administrativa.

Sin otro particular, saludo atentamente.
"""

        st.subheader("📄 Nota Generada")
        st.write(resultado)

    else:
        st.warning("Por favor, ingrese información.")

# CÓMO FUNCIONA
st.markdown("---")

st.header("ℹ️ Cómo funciona")

st.write("""
1. El usuario ingresa información administrativa.
2. La aplicación analiza el contenido ingresado.
3. Se genera automáticamente una nota formal profesional.
4. El resultado puede utilizarse en expedientes o documentación institucional.
""")

# FOOTER
st.markdown("---")
st.caption("Proyecto Final - Aplicación Web con IA")