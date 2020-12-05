def dataStat(x):
    hasil = []
    for i in x :
        myList = list(x)
        a = sum(myList)/len(myList)
        b = max(myList)
        c = min(myList)
        hasil = [a, b, c]
        return hasil
    x = [5,2,3,6]
    print(dataStat(x))
