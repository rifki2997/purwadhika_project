#Module 1 
#Muhammad Rifki Hartanto
#program data pasien di rumah sakit purwadhika
#data yang dipakai:
#                   1.nama pasien
#                   2.umur
#                   3.penyakit
#                   4.nama dokter 
#                   5.gender
#                   6.stock obat
#                   7.harga
#                   8.rawat inap

from tabulate import tabulate
daftar_pasien = [
    {
        'nama': 'Amiya',
        'kelamin': "Female",
        'Umur': 20,
        'penyakit': "bahaya",
        'dokter': "Kaltsit",
        'rawat_inap': "Ya",
        'stock_obat': 40,
        'harga': 20000
    },
    {
        'nama': 'Joko',
        'kelamin': "Male",
        'Umur': 40,
        'penyakit': "bahaya",
        'dokter': "Kaltsit",
        'rawat_inap': "Ya",
        'stock_obat': 20,
        'harga': 100000
    },
    {
        'nama': 'Adi',
        'kelamin': "Male",
        'Umur': 18,
        'penyakit': "tidak",
        'dokter': "Budi",
        'rawat_inap': "tidak",
        'stock_obat': 100,
        'harga': 5000

    }
]

def menu_utama():
    print("\t Welcome to Database")
    menu_database = int(input('''
     Selamat Datang
    
    List Menu:
    1. menampilkan daftar pasien dan daftar dokter
    2. menambah data pasien
    3. menghapus index
    4. mengupdate index
    5. transaksi pengobatan
    6. exit
    
    Masukkan no pilihan: '''))
    if menu_database == 1:
       tampilan_data()
    elif menu_database == 2:
       add_data()
    elif menu_database == 3:
       delete_data()
    elif menu_database == 4:
       update()
    elif menu_database == 5:
       transaksi()
    elif menu_database == 6:
       print("\t\t Terima Kasih")
       quit()
    else:
       print('wrong, please enter number 1 - 5 to enter the program')
       return menu_utama()


def table():
   d2 = [('Index','Nama', 'Kelamin', 'Umur', 'Penyakit', 'Dokter', 'Rawat Inap', 'Stock Obat', 'Harga')]
   for i in range(len(daftar_pasien)):
      d2.append((i + 1,daftar_pasien[i]['nama'],daftar_pasien[i]['kelamin'],daftar_pasien[i]['Umur'],
                 daftar_pasien[i]['penyakit'],daftar_pasien[i]['dokter'],daftar_pasien[i]['rawat_inap'],
                 daftar_pasien[i]['stock_obat'],daftar_pasien[i]['harga']))
   d3 = tabulate(d2, headers='firstrow',tablefmt='grid')
   #print(d3)
   return d3

def table2():
   d5 = [('Index','Nama', 'Penyakit', 'Dokter', 'Rawat Inap', 'Stock Obat', 'Harga')]
   for i in range(len(daftar_pasien)):
      d5.append((i + 1,daftar_pasien[i]['nama'],daftar_pasien[i]['penyakit'],daftar_pasien[i]['dokter'],
                 daftar_pasien[i]['rawat_inap'],daftar_pasien[i]['stock_obat'],daftar_pasien[i]['harga']))
   d6 = tabulate(d5, headers='firstrow',tablefmt='grid')
   return d6


def backtomenu1():
   sudah = str(input("apakah sudah selesai melihat ( ketik yes): "))
   if (sudah == "yes"):
      tampilan_data()
   else:
      print("salah, ketik yes")
      return backtomenu1()
   menu_utama()


def tampilan_data():
   print("Menampilkan Data Pasien")
   menu_data =int(input('''
    List Menu:
    1. menampilkan data pribadi pasien
    2. menampilkan data dokter yang menangani pasien
    3. kembali ke menu 
    Masukkan no pilihan: '''))

   if menu_data == 1:
      print(table())
      backtomenu1()
   elif menu_data == 2:
      d1 = [('No','Nama', 'Penyakit', 'Dokter', 'Dirawat')]
      for i in range(len(daftar_pasien)):
         d1.append(( i+1,daftar_pasien[i]['nama'], daftar_pasien[i]['penyakit'], daftar_pasien[i]['dokter'], daftar_pasien[i]['rawat_inap']))
      table1 = tabulate(d1,headers='firstrow',tablefmt='grid')
      print(table1)
      backtomenu1()
   elif menu_data == 3:
      return menu_utama()
   else:
      print("salah nomor, pilih no 1 dan 2 untuk melihat data, 3 untuk kembali ke menu utama")


def add_data():
   print("masukkan data data yang akan dimasukkan ke 2 kategori")
   namapasien = str(input('Masukkan nama pasien: '))
   namapasien = namapasien.capitalize()
   gender = str(input('Masukkan gender pasien (male / female): '))
   if (gender == "male") or (gender == "female"):
      gender = gender.capitalize()
   else:
      return gender
   usia = int(input('Masukkan usia pasien: '))
   dokter = str(input('Masukkan nama dokter: '))
   dokter1 = dokter.lower()
   if (dokter1 == "kaltsit"):
      status = "bahaya"
      dirawat = "ya"
      dokter = dokter1.capitalize()
   elif (dokter1 == "budi"):
      status = "tidak"
      dirawat = "ya"
      dokter = dokter1.capitalize()
   else:
      dokter = dokter1.capitalize()
      status = str(input('Masukkan status penyakit(bahaya/tidak): '))
      status = status.lower()
      dirawat = str(input('Masukkan status apakah dirawat di ruang ICU (ya/tidak): '))
      dirawat = dirawat.lower()
   stock = int(input('Masukkan stock obat: '))
   harga = int(input('Masukkan harga obat: '))

   daftar_pasien.append({
      'nama': namapasien,
      'kelamin': gender,
      'Umur': usia,
      'penyakit': status,
      'dokter': dokter,
      'rawat_inap': dirawat,
      'stock_obat': stock,
      'harga': harga
      })
   backtomenu1()

def delete_data():
   d4 = [('Index','Nama', 'Kelamin', 'Umur', 'Penyakit', 'Dokter', 'Rawat Inap', 'Stock Obat', 'Harga')]

   for i in range(len(daftar_pasien)):
      d4.append((i + 1,daftar_pasien[i]['nama'],daftar_pasien[i]['kelamin'],daftar_pasien[i]['Umur'],
                 daftar_pasien[i]['penyakit'],daftar_pasien[i]['dokter'],daftar_pasien[i]['rawat_inap'],
                 daftar_pasien[i]['stock_obat'],daftar_pasien[i]['harga']))
   rows = tabulate(d4,headers='firstrow',tablefmt='grid')
   print(rows)
   index_pasien = int(input('Masukkan index pasien yang ingin dihapus: '))

   if index_pasien < 1 or index_pasien > len(rows):
        print("Index pasien tidak valid, check tabel.")
        return delete_data()
   else:
      deleted_pasien = daftar_pasien.pop(index_pasien - 1)
      print(f"Data pasien dengan index {index_pasien} berhasil dihapus:")
      print(deleted_pasien)
      print("Data pasien setelah penghapusan:")
      print(table())
      menu_utama()

def bayar():
   cart = []
   print('Daftar Obat\n')
   print('Index\t| Nama  \t| Stock\t| Harga')
   for i in range(len(daftar_pasien)) :
      print('{}\t| {}  \t| {}\t| {}'.format(i,daftar_pasien[i]['nama'],daftar_pasien[i]['stock_obat'],daftar_pasien[i]['harga']))
   while True :
      index1 = int(input('Masukkan index pasien yang ingin transaksi: '))
      qtyobat = int(input('Masukkan jumlah obat yang ingin dibeli : '))
      if(qtyobat > daftar_pasien[index1]['stock_obat']) :
         print('Stock tidak cukup, pasien {} obat ini tinggal {}'.format(daftar_pasien[index1]['nama'],daftar_pasien[index1]['stock_obat']))
      else :
         cart.append({
            'nama': daftar_pasien[index1]['nama'], 
            'qty': qtyobat, 
            'harga': daftar_pasien[index1]['harga'], 
            'index': index1
            })
      print('Isi Cart :')
      print('Nama\t| Qty\t| Harga')
      for item in cart :
         print('{}\t| {}\t| {}'.format(item['nama'], item['qty'], item['harga']))
      print('Daftar Belanja :')
      print('Nama\t| Qty\t| Harga\t| Total Harga')
      totalHarga = 0
      for item in cart :
         print('{}\t| {}\t| {}\t| {}'.format(item['nama'], item['qty'], item['harga'], item['qty'] * item['harga']))
         totalHarga += item['qty'] * item['harga']    
      while True :
         print('Total Yang Harus Dibayar = {}'.format(totalHarga))
         jmlUang = int(input('Masukkan jumlah uang : '))
         if(jmlUang > totalHarga) :
            kembali = jmlUang - totalHarga
            print('Terima kasih \n\nUang kembali anda : {}'.format(kembali))
            for item in cart :
                    daftar_pasien[item['index']]['stock_obat'] -= item['qty']
            cart.clear()
            done = str(input("kembali ke menu utama?(y/n): "))
            if done == "y":
               menu_utama()
            elif done == "n":
               bayar()
            else:
               return done
         elif(jmlUang == totalHarga) :
            print('Terima kasih')
            for item in cart :
                    daftar_pasien[item['index']]['stock_obat'] -= item['qty']
            cart.clear()
            done = str(input("kembali ke menu utama?(y/n): "))
            if done == "y":
               menu_utama()
            elif done == "n":
               bayar()
            else:
               return done
         else :
            kekurangan = totalHarga - jmlUang
            print('Uang anda kurang sebesar {}'.format(kekurangan))


cart = []
def transaksi():
   print('Daftar data biaya pasien berobat\n')
   print(table2())
   tanya=str(input('apakah pasien ingin membayar pengobatan?[y/n]:'))
   tanya1=str(input('apakah pasien dirawat inap?[y/n]:'))
   while tanya=="y":
      if tanya1 == "y":
         keadaan = str(input('apakah pasien sudah sembuh?[y/n]:'))
         if keadaan == "n":
            print("pembayaran dapat dilakukan setelah pasien dinyatakan sembuh")
            menu_utama()
         elif keadaan == "y":
            bayar()
            menu_utama()
      elif tanya1 == "n":
         bayar()
         menu_utama()
   while tanya=="n" and tanya1 == "n":
      menu_utama()

def update():
   print("Update data yang tersedia\n")
   print("check data yang akan diubah \n")
   d6 = [('Index','Nama', 'Kelamin', 'Umur', 'Penyakit', 'Dokter', 'Rawat Inap', 'Stock Obat', 'Harga')]

   for i in range(len(daftar_pasien)):
      d6.append((i + 1,daftar_pasien[i]['nama'],daftar_pasien[i]['kelamin'],daftar_pasien[i]['Umur'],
                 daftar_pasien[i]['penyakit'],daftar_pasien[i]['dokter'],daftar_pasien[i]['rawat_inap'],
                 daftar_pasien[i]['stock_obat'],daftar_pasien[i]['harga']))
   rows = tabulate(d6,headers='firstrow',tablefmt='grid')
   print('Daftar data pasien\n')
   print(rows)
   index_pasien = int(input('Masukkan index pasien yang ingin diupdate: '))

   if index_pasien < 1 or index_pasien > len(rows):
        print("Index pasien tidak valid.")
   else:
        pasien = daftar_pasien[index_pasien - 1]
        print(f"\nData pasien dengan index {index_pasien}:")
        for key, value in pasien.items():
            print(f"{key}: {value}")

        yg_diganti = input("Apakah sudah selesai melihat dan menentukan yang akan diganti? (ya/tidak): ")

        if yg_diganti.lower() == "ya":
            new_nama = input('Masukkan nama baru: ')
            new_nama = new_nama.capitalize()
            new_gender = input('Masukkan jenis kelamin baru (male/female): ')
            if (new_gender == "male") or (new_gender == "female"):
               new_gender = new_gender.capitalize()
            else:
               return update()
            new_usia = int(input('Masukkan umur baru: '))
            new_dokter = input('Masukkan nama dokter baru: ')
            new_dokter1 = new_dokter.lower()
            if (new_dokter1 == "kaltsit"):
               new_status = "tidak"
               new_dirawat = input('Masukkan status rawat inap baru (Ya/Tidak): ')
               new_dirawat = new_dirawat.lower()
               new_dokter = new_dokter1.capitalize()
            elif (new_dokter1 == "budi"):
               new_status = str(input('Masukkan status penyakit(bahaya/tidak): '))
               new_status = new_status.lower()
               new_dirawat = "ya"
               new_dokter = new_dokter1.capitalize()
            else:
               new_dokter = new_dokter1.capitalize()
               new_status = str(input('Masukkan status penyakit(bahaya/tidak): '))
               new_status = new_status.lower()
               new_dirawat = str(input('Masukkan status apakah dirawat di ruang ICU (ya/tidak): '))
               new_dirawat = new_dirawat.lower()
            new_stock_obat = int(input('Masukkan stok obat baru: '))
            new_harga = int(input('Masukkan harga baru: '))

            pasien['nama'] = new_nama
            pasien['kelamin'] = new_gender
            pasien['Umur'] = new_usia
            pasien['penyakit'] = new_status
            pasien['dokter'] = new_dokter
            pasien['rawat_inap'] = new_dirawat
            pasien['stock_obat'] = new_stock_obat
            pasien['harga'] = new_harga

            print("\nData pasien setelah diupdate:")
            for key, value in pasien.items():
                print(f"{key}: {value}")
            #print(table())
            #menu_utama()
            backtomenu1()
        else:
            print("Pengubahan data dibatalkan.")

menu_utama()
