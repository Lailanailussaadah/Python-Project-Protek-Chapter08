def sortStringByChar(namaBuah):
    namaBuah.sort(reverse = True, key = len)
    return namaBuah
urutan = ['apel', 'rambutan', 'jeruk']
print(sortStringByChar(urutan))
