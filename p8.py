namaBuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
def rerata_harga(namaBuah):
    hasil = []
    for i in namaBuah :
        rata2 = list(namaBuah.values())
        average = sum(rata2) / len(rata2)
        hasil = [average]
    return hasil
print(rerata_harga(namaBuah))
