
data = "ini adalah string"
print(data)
print(type(data))

# 1. cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Apalah?"')
print("'Tes bang'")
print("ini adalah hari Selasa 12/31/2024")

# 2. Menggunakan tanda \

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\Hikari Reiziq")

# tab
print("Hikari\t\t\totong, semakin jauhan")

# backspace
print("Hikari \botong, jadi deketan")

# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR -> carriage return -> commodore, acorn, lisp 
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> dipakai oleh windows

# 3. String literal atau raw

# hati-hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Hikari
Kelas : 13 SMA   
""")

# multiline literal string dan RAW
print(r"""
Nama : Hikari
Kelas : 13 SMA\new normal 
Website : www.Hikari.com/newID
""")