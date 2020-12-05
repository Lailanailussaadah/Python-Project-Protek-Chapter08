namaBuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
a = list(namaBuah)
b = list(namaBuah.values())
hitung = []
#input buah dan banyak buah yang dibeli
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
print('-------------------------')

#total buah dan banyak buah yang dibeli
hargaBeli2 = sum(hitung)
print('Total harga : ',hargaBeli2)
