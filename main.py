import streamlit as st
import pandas as pd
import openpyxl
from PIL import Image
import webbrowser

def save_to_database(materi):
    # Fungsi ini menyimpan materi ke dalam database
    df = pd.read_excel('database_pengetahuan.xlsx')
    df = df._append({'Materi': materi}, ignore_index=True)
    df.to_excel('database_pengetahuan.xlsx', index=False)

def save_to_database_gambar(gambar, konteks):
    df = pd.read_excel('database_pengetahuan.xlsx')
    df = df._append({'Gambar': gambar, 'Konteks': konteks},ignore_index=True)
    df.to_excel('database_pengetahuan.xlsx', index=False)
    

def search_in_database(keyword):
    # Fungsi ini mencari kata kunci dalam database
    df = pd.read_excel('database_pengetahuan.xlsx') 
    result_df = df[df['Materi'].str.contains(keyword, case=False,na=False)]
    return result_df

def search_in_database_gambar(keyword):
    df = pd.read_excel('database_pengetahuan.xlsx')
    result_df = df[df['Konteks'].str.contains(keyword, case=False,na=False)]
    return result_df


# Tampilan halaman web
st.title("Aplikasi Database Pengetahuan")


# Input untuk mencari kata kunci dalam database
keyword_input = st.text_input("Cari Kata atau Kalimat:")
if st.button("Cari"):
    search_result = search_in_database(keyword_input)
    search_result1 = search_in_database_gambar(keyword_input)
    if not search_result.empty:
        st.table(search_result)
    else:
        st.warning("Tidak ada hasil untuk kata kunci tersebut.")
    if not search_result1.empty:

        for index, row in search_result1.iterrows():
            st.image(row['Gambar'],caption=row['Konteks'])
    else:
        st.warning("Tidak ada hasil gambar kata kunci tersebut.")


if st.button("Cari di Google"):
    google_search_url = "https://www.google.com/search?q=" + keyword_input
    webbrowser.open_new_tab(google_search_url)

if st.button("Cari di ChatGPT"):
    google_search_url = "https://chat.openai.com/" + keyword_input
    webbrowser.open_new_tab(google_search_url)

st.subheader("Upload Materi Teks")
# Input untuk menambahkan materi ke database
materi_input = st.text_area("Masukkan Materi:")
if st.button("Simpan"):
    save_to_database(materi_input)
    st.success("Materi berhasil disimpan!")


st.subheader("Upload Materi Gambar")
    # Input untuk upload gambar
konteks_input = st.text_area("Konteks Gambar:")

gambar_upload = st.file_uploader("Upload Gambar", type=["jpg", "jpeg", "png"])
# Tombol untuk menyimpan gambar dan konteks ke dalam database
if gambar_upload is not None:



    judul = st.text_input('Judul Gambar')
    st.image(gambar_upload)
           
    if st.button("Simpan Gambar"):
        img_PIL = Image.open(gambar_upload)
        path = "{}.png".format(judul)
        img_PIL.save(r'{}'.format(path))
        save_to_database_gambar(path, konteks_input)
        st.success("Data berhasil disimpan!")
