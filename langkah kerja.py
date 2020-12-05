#membuat list a dan b
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print(a)
print(b)

#menyisipkan nilai ke dalam indeks
a. insert(3, 10)
b. insert(2, 15)
print(a)
print(b)

#menyisipkan nilai ke dalam indeks
a. append(4)
b. append(8)
print(a)
print(b)

#melakukan sorting secara ascending
a. sort()
b. sort()
print(a)
print(b)

#membuat list c dan d
c = a[0:7]
d = b[2:9]
print(c)
print(d)

#membuat list e
e = []
for i in range(len(c)):
    baru = c[i]+d[i]
    e = e+ [baru]
print(e)

#mengubah list kedalam tuple
e = tuple(e)
print(e)

#mencari nilai min, max dan jumlahan 
print(min (e), max (e), sum (e))


#membuat string
myString = "python adalah bahasa pemrograman yang menyenangkan"

#mengetahui karakter huruf yang menyusun string
karakter = set(myString)
print(karakter)

#mengurutkan alphabet
myList=list(karakter)
myList.sort()
print(myList)
