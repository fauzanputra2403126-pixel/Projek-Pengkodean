import numpy as np
from PIL import Image
import io

def load_and_preprocess_images(image_file_asli, image_file_uji, target_mode='RGB'):
    """
    Membaca dua file gambar, menyamakan mode warna dan ukurannya 
    berdasarkan dimensi gambar asli.
    """
    # 1. Buka citra menggunakan PIL
    img_asli = Image.open(image_file_asli).convert(target_mode)
    img_uji = Image.open(image_file_uji).convert(target_mode)
    
    # 2. Samakan ukuran dimensi citra uji sesuai citra asli (jika berbeda)
    if img_asli.size != img_uji.size:
        img_uji = img_uji.resize(img_asli.size, Image.Resampling.LANCZOS)
        
    return img_asli, img_uji

def image_to_binary_vector(pil_image):
    """
    Mengonversi setiap piksel gambar menjadi deretan vektor biner (0 dan 1).
    Menggunakan np.unpackbits untuk efisiensi komputasi bit-level.
    """
    # Konversi gambar ke numpy array uint8 (rentang piksel 0 - 255)
    img_np = np.array(pil_image, dtype=np.uint8)
    
    # Ratakan array (flatten) menjadi 1 dimensi
    flat_pixels = img_np.flatten()
    
    # Unpack setiap nilai desimal uint8 menjadi 8 bit biner (vektor berdimensi n)
    binary_vector = np.unpackbits(flat_pixels)
    
    return binary_vector