# Casting Tipe Data dlm Python
# Casting digunakan buat mengubah tipe data  1ke tipe data lain
# Contoh --> ubah int jadi string, atau list menjadi tuple

# Int ke Float
angka_bulat = 10
angka_float = float(angka_bulat)  # Mubah int ke float
print("Integer ke Float:", angka_float)

# Float ke Int
angka_desimal = 3.14
angka_bulat_kembali = int(angka_desimal)  #ubah float ke int
print("Float ke Integer:", angka_bulat_kembali)

# Int ke String
angka_bulat = 100
angka_string = str(angka_bulat)  #ubah int ke string
print("Integer ke String:", angka_string)

# String ke Int
angka_dalam_teks = "50"
angka_asli = int(angka_dalam_teks)  # Mengubah string ke int
print("String ke Integer:", angka_asli)

# String ke Float
angka_dalam_teks_float = "3.14"
angka_float_asli = float(angka_dalam_teks_float)  # Mengubah string to float
print("String ke Float:", angka_float_asli)

# List ke Tuple
daftar = [1, 2, 3]
tuple_baru = tuple(daftar)  # Mengubah list ke tuple
print("List ke Tuple:", tuple_baru)

# Tuple ke List
tuple_asli = (4, 5, 6)
list_baru = list(tuple_asli)  # Mengubah tuple ke list
print("Tuple ke List:", list_baru)

# String ke List
text = "Python"
list_text = list(text)  # Mengubah string ke list
print("String ke List:", list_text)

# Set ke List
kumpulan = {1, 2, 3}
list_dari_set = list(kumpulan)  # Mengubah set ke list
print("Set ke List:", list_dari_set)

# Menggunakan Boolean
nilai_benar = bool(1)  # 1  True
nilai_salah = bool(0)  # 0 False
print("1 ke Boolean:", nilai_benar)
print("0 ke Boolean:", nilai_salah)
