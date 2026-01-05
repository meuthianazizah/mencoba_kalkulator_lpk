import streamlit as st

st.set_page_config(
    page_title="Kalkulator Timbangan Zat Kimia",
    layout="centered"
)

# Judul Web
st.title("🧪 Kalkulator Timbangan Zat Kimia")
st.write(
    "Aplikasi ini digunakan untuk menghitung **massa bahan kimia (gram)** "
    "yang harus ditimbang untuk memperoleh **konsentrasi larutan tertentu**."
)

st.divider()

# Input pengguna
nama_zat = st.text_input("Nama zat kimia (opsional)")

mr = st.number_input(
    "Massa Molekul Relatif (Mr) (g/mol)",
    min_value=0.0,
    step=0.01
)

konsentrasi = st.number_input(
    "Konsentrasi larutan (M)",
    min_value=0.0,
    step=0.001
)

volume_ml = st.number_input(
    "Volume larutan (mL)",
    min_value=0.0,
    step=1.0
)

# Tombol hitung
if st.button("Hitung Bobot Timbangan"):
    if mr == 0 or konsentrasi == 0 or volume_ml == 0:
        st.warning("⚠️ Semua nilai harus lebih dari 0")
    else:
        volume_l = volume_ml / 1000  # konversi mL ke L
        mol = konsentrasi * volume_l
        massa = mol * mr

        st.success("✅ Perhitungan Berhasil")

        if nama_zat:
            st.write(f"**Zat kimia:** {nama_zat}")

        st.write(f"**Jumlah mol (n):** `{mol:.4f} mol`")
        st.write(
            f"**Bobot yang harus ditimbang:** "
            f"`{massa:.4f} gram`"
        )

st.divider()
st.caption("Web Praktikum Kimia – Perhitungan Bobot Zat Berdasarkan Konsentrasi")
