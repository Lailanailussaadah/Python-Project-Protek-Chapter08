namaBuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
a = list(namaBuah)
b = list(namaBuah.values())
hitung = []

print('Menu :')
print('A. Tambah data buah')
print('B. Beli buah')

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
    print('---------------------------------')

    #HITUNG TOTAL YANG DIBELI
    hargaBeli2 = sum(hitung)
    print('Total harga           : ',hargaBeli2)
