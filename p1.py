while True:
    n = int(input('Masukkan berapa banyak angka yang menerima input:'))
    break
data = []
i = 0
while (i < n):
    bil = int(input('Masukkan bilangan bulat yang diinginkan:'))
    data.append(bil)
    i+=1
data.sort(reverse = True)
print(data)
