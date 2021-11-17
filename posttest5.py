#list menu
dafmen = {
    'NG' : '[NG]-Nasgor(Nasi Goreng)',
    'CR' : '[CR]-Ciwa(Cicak Rawa)',
    'MG' : '[MG]-Mie Goreng',
    'NK' : '[NK]-Nasi Kuning + Ayam',
    'NP' : '[NP]-Nasi Putih',
    'PG' : '[PG]-Pisang Goreng',
    'RB' : '[RB]-Rujak Buah',
    'JT' : '[JT]-Jus Teh',
    'JK' : '[JK]-Jus Kopi',
    'KC' : '[KC]-Kopi Coklat',
    'KA' : '[KA]-Kopi Asin',
    'JS' : '[JS]-Jus Smoke',
}
def edmen():
    print("""
============ edit menu ============
    1.tambahkan menu
    2.hapus menu
    3.ubah menu
    4.tampilkan menu
    5.keluar
""")


def carhap():
    print("1.menghapus item dengan del\n2.menghapus item dengan pop()\n")

def pil2():
    dafmen[l.upper()]= f'[{l.upper()}]-'+ganl.title()

# vaar
pilung = str('y')
while pilung == 'y':
    edmen()
    try:
        pil1 = int(input("masukkan pilihan(gunakan angka) : "))  
    except:
        print("\nyang anda masukkan bukan angka, pilihan harus berupa angka!")
    else:
        if pil1 == 1 :  # pilih tambahkan menu
            thekey = input("masukkan key = ")
            newname = input(f"tambahkan apa saja yang ada di {thekey} : ")
            dafmen.update({thekey.upper() : f'[{thekey.upper()}]' +"-"+ newname.title(),})
            print("menu telah ditambahkan")
        elif pil1 == 2:     # hapus menu
            carhap()
            try:
                pil2 = int(input("masukkan pilihan : "))
            except:
                print("mohon, masukkan angka!")
            else:
                if pil2 == 1:
                    h = input("key-makanan yang ingin di hapus: ")
                    if h.upper() in dafmen:
                        del dafmen[h.upper()]
                        print("key-menu telah terhapus")
                    else:
                        print("\n key tidak ditemukan")
                elif pil2 == 2:
                    hp = str(input("masukkan key-menu apa yang ingin di hapus? "))
                    dafmen.pop(hp.upper())
                else:
                    print("anda salah inputan")
        elif pil1 == 3:     #ubah menu
            l = str(input("masukkan keyword yang ingin diubah = "))
            ganl = str(input("diubah menjadi : "))
            pil2()

        elif pil1 == 4:     #tampilkan menu
            for key in dafmen:
                print(dafmen[key])
        elif pil1 == 5:     #keluar
            print("terimakasih, anda telah keluar")
            break
        else:
            print("\nmohon maaf, masukkan anda salah. tolong ulangi kembali")        
