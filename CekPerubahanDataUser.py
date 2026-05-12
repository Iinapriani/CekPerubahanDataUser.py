import hashlib

# Fungsi membuat hash MD5
def buat_hash_md5(nama, email, no_hp):

    data_user = nama + email + no_hp

    # Membuat hash MD5
    hash_md5 = hashlib.md5(data_user.encode())

    return hash_md5.hexdigest()


print("=== PROGRAM CEK PERUBAHAN DATA PROFIL USER ===")

try:

    # Input data awal
    print("\nMasukkan Data User Awal")

    nama_awal = input("Nama  : ")
    email_awal = input("Email : ")
    no_hp_awal = input("No HP : ")

    # Membuat hash awal
    hash_awal = buat_hash_md5(nama_awal, email_awal, no_hp_awal)

    print("\n=== HASH DATA AWAL ===")
    print("Nama  :", nama_awal)
    print("Email :", email_awal)
    print("No HP :", no_hp_awal)
    print("Hash MD5 Awal :", hash_awal)

    # Input data baru
    print("\nMasukkan Data User Baru")

    nama_baru = input("Nama  : ")
    email_baru = input("Email : ")
    no_hp_baru = input("No HP : ")

    # Membuat hash baru
    hash_baru = buat_hash_md5(nama_baru, email_baru, no_hp_baru)

    print("\n=== HASIL PERBANDINGAN DATA ===")
    print("Hash MD5 Lama :", hash_awal)
    print("Hash MD5 Baru :", hash_baru)

    # Membandingkan hash
    if hash_awal == hash_baru:
        print("Status : Data profil tidak berubah")
    else:
        print("Status : Data profil telah berubah atau dimodifikasi")

except Exception as e:
    print("Terjadi kesalahan :", e)