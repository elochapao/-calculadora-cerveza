import streamlit as st

st.set_page_config(page_title="Calculadora de Consumo de Cerveza", layout="centered")

st.title("🍻 Calculadora de Cerveza en la Arena Monterrey")
st.markdown("Estima el consumo total de cerveza en un concierto promedio basado en tus propios supuestos.")

# Entradas del usuario
capacidad_total = st.number_input("Capacidad total de la Arena", value=17600)

porcentaje_ocupacion = st.slider("Porcentaje de ocupación", 0, 100, 85)
porcentaje_consumidores = st.slider("Porcentaje que consume cerveza", 0, 100, 70)
vasos_por_persona = st.number_input("Vasos por persona", value=6.0)
ml_por_botella = st.number_input("Mililitros por botella", value=355)
botellas_por_vaso = st.number_input("Botellas por vaso", value=2.0)

# Cálculos
asistentes = capacidad_total * (porcentaje_ocupacion / 100)
consumidores = asistentes * (porcentaje_consumidores / 100)
total_vasos = consumidores * vasos_por_persona
ml_por_vaso = ml_por_botella * botellas_por_vaso
total_ml = total_vasos * ml_por_vaso

# Resultados
st.subheader("📊 Resultado estimado:")
st.write(f"**Asistentes estimados:** {asistentes:,.0f}")
st.write(f"**Personas que consumen cerveza:** {consumidores:,.0f}")
st.write(f"**Total de vasos servidos:** {total_vasos:,.0f}")
st.write(f"**Mililitros por vaso:** {ml_por_vaso:.0f} ml")
st.write(f"**➡️ TOTAL: {total_ml:,.0f} ml** de cerveza consumida")
