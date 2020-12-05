namaBuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
a = list(namaBuah)
b = list(namaBuah.values())

#input buah dan banyak buah yang dibeli
x = input('Nama buah yang dibeli : ')
y = int(input('Berapa Kg : '))
print('--------------------------')

#total buah dan banyak buah yang dibeli
indx = a.index(x)
hargaBeli = b[indx] * y
print('Total harga : ',hargaBeli)
