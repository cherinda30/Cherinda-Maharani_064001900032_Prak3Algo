#AlgoPrak3_Cherinda Maharani

print ("           /$$                           /$$                 /$$          ")
print ("          | $$                          |__/                | $$          ")
print ("  /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$  /$$ /$$$$$$$   /$$$$$$$  /$$$$$$ ")
print (" /$$_____/| $$__  $$ /$$__  $$ /$$__  $$| $$| $$__  $$ /$$__  $$ |____  $$")
print ("| $$      | $$  \ $$| $$$$$$$$| $$  \__/| $$| $$  \ $$| $$  | $$  /$$$$$$$")
print ("| $$      | $$  | $$| $$_____/| $$      | $$| $$  | $$| $$  | $$ /$$__  $$")
print ("|  $$$$$$$| $$  | $$|  $$$$$$$| $$      | $$| $$  | $$|  $$$$$$$|  $$$$$$$")
print (" \_______/|__/  |__/ \_______/|__/      |__/|__/  |__/ \_______/ \_______/")

a,b = (
    int(input('Masukkan angka awal: ')),
    int(input('Masukkan angka terakhir: '))
)

#i = a
while (a and a <= b):
    print (a,b)
    a += 1
    b -= 1
