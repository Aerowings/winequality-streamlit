# Wine Quality Dashboard (Streamlit)

Aplikasi interaktif untuk menganalisis dataset Wine Quality (Red Wine) menggunakan Streamlit.

## Fitur
- Filter data berdasarkan kualitas wine.
- Pilih variabel X dan Y untuk scatter plot interaktif.
- Tampilkan distribusi alkohol secara opsional.
- Visualisasi rata-rata metrik berdasarkan kualitas.
- Insight sederhana berdasarkan input pengguna.

## Komponen Streamlit yang digunakan
- st.sidebar.file_uploader
- st.sidebar.slider
- st.sidebar.selectbox
- st.checkbox
- st.button
- st.bar_chart
- st.pyplot

## Cara Menjalankan
```
pip install -r requirements.txt
streamlit run app.py
```

## Dataset
Gunakan file `winequality-red.csv` dari UCI Machine Learning Repository.

## Deployment
- GitHub Repository:https://github.com/Aerowings/winequality-streamlit
- Streamlit App: https://winequality-app-wqn7mvgwmxyqgfmuzueiez.streamlit.app/
