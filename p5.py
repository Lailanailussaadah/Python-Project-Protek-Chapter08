def kuadrat(bil):
    hasil = []
    for i in range (len(bil)):
        hitung = bil[i]**2
        hasil = hasil + [hitung]
    return hasil
bil = [2, 5, 6, 4]
print(kuadrat(bil))
