jawab = 'ya'
i = 0
while True :
    i += 1
    x = input('Nama Mahasiswa : ')
    mylist = list(x)
    print(x, '(', len(mylist), 'karakter)')
    tanya = input('Apakah ingin input nama lagi? (ya/tidak) :')
    if (tanya == 'tidak'):
        break
 
