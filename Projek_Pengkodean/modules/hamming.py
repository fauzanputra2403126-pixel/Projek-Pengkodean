import numpy as np

def analyze_hamming_metrics(vector_x, vector_y):
    """
    Menghitung XOR, Hamming Weight, Hamming Distance, 
    persentase perubahan, serta status keaslian bukti transaksi.
    """
    # 1. Validasi dimensi vektor
    n = len(vector_x)
    if len(vector_y) != n:
        raise ValueError("Dimensi kedua vektor biner harus persis sama!")
    
    # 2. Operasi Biner XOR: e = x XOR y
    error_vector = np.bitwise_xor(vector_x, vector_y)
    
    # 3. Perhitungan Hamming Weight: wt(e) = sum(e)
    hamming_weight = int(np.sum(error_vector))
    
    # 4. Perhitungan Hamming Distance: d(x, y) = count(x != y)
    hamming_distance = int(np.count_nonzero(vector_x != vector_y))
    
    # 5. Verifikasi hubungan matematis: d(x, y) == wt(e)
    is_verified = (hamming_distance == hamming_weight)
    
    # 6. Menghitung persentase perubahan bit
    bit_change_percentage = (hamming_distance / n) * 100
    
    # 7. Penentuan Status Integritas
    if hamming_distance == 0:
        status = "VALID / ASLI"
        description = "Integritas dokumen utuh 100%. Tidak terdeteksi adanya pembalikan bit (bit flipping)."
    else:
        status = "TERINDIKASI MANIPULASI"
        description = f"Terdeteksi pembalikan bit biner pada {hamming_distance:,} posisi. Integritas dokumen terganggu."
        
    return {
        'total_bits': n,
        'hamming_distance': hamming_distance,
        'hamming_weight': hamming_weight,
        'is_verified': is_verified,
        'percentage': bit_change_percentage,
        'status': status,
        'description': description,
        'error_vector': error_vector
    }