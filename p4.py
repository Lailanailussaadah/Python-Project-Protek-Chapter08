#menu awal
namaSayur = ('bayam', 'kangkung', 'wortel', 'selada')
print('Menu : ')
A = 'A. = Tambah data sayur'
B = 'B. = Hapus data sayur'
C = 'C. = Tampilkan data sayur'
print(A)
print(B)
print(C)

#input pilihan
pilihan = input('Pilihan anda : ')
if (pilihan == 'A'):
    print(namaSayur)
    x = list(namaSayur)
    tambahan = input('Sayur yang ditambahkan : ')
    x.append(tambahan)
    x_2 = tuple(x)
    print(x_2)
elif (pilihan == 'B'):
    print(namaSayur)
    y = list(namaSayur)
    hapus = input('Sayur yang dihapus : ')
    y.remove(hapus)
    y_2 = tuple(y)
    print(y_2)
elif (pilihan == 'C'):
    print(namaSayur)
