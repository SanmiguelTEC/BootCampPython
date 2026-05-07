import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Práctica Evaluada: Ecuaciones Cuadráticas")

st.markdown("""
Esta práctica permite:
- Visualizar **cambios dinámicos** en una parábola
- Identificar **raíces y vértice**
- Analizar el efecto de los coeficientes
""")

# =====================================================
# INPUTS DINÁMICOS (ANIMACIÓN)
# =====================================================
st.subheader("Coeficientes dinámicos")

cols = st.columns(3)
coeficientes = []

for i, col in enumerate(cols):
    with col:
        st.markdown(f"### Caso {i+1}")
        a = st.slider(f"a{i+1}", -5.0, 5.0, 1.0, 0.1)
        b = st.slider(f"b{i+1}", -10.0, 10.0, 0.0, 0.5)
        c = st.slider(f"c{i+1}", -10.0, 10.0, 0.0, 0.5)
        coeficientes.append((a, b, c))

x = np.linspace(-10, 10, 400)
graficas = st.columns(3)
colores = ["blue", "green", "red"]

# =====================================================
# GRÁFICAS CON VÉRTICE Y RAÍCES
# =====================================================
for i, (a, b, c) in enumerate(coeficientes):
    y = a*x**2 + b*x + c
    d = b**2 - 4*a*c

    fig, ax = plt.subplots()
    ax.plot(x, y, color=colores[i], label="Parábola")
    ax.axhline(0, color="black", linestyle="--")
    ax.axvline(0, color="black", linestyle="--")

    if a != 0:
        xv = -b / (2*a)
        yv = a*xv**2 + b*xv + c
        ax.scatter(xv, yv, color="purple", label="Vértice", zorder=5)

        if d >= 0:
            x1 = (-b + np.sqrt(d)) / (2*a)
            x2 = (-b - np.sqrt(d)) / (2*a)
            ax.scatter([x1, x2], [0, 0], color="orange", label="Raíces", zorder=5)

    ax.set_title(f"Caso {i+1}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    ax.grid(True)

    with graficasst.pyplot(fig)
        st.markdown("""
**1️⃣ ¿Qué determina si la parábola abre hacia arriba o hacia abajo?**  
→ El coeficiente **a**  
- a > 0 → abre hacia arriba  
- a < 0 → abre hacia abajo

**2️⃣ ¿Qué representan x₁ y x₂?**  
→ Son las **intersecciones con el eje X**, es decir, las **soluciones reales**.

**3️⃣ ¿Qué representa el vértice?**  
→ Es el **máximo o mínimo** de la función cuadrática.
""")

# =====================================================
# PRÁCTICA EVALUABLE
# =====================================================
st.divider()
st.header("📝 Práctica evaluable")

puntaje = 0

r1 = st.radio(
    "1. ¿Qué coeficiente controla la concavidad de la parábola?",
    ["b", "c", "a"]
)
if r1 == "a":
    puntaje += 1

r2 = st.radio(
    "2. El vértice de una parábola representa:",
    ["Las raíces", "El máximo o mínimo", "El corte con Y"]
)
if r2 == "El máximo o mínimo":
    puntaje += 1

r3 = st.radio(
    "3. Si el discriminante es negativo, entonces:",
    [
        "Hay dos soluciones reales",
        "Hay una solución real",
        "No hay soluciones reales"
    ]
)
if r3 == "No hay soluciones reales":
    puntaje += 1

if st.button("Evaluar"):
    st.success(f"✅ Puntaje obtenido: {puntaje}/3")

    if puntaje == 3:
        st.balloons()
        st.markdown("🎉 **Excelente dominio del tema**")
    elif puntaje == 2:
        st.markdown("👍 Buen trabajo, revisa un poco más")
    else:
        st.markdown("📘 Te recomiendo repasar conceptos básicos")
