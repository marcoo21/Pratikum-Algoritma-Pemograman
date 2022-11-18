print("----------------- SAHARA CLUB -----------------")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 
def fungsimakanan():
    global totalmkn
    global porsi
    global mkn
print ("\n----------------- Menu Makanan -----------------")
print("1. Sandwitch - Rp 25000")
print("2. Spageti - Rp 30000")
print("3. Burger - Rp 11000")
nomor=int(input("Masukan Pilihan: "))
porsi= int(input("Berapa Porsi: "))
if nomor==1:
    totalmkn=porsi*25000
    print (porsi," porsi Sandwitch = Rp", totalmkn)
    mkn=("Sandwitch")
elif nomor==2:
    totalmkn=porsi*30000
    print (porsi," Spageti = Rp", totalmkn)
    mkn=("Spageti")
elif nomor==3:
    totalmkn=porsi*11000
    print (porsi, " Burger = Rp", totalmkn)
    mkn=("Burger")
else:
    print("Pilihan tidak ada, silahkan masukan lagi!!")
    fungsimakanan()
def fungsiminuman():
    global totalmnm
    global mnm
    global gelas
print("\n----------------- Menu Minuman -----------------")
print("1. Ice Land - Rp 60000")
print("2. Jack Denil Wiskey - Rp 55000")
print("3. Mc Donald - Rp 80000")
nomor=int(input("Masukan Pilihan: "))
gelas= int(input("Berapa Gelas: "))
if nomor==1:
    totalmnm=gelas*60000
    print (gelas," Ice Land = Rp", totalmnm)
    mnm=(" Ice Land")
elif nomor==2:
    totalmnm=gelas*55000
    print (gelas, " Jack Denil Wiskey = Rp", totalmnm)
    mnm=("Arcep")
elif nomor==3:
    totalmnm=gelas*80000
    print (gelas, " Mc Donald = Rp", totalmnm)
    mnm=("Mc Donald")
else:
    print("Pilihan tidak ada, silahkan masukan lagi!!")
    fungsiminuman()
    fungsimakanan()
    fungsiminuman()
totalsemua=totalmkn+totalmnm
print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)
print("\n==================================")
print("========== THANK YOU =========")
print("==================================")
print ("Nama\t\t:",pembeli)
print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("Thank you for visiting")
print("Jatibening Estade Blok H no 26")