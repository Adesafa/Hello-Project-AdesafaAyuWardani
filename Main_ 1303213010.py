#Membuat dictionary daftar_mobil dengan key adalah tipe mobil, sedangkan valuenya berupa list yang elemennya berupa warna, jenis dan stok dari mobil.
daftar_mobil = {'avanze_S' : ['merah', 'bensin', 10],
                'avanze_Q' : ['merah', 'bensin', 5],
                'kijang_V' : ['biru', 'solar', 3],
                'kijang_S' : ['hitam', 'solar', 5],
                'kijang_Q' : ['merah', 'solar', 4]}


def report(): #Membuat fungsi report yang digunakan untuk menampilkan tipe mobil dengan stok terbanyak dan tersedikit.
    val = [daftar_mobil['avanze_S'][2],daftar_mobil['avanze_Q'][2],daftar_mobil['kijang_V'][2],
           daftar_mobil['kijang_S'][2],daftar_mobil['kijang_Q'][2]] #membandingkan tipe mobil dengan nilainya dalam satu array
    for key in daftar_mobil:
        if max(val) == daftar_mobil[key][2]: #menggunakan if max dan if min untuk mencari jumlah yang terbanyak dan tersedikit
            print("Jumlah mobil terbanyak adalah type", key) #key yang dipakai yaitu dictionary yang diatas berisi tipe mobil
        if min(val) == daftar_mobil[key][2]:
            print("Jumlah mobil tersedikit adalah type", key)

def bahan_bakar(): #membuat fungsi bahan_bakar yang digunakan untuk mengembalikan (return) bahan bakar suatu mobil tertentu.
    for key,value in daftar_mobil.items(): #menggunakan perulangan for key agar mempermudah dalam mereturn itemsnya 
        print("Bahan bakar mobil type", key, "adalah", value[1]) 

def main(): #Membuat main program yang digunakan untuk menampilkan dictionary dan memanggil fungsi yang dibuat.
    print('===============================DATA MOBIL===============================')
    for key,value in daftar_mobil.items():
        print("Mobil dengan type", key, "bewarna", value[0], "berbahan bakar", value[1], "dan stoknya berjumlah",
              value[2]) #membuat keluaran dengan menyandingkan masing-masing nilai(value) di dictionary
    print("====================STOK MOBIL TERBANYAK DAN TERSEDIKIT==================")
    report()
    print("===========================JENIS BAHAN BAKAR============================")
    bahan_bakar()

if __name__== "__main__": # main digunakan untuk memanggil fungsinya
    main()






    

