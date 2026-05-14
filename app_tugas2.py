import streamlit as st

st.set_page_config(page_title="Rekomendasi Laptop", page_icon="💻")
st.title("💻 Sistem Rekomendasi Laptop (Rule-Based)")
st.write("Sistem pakar sederhana ini akan merekomendasikan laptop berdasarkan kebutuhan dan anggaran Anda.")

st.markdown("---")

fakta_laptop = {
    "Acer Chromebook": {
        "kategori": "Dasar",
        "harga": "Rp 3.500.000", 
        "spesifikasi": "Intel Celeron, 4GB RAM, 32GB eMMC, ChromeOS"
    },
    "Asus VivoBook 14": {
        "kategori": "Pelajar",
        "harga": "Rp 6.500.000", 
        "spesifikasi": "Intel Core i3/Ryzen 3, 8GB RAM, 512GB SSD, Windows 11"
    },
    "MacBook Air M1": {
        "kategori": "Desain/Kreator",
        "harga": "Rp 13.000.000", 
        "spesifikasi": "Apple M1 Chip, 8GB RAM, 256GB SSD, macOS"
    },
    "Lenovo Legion 5": {
        "kategori": "Gaming",
        "harga": "Rp 18.500.000", 
        "spesifikasi": "AMD Ryzen 7, RTX 3060, 16GB RAM, 512GB SSD, Windows 11"
    },
    "ThinkPad X1 Carbon": {
        "kategori": "Bisnis Premium",
        "harga": "Rp 25.000.000", 
        "spesifikasi": "Intel Core i7, 16GB RAM, 1TB SSD, Sangat Ringan & Tahan Banting"
    }
}


st.subheader("Masukkan Kriteria Anda")

kebutuhan = st.selectbox(
    "Apa kebutuhan utama Anda menggunakan laptop?", 
    [
        "Hanya Browsing & Nonton Video", 
        "Tugas Sekolah / Kuliah Umum", 
        "Desain Grafis / Editing Video", 
        "Bermain Game Berat / Render 3D", 
        "Pekerjaan Bisnis Eksekutif & Mobilitas Tinggi"
    ]
)

budget = st.selectbox(
    "Berapa batas maksimal anggaran (budget) Anda?", 
    [
        "Sangat Murah (< 5 Juta)", 
        "Murah (5 - 10 Juta)", 
        "Menengah (10 - 20 Juta)", 
        "Tinggi (> 20 Juta)"
    ]
)


if st.button("Cari Rekomendasi Laptop"):
    
    rekomendasi = None
    alasan = ""

    if kebutuhan == "Bermain Game Berat / Render 3D":
        rekomendasi = "Lenovo Legion 5"
        alasan = "Karena Anda membutuhkan laptop untuk beban berat (gaming/render), spesifikasi kartu grafis tinggi sangat mutlak diperlukan."

    elif kebutuhan == "Desain Grafis / Editing Video":
        rekomendasi = "MacBook Air M1"
        alasan = "Untuk keperluan visual dan desain, MacBook menawarkan akurasi warna layar yang sangat baik dan performa stabil untuk rendering."

    elif kebutuhan == "Pekerjaan Bisnis Eksekutif & Mobilitas Tinggi" and budget == "Tinggi (> 20 Juta)":
        rekomendasi = "ThinkPad X1 Carbon"
        alasan = "Sebagai profesional, Anda membutuhkan laptop yang tingkat keamanannya tinggi, baterai awet, dan sangat ringan untuk dibawa bepergian."
        
    elif kebutuhan == "Hanya Browsing & Nonton Video" and budget == "Sangat Murah (< 5 Juta)":
        rekomendasi = "Acer Chromebook"
        alasan = "Karena kebutuhan Anda sangat dasar dan budget terbatas, sistem ChromeOS yang ringan sudah lebih dari cukup dan cepat."

    elif kebutuhan == "Tugas Sekolah / Kuliah Umum" or budget == "Murah (5 - 10 Juta)":
        rekomendasi = "Asus VivoBook 14"
        alasan = "Laptop ini adalah pilihan standar paling masuk akal yang menawarkan rasio harga-ke-performa terbaik untuk kegiatan sehari-hari."
        
    else:
        rekomendasi = "Asus VivoBook 14"
        alasan = "Berdasarkan kombinasi pilihan Anda, laptop *all-rounder* ini adalah titik tengah paling aman untuk berbagai kebutuhan."

    st.markdown("---")
    st.success(f"🎯 **Rekomendasi Terbaik untuk Anda: {rekomendasi}**")
    st.write(f"**Alasan Sistem:** {alasan}")
    
    st.info("**💡 Data Fakta dari Knowledge Base:**")
    st.write(f"- **Kategori:** {fakta_laptop[rekomendasi]['kategori']}")
    st.write(f"- **Estimasi Harga:** {fakta_laptop[rekomendasi]['harga']}")
    st.write(f"- **Spesifikasi Utama:** {fakta_laptop[rekomendasi]['spesifikasi']}")
