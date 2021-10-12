#AlgoPrak3_ELKOM2_Cherinda Maharani

a,b = (
    int(input('Masukkan nilai total harga belanjaan Anda: ')),
    int(input('Masukkan jumlah uang Anda: '))
)
c= b-a
print("Kembalian Anda sejumlah Rp.",c,'Pecahan uang yang dibutuhkan :')
d= [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
for x in range(0, 9):
    i=0
    while c >= d[x]:
        c = c - d[x]
        i = i+1
        if (i>0):
            print('Uang Rp. %d sebanyak %d lembar' %(d[x], i))             
