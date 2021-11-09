# vaar
pilung = str('y')
#list menu
dafman = [
    ["nasi goreng " 'Rp5000'],
    ["nasi kuning + ayam " 'Rp15000'],
    ["nasi putih " 'Rp2000'],
    ["cicak rawa " 'Rp2000'],
    ["mie goreng " 'Rp3000']
]
dafmin = [
    ["jus teh " 'Rp2000'],
    ["jus kopi " 'Rp3000'],
    ["jus smoke " 'Rp20000'],
    ["kopi coklat " 'Rp4000'],
    ["kopi asin " '2000']
]
print(dafman)
def edmen():
    print("""
============ edit menu ============
    1.tambahkan menu
    2.hapus menu
    3.ubah menu
    4.tampilkan menu
    5.keluar
""")

def bahmen():
    print("""
    menu apa yang ingin anda tambahkan?
    1.makanan
    2.minuman
    """)
def letak1():
    print("""
    dimana letak yang ingin anda tambahkan?
    1.tengah
    2.belakang
    3.tekan angka selain 1 dan 2 untuk keluar (untuk type data str = error)
        """)

def pusmn():
    print("""
    menu apa yang ingin anda hapus?
    1.makanan
    2.minuman
    """)
def carhap():
    print("1.menghapus item dengan remove()\n2.menghapus item dengan clear()\n")

def ubmn():
    print("""
    menu apa yang ingin anda ubah?
    1.makanan
    2.minuman
    """)

while pilung == 'y':
    edmen()
    pil1 = int(input("masukkan pilihan(gunakan angka) : "))
    if pil1 == 1 :  # pilih tambahkan menu
        bahmen()
        pil2 = int(input("pilih dengan angka : "))
        if pil2 == 1 :  # pilih makanan
            letak1()
            letak = int(input("pilih dengan angka : "))
            if letak == 1:
                newname = input("tambahkan menu makanan = ")
                newga = input('masukkan harga : ')
                dafman.insert(1,[newname+' '+ newga])
            elif letak == 2:
                newname = input("tambahkan menu makanan = ")
                newga = input('masukkan harga : ')
                dafman.append([newname+' '+newga])
            else :
                print("pilihan salah, otomatis kembali ke menu awal")
        elif pil2 == 2 :    # pilih minuman
            letak1()
            letak = int(input("pilih dengan angka : "))
            if letak == 1:
                newnamen = input("tambahkan menu minuman = ")
                newrga = input('masukkan harga : ')
                dafmin.insert(1,[newnamen+' '+newrga])
            elif letak == 2:
                newnamen = input("tambahkan menu minuman = ")
                newrga = input('masukkan harga : ')
                dafmin.append([newnamen+' '+newrga])
            else :
                print("pilihan salah, otomatis kembali ke menu awal")
        else:
            print("masukan salah, anda kembali ke menu awal")
    elif pil1 == 2:     # hapus menu
        pusmn()
        pil2 = int(input("masukkan pilihan : "))
        if pil2 == 1:
            h = int(input("makanan yang ingin di hapus di line : "))
            del dafman[h]
        elif pil2 == 2:
            hap = str(input("masukkan menu minuman apa yang ingin di hapus "))
            al = len(dafmin)
            for hp in range(al):
                dafmin.remove(hp)
        else:
            print("anda salah inputan")
    elif pil1 == 3:     #ubah menu
        ubmn()
        k = int(input("pilih 1 atau 2? "))
        if k == 1:
            l = int(input("list ke- "))
            ganl = input("diubah menjadi : ")
            dafman[l]=[ganl]
        elif k == 2:
            l = int(input("list ke- "))
            ganl = input("diubah menjadi : ")
            dafman[l]=[ganl]
        else:
            print("pilihan anda salah")
    elif pil1 == 4:     #tampilkan menu
        print("""
     ------daftar menu------
        """)
        print("""
             makanan
        """)
        for men in dafman:
            for dafman in men:
                print(dafman)
        print("""
             minuman
        """)
        for emn in dafmin:
            for dafmin in emn:
                print(dafmin)
        break
    elif pil1 == 5:     #keluar
        print("terimakasih, anda telah keluar")
        break
    else:
        print("mohon maaf, masukkan anda salah. tolong ulangi kembali")