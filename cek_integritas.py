import hashlib

# Fungsi untuk menghitung hash file
def hitung_hash(nama_file):

    # Membuat objek hash
    md5_hash = hashlib.md5()
    sha256_hash = hashlib.sha256()

    # Membaca file dalam mode binary
    with open(nama_file, "rb") as file:

        # Membaca file per 4096 byte
        while chunk := file.read(4096):

            # Update hash MD5
            md5_hash.update(chunk)

            # Update hash SHA-256
            sha256_hash.update(chunk)

    # Mengembalikan hasil hash
    return md5_hash.hexdigest(), sha256_hash.hexdigest()


# Nama file
file_asli = "file_asli.txt"
file_modifikasi = "file_modifikasi.txt"

# Menghitung hash file asli
md5_asli, sha256_asli = hitung_hash(file_asli)

# Menghitung hash file modifikasi
md5_mod, sha256_mod = hitung_hash(file_modifikasi)

# Menampilkan hasil hash
print("===== FILE ASLI =====")
print("MD5      :", md5_asli)
print("SHA-256  :", sha256_asli)

print("\n===== FILE MODIFIKASI =====")
print("MD5      :", md5_mod)
print("SHA-256  :", sha256_mod)

# Membandingkan hash
print("\n===== HASIL PERBANDINGAN =====")

if md5_asli == md5_mod:
    print("MD5      : File tidak berubah")
else:
    print("MD5      : File telah dimodifikasi")

if sha256_asli == sha256_mod:
    print("SHA-256  : File tidak berubah")
else:
    print("SHA-256  : File telah dimodifikasi")