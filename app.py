import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi halaman
st.set_page_config(page_title="Wine Quality Dashboard", layout="wide")

# Judul utama
st.title("Wine Quality Analysis Dashboard")
st.markdown("Analisis interaktif terhadap dataset **Wine Quality (Red Wine)** menggunakan Streamlit.")

# Upload dataset
st.sidebar.header("Data Input")
uploaded_file = st.sidebar.file_uploader("Upload file CSV:", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("winequality-red.csv")

st.sidebar.success("Dataset berhasil dimuat.")

# Tampilkan beberapa data awal
if st.checkbox("Tampilkan Data Awal"):
    st.dataframe(df.head())

# Filter kualitas minimum
st.sidebar.header("Filter dan Parameter")
min_quality = st.sidebar.slider("Pilih kualitas minimum:", 0, 10, 5)
filtered_df = df[df["quality"] >= min_quality]

st.write(f"Data dengan kualitas minimal {min_quality}")
st.dataframe(filtered_df)

# Pilih variabel scatter plot
st.sidebar.subheader("Pilih Variabel Scatter Plot")
x_var = st.sidebar.selectbox("Sumbu X:", df.columns[:-1])
y_var = st.sidebar.selectbox("Sumbu Y:", df.columns[:-1])

# Scatter Plot
st.header("Hubungan Antar Variabel")
fig1, ax1 = plt.subplots()
sns.scatterplot(data=filtered_df, x=x_var, y=y_var, hue="quality", palette="viridis", ax=ax1)
st.pyplot(fig1)

# Checkbox distribusi alkohol
if st.checkbox("Tampilkan Distribusi Alkohol"):
    st.subheader("Distribusi Alkohol")
    fig2, ax2 = plt.subplots()
    sns.histplot(filtered_df["alcohol"], bins=15, kde=True, color="steelblue", ax=ax2)
    st.pyplot(fig2)

# Analisis statistik rata-rata
st.sidebar.subheader("Analisis Statistik")
metric = st.sidebar.selectbox("Pilih variabel:", df.columns[:-1])
avg_metric = filtered_df.groupby("quality")[metric].mean().reset_index()

# Bar Chart rata-rata
st.header(f"Rata-Rata {metric} Berdasarkan Kualitas")
st.bar_chart(data=avg_metric, x="quality", y=metric)

# Tombol insight
if st.button("Tampilkan Insight"):
    st.subheader("Insight Singkat")
    st.write(f"Jumlah data setelah filter: {len(filtered_df)} baris")
    st.write(f"Rata-rata {metric}: {filtered_df[metric].mean():.2f}")
    st.write(f"Rata-rata kualitas: {filtered_df['quality'].mean():.2f}")
    st.info("Secara umum, kualitas wine meningkat seiring dengan kadar alkohol yang lebih tinggi.")

# Footer
st.markdown("---")
st.caption("Dibuat oleh [Nama Anda] | Tugas: Building Portfolio with Streamlit")
