import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.title("🧮 Kalkulator Turunan Parsial & Bidang Singgung")

# Input fungsi dan titik evaluasi
fungsi_input = st.text_input("Masukkan fungsi f(x, y):", "x**2 + y**2")
x0 = st.number_input("Masukkan nilai x₀:", value=1.0)
y0 = st.number_input("Masukkan nilai y₀:", value=1.0)

# Definisikan variabel
x, y = sp.symbols('x y')

# Proses hitung turunan parsial
fungsi = sp.sympify(fungsi_input)
fx = sp.diff(fungsi, x)
fy = sp.diff(fungsi, y)

# Nilai turunan di titik (x0, y0)
fx_val = fx.subs({x: x0, y: y0})
fy_val = fy.subs({x: x0, y: y0})

st.latex(r"f_x = " + sp.latex(fx))
st.latex(r"f_y = " + sp.latex(fy))

st.write(f"Nilai fₓ di ({x0}, {y0}) = {fx_val}")
st.write(f"Nilai fᵧ di ({x0}, {y0}) = {fy_val}")

# Grafik 3D fungsi dan bidang singgung
X_vals = np.linspace(x0-5, x0+5, 50)
Y_vals = np.linspace(y0-5, y0+5, 50)
X, Y = np.meshgrid(X_vals, Y_vals)
f_lambd = sp.lambdify((x, y), fungsi, "numpy")
Z = f_lambd(X, Y)

# Bidang singgung z = f(x0,y0) + fₓ(x0,y0)(x-x0) + fᵧ(x0,y0)(y-y0)
f0 = f_lambd(x0, y0)
Z_tangent = f0 + float(fx_val)*(X-x0) + float(fy_val)*(Y-y0)

fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, alpha=0.6, cmap='viridis')
ax.plot_surface(X, Y, Z_tangent, alpha=0.5, color='orange')
ax.scatter(x0, y0, f0, color='r', s=50)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

st.pyplot(fig)

st.write("Bidang singgung ditampilkan dalam warna oranye.")
