
import streamlit as st                  # Untuk membuat antarmuka aplikasi web
import sympy as sp                     # Untuk komputasi simbolik (aljabar, turunan)
import numpy as np                     # Untuk komputasi numerik dan array/grid
import matplotlib.pyplot as plt        # Untuk membuat grafik 3D

# Judul utama aplikasi
st.title("🧮 Aplikasi Turunan Parsial")

# Definisi simbol-simbol variabel simbolik
x, y = sp.symbols('x y')

# Input teks dari pengguna untuk fungsi dua variabel f(x, y)
fungsi_str = st.text_input("Masukkan fungsi f(x, y):", "x**2 * y + y**3")

try:
    # Konversi string input menjadi ekspresi simbolik
    f = sp.sympify(fungsi_str)

    # Hitung turunan parsial terhadap x dan y
    fx = sp.diff(f, x)
    fy = sp.diff(f, y)

    # Tampilkan fungsi dan turunannya dalam format matematika (LaTeX)
    st.latex(f"f(x, y) = {sp.latex(f)}")
    st.latex(f"\\frac{{\\partial f}}{{\\partial x}} = {sp.latex(fx)}")
    st.latex(f"\\frac{{\\partial f}}{{\\partial y}} = {sp.latex(fy)}")

    # Input nilai titik evaluasi dari pengguna
    x0 = st.number_input("Nilai x₀:", value=1.0)
    y0 = st.number_input("Nilai y₀:", value=2.0)

    # Evaluasi nilai fungsi dan turunannya di titik (x₀, y₀)
    f_val = f.subs({x: x0, y: y0})        # Nilai fungsi
    fx_val = fx.subs({x: x0, y: y0})      # Nilai turunan parsial ∂f/∂x
    fy_val = fy.subs({x: x0, y: y0})      # Nilai turunan parsial ∂f/∂y

    # Tampilkan hasil evaluasi
    st.write("Nilai fungsi di titik (x₀, y₀):", f_val)
    st.write("Gradien di titik (x₀, y₀):", f"({fx_val}, {fy_val})")

    # Subjudul untuk visualisasi grafik
    st.subheader("📈 Grafik Permukaan & Bidang Singgung")

    # Buat grid nilai x dan y di sekitar titik (x₀, y₀)
    x_vals = np.linspace(x0 - 2, x0 + 2, 50)    # Range nilai x
    y_vals = np.linspace(y0 - 2, y0 + 2, 50)    # Range nilai y
    X, Y = np.meshgrid(x_vals, y_vals)         # Buat grid 2D

    # Hitung nilai fungsi f(x, y) di grid X, Y
    Z = sp.lambdify((x, y), f, 'numpy')(X, Y)

    # Hitung bidang singgung pada titik (x₀, y₀):
    # z = f(x₀, y₀) + fx(x₀, y₀)*(x - x₀) + fy(x₀, y₀)*(y - y₀)
    Z_tangent = float(f_val) + float(fx_val)*(X - x0) + float(fy_val)*(Y - y0)

    # Buat figure untuk plot 3D
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Plot permukaan fungsi f(x, y)
    ax.plot_surface(X, Y, Z, alpha=0.7, cmap='viridis')

    # Plot bidang singgung di titik (x₀, y₀)
    ax.plot_surface(X, Y, Z_tangent, alpha=0.5, color='red')

    # Atur label dan judul grafik
    ax.set_title("Permukaan f(x, y) dan bidang singgungnya")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # Tampilkan plot di aplikasi Streamlit
    st.pyplot(fig)

# Jika terjadi kesalahan (misalnya fungsi tidak valid), tampilkan pesan error
except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
