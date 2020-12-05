namaBuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
a = list(namaBuah)
b = list(namaBuah.values())
hitung = []

print('Menu :')
print('A. Tambah data buah')
print('B. Beli buah')
print('C. Hapus data buah')
pilihMenu = input('Pilihan menu : ')

if pilihMenu == 'A':
    buahBaru = input('Masukkan nama buah : ')
    if buahBaru in namaBuah :
        print('Buah sudah terdapat dalam daftar')
        buahBaru = input('Masukkan nama buah : ')
    hargaBaru = int(input('Masukkan harga satuan : '))
    namaBuah[buahBaru] = hargaBaru
    print(namaBuah)

elif pilihMenu == 'B':
    while True:
        x = input('Nama buah yang dibeli : ')
        y = int(input('Berapa Kg             : '))
        indx = a.index(x)
        hargaBeli = b[indx] * y
        hitung.append(hargaBeli)
        print('')
        tanya = input('Beli buah yang lain(y/n)? ')
        print('')
        if tanya == 'y' :
            continue
        elif tanya == 'n' :
            break
        else:
            print('Input salah')
            print('')
            tanya = input('Beli buah yang lain(y/n)? ')
            print('')
    print('--------------------------------')

    #total buah dan banyak buah yang dibeli
    hargaBeli2 = sum(hitung)
    print('Total harga : ',hargaBeli2)

elif pilihMenu == 'C':
    buahHapus = input('Masukkan nama buah : ')
    if buahHapus not in namaBuah :
        print('Nama buah tidak ditemukan')
        buahHapus = input('Masukkan nama buah : ')
    del namaBuah[buahHapus]
    print(namaBuah)
