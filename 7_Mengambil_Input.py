#Mengambil input sebagai string
nama = input("Masukkan nama You: ")  
print("Halo,", nama) #/\_/\

#Mengambil input sebagai integer
usia = int(input("Masukkan age Anda: "))  
print("Usia Anda adalah:", usia)

#ambil input sebagai float
tinggi = float(input("Masukkan tinggi badan Anda (gawe cm): "))  
print("Tinggi badan Anda adalah:", tinggi, "cm")

#   input boolean
jawaban = input("Apakah Anda menyukai Python? (ya/tidak): ")  
menyukai_python = (jawaban.lower() == "ya")  
print("Menyukai Python:", menyukai_python)

daftar_angka = input("Masukkan beberapa angka yang dipisahkan dengan koma: ")  # Input berupa teks
list_angka = daftar_angka.split(",")  # Memisahkan string menjadi list berdasarkan koma
print("Daftar angka Anda:", list_angka)

# Mengubah elemen dalam list menjadi integer
list_angka_int = [int(angka) for angka in list_angka]  
print("Daftar angka dalam bentuk integer:", list_angka_int)
