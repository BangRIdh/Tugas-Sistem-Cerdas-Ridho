import streamlit as st
import datetime

# Mengatur judul halaman
st.title("🏨 Sistem Reservasi Hotel Sederhana")
st.write("Selamat datang! Silakan lengkapi formulir di bawah ini untuk memesan kamar Anda.")

# Membuat form untuk input data
with st.form("form_reservasi"):
    st.subheader("Data Diri & Detail Pesanan")
    
    # Input Nama
    nama = st.text_input("Nama Lengkap")
    
    # Input Tanggal (Check-in dan Check-out)
    hari_ini = datetime.date.today()
    besok = hari_ini + datetime.timedelta(days=1)
    
    col1, col2 = st.columns(2)
    with col1:
        check_in = st.date_input("Tanggal Check-in", min_value=hari_ini)
    with col2:
        check_out = st.date_input("Tanggal Check-out", min_value=besok)
        
    # Input Pilihan Kamar dan Jumlah Tamu
    tipe_kamar = st.selectbox(
        "Pilih Tipe Kamar",
        ["Standard Room", "Deluxe Room", "Family Suite", "Presidential Suite"]
    )
    
    jumlah_tamu = st.number_input("Jumlah Tamu", min_value=1, max_value=10, value=1)
    
    # Input Permintaan Khusus
    catatan = st.text_area("Permintaan Khusus (Opsional)", placeholder="Contoh: Minta kamar di lantai atas, alergi debu, dll.")
    
    # Tombol Submit
    submit_button = st.form_submit_button(label="Buat Reservasi")

# Logika ketika tombol submit ditekan
if submit_button:
    # Validasi sederhana
    if not nama:
        st.error("Mohon isi Nama Lengkap Anda terlebih dahulu.")
    elif check_out <= check_in:
        st.error("Tanggal Check-out harus setelah tanggal Check-in.")
    else:
        # Menampilkan pesan sukses dan detail reservasi
        st.success(f"🎉 Reservasi Berhasil, {nama}!")
        st.write("---")
        st.write("### Detail Reservasi Anda:")
        st.write(f"**Tipe Kamar:** {tipe_kamar}")
        st.write(f"**Tanggal Check-in:** {check_in.strftime('%d %B %Y')}")
        st.write(f"**Tanggal Check-out:** {check_out.strftime('%d %B %Y')}")
        st.write(f"**Jumlah Tamu:** {jumlah_tamu} Orang")
        
        if catatan:
            st.write(f"**Catatan Khusus:** {catatan}")
        
        st.info("Kuitansi dan detail pembayaran akan dikirimkan ke email Anda saat check-in.")
