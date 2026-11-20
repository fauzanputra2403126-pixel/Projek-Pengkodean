import streamlit as st
from PIL import Image
from modules.converter import load_and_preprocess_images, image_to_binary_vector
from modules.hamming import analyze_hamming_metrics

# 1. Konfigurasi Halaman Web
st.set_page_config(
    page_title="Analisis Integritas Transaksi Digital - Hamming Metrics",
    page_icon="🛡️",
    layout="wide"
)

# Header Utama
st.title("🛡️ Analisis Perubahan Biner Bukti Transaksi Digital")
st.subtitle = "Penerapan Hamming Distance & Hamming Weight untuk Pengujian Integritas Data"
st.markdown("---")

# Sidebar Informasi
with st.sidebar:
    st.header("📌 Informasi Projek")
    st.info("""
    **Metodologi:** Teori Pengkodean (Coding Theory)  
    **Metrik Utama:**  
    • Hamming Distance $d(x, y)$  
    • Hamming Weight $wt(x \oplus y)$  
    **Formulasi:** $d(x, y) = wt(x \oplus y)$
    """)
    st.write("Disusun untuk Pengujian Bukti Transaksi Digital.")

# 2. Section Unggah Berkas Gambar
col_up1, col_up2 = st.columns(2)

with col_up1:
    st.subheader("📷 1. Unggah Bukti Transaksi Asli (x)")
    file_asli = st.file_uploader("Pilih gambar asli (PNG/JPG)", type=['png', 'jpg', 'jpeg'], key="asli")

with col_up2:
    st.subheader("🧪 2. Unggah Bukti Transaksi Uji (y)")
    file_uji = st.file_uploader("Pilih gambar uji / editan (PNG/JPG)", type=['png', 'jpg', 'jpeg'], key="uji")

# 3. Eksekusi Analisis Saat Kedua Gambar Diunggah
if file_asli and file_uji:
    # Tampilkan Preview Gambar
    img_asli, img_uji = load_and_preprocess_images(file_asli, file_uji)
    
    st.markdown("### 🔍 Pratinjau Dokumen Uji")
    col_img1, col_img2 = st.columns(2)
    with col_img1:
        st.image(img_asli, caption=f"Gambar Asli ({img_asli.size[0]}x{img_asli.size[1]} px)", use_container_width=True)
    with col_img2:
        st.image(img_uji, caption=f"Gambar Uji ({img_uji.size[0]}x{img_uji.size[1]} px)", use_container_width=True)
        
    # Tombol Eksekusi Komputasi
    if st.button("🚀 Jalankan Analisis Metrik Hamming", type="primary"):
        with st.spinner("Mengonversi piksel ke vektor biner dan menghitung metrik Hamming..."):
            # Step A: Ekstraksi Vektor Biner
            vec_x = image_to_binary_vector(img_asli)
            vec_y = image_to_binary_vector(img_uji)
            
            # Step B: Hitung Metrik Hamming
            results = analyze_hamming_metrics(vec_x, vec_y)
            
        st.markdown("---")
        st.header("📊 Hasil Analisis Integritas Biner")
        
        # Display Status Badge
        if results['status'] == "VALID / ASLI":
            st.success(f"### Status: {results['status']}")
        else:
            st.error(f"### Status: {results['status']}")
            
        st.write(f"**Keterangan:** {results['description']}")
        
        # Display Metric Dashboard
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Bit (n)", f"{results['total_bits']:,}")
        m2.metric("Hamming Distance d(x, y)", f"{results['hamming_distance']:,}")
        m3.metric("Hamming Weight wt(e)", f"{results['hamming_weight']:,}")
        m4.metric("Rasio Perubahan Bit", f"{results['percentage']:.4f} %")
        
        # Verifikasi Matematika
        st.markdown("#### 📐 Verifikasi Teori Pengkodean")
        if results['is_verified']:
            st.info(f"✅ **Terbukti Mutlak:** Nilai $d(x, y)$ sama dengan $wt(x \\oplus y)$ yaitu **{results['hamming_distance']:,} bit**.")
        else:
            st.warning("⚠️ Ketidaksesuaian perhitungan matematis!")
else:
    st.warning("Silakan unggah kedua berkas bukti transaksi di atas untuk memulai analisis.")