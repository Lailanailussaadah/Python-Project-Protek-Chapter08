nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	    {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]
    
def nilaitertinggi(nilaiMhs):
    mid=[]
    uas =[]
    hasil = []
    tertinggi =[]
    for i in nilaiMhs:
        nilaiAkhir = (i['mid'] + (2*i['uas']))/3
        hasil.append(nilaiAkhir)
    tertinggi = hasil.index(max(hasil))   
    dTertinggi =  {'nim': nilaiMhs[tertinggi]['nim'], 'nama' : nilaiMhs[tertinggi]['nama']}

    return dTertinggi
xTertinggi = nilaitertinggi(nilaiMhs)
print('Mahasiswa dengan nilai tertinggi : ' , xTertinggi['nama'] , 'NIM' , xTertinggi['nim'])
