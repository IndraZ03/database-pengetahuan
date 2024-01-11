import streamlit as st
from PIL import Image

def main():
    st.title("Aplikasi Pengunggah dan Penampil Gambar")

    # Upload gambar melalui widget
    uploaded_image = st.file_uploader("Pilih sebuah gambar", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Menampilkan gambar yang diunggah
        st.image(uploaded_image, caption="Gambar yang diunggah", use_column_width=True)

        # Menambahkan beberapa manipulasi gambar jika diperlukan
        st.subheader("Manipulasi Gambar:")
        if st.button("Tampilkan Gambar Terbalik"):
            flipped_image = Image.open(uploaded_image).transpose(Image.FLIP_LEFT_RIGHT)
            st.image(flipped_image, caption="Gambar Terbalik", use_column_width=True)

if __name__ == "__main__":
    main()
