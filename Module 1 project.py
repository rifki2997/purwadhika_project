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

def menu_utama(): #menampilkan menu utama
    print("\t Welcome to Database")
    try:
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
    except ValueError:
       print('wrong, please enter number 1 - 5 to enter the program')
       return menu_utama()



def table(): #membuat data list yang mempunyai dictionary di dalamnya menjadi bentuk tabel dengan tabulate
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


def backtomenu1(): #membuat jalan pintas ke tampilan data
   sudah = str(input("apakah sudah selesai melihat ( ketik yes): "))
   if (sudah == "yes"):
      tampilan_data()
   else:
      print("salah, ketik yes")
      return backtomenu1()
   menu_utama()

def backtomenu(): #membuat jalan pintas ke menu utama
   sudah = str(input("apakah sudah selesai melihat ( ketik yes): "))
   if (sudah == "yes"):
      menu_utama()
   else:
      print("salah, ketik yes")
      return backtomenu()
   menu_utama()

def tampilan_data(): #membaca data
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


def add_data(): #menambah data
   try:
      print("masukkan data data yang akan diinputkan ke tabel")
      namapasien = str(input('Masukkan nama pasien: '))
      namapasien = namapasien.capitalize()
      gender = str(input('Masukkan gender pasien (male / female): '))
      if (gender == "male") or (gender == "female"):
         gender = gender.capitalize()
      else:
         return add_data()
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
         if (status == "bahaya") or (status == "tidak"):
               status = status.capitalize()
         else:
            return add_data()
         dirawat = str(input('Masukkan status apakah dirawat di ruang ICU (ya/tidak): '))
         dirawat = dirawat.lower()
         if (dirawat == "bahaya") or (dirawat == "tidak"):
               dirawat = dirawat.capitalize()
         else:
               return add_data()
      stock = int(input('Masukkan stock obat: '))
      if (0 < stock < 10000000000):
         stock = stock
      else:
         return add_data()
      harga = int(input('Masukkan harga obat: '))
      if (0 < harga < 10000000000):
         harga = harga
      else:
         return add_data()
   

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
   except ValueError:
      print("ada yang salah input, ulang dari awal")
      add_data()
   backtomenu1()

def delete_data():
   d4 = [('Index','Nama', 'Kelamin', 'Umur', 'Penyakit', 'Dokter', 'Rawat Inap', 'Stock Obat', 'Harga')]

   for i in range(len(daftar_pasien)):
      d4.append((i + 1,daftar_pasien[i]['nama'],daftar_pasien[i]['kelamin'],daftar_pasien[i]['Umur'],
                 daftar_pasien[i]['penyakit'],daftar_pasien[i]['dokter'],daftar_pasien[i]['rawat_inap'],
                 daftar_pasien[i]['stock_obat'],daftar_pasien[i]['harga']))
   rows = tabulate(d4,headers='firstrow',tablefmt='grid')
   print(rows)
   try:
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
         backtomenu()
   except ValueError:
      return delete_data()
def bayar():
   cart = []
   print('Daftar Obat\n')
   print(table2())
   try:
      while True :
         index1 = int(input('Masukkan index pasien yang ingin transaksi: '))
         if (index1 < 0 or index1 >= len(daftar_pasien)+1):
            print("tidak ada di index yg dilihat")
            return bayar()
         qtyobat = int(input('Masukkan jumlah obat yang ingin dibeli : '))
         index1 = index1 - 1
         if(qtyobat > daftar_pasien[index1]['stock_obat']) :
            print('Stock tidak cukup, pasien {} obat ini tinggal {}'.format(daftar_pasien[index1]['nama'],daftar_pasien[index1]['stock_obat']))
         elif (qtyobat <= daftar_pasien[index1]['stock_obat']):
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
         else:
            print("error, input yang benar")
            return transaksi()
   except ValueError:
      return transaksi()

cart = []
def transaksi():
   print('Daftar data biaya pasien berobat\n')
   print(table2())
   try:
      tanya=str(input('apakah pasien ingin membayar pengobatan?[y/n]:'))
      tanya1=str(input('apakah pasien dirawat inap?[y/n]:'))
      while tanya=="y":
         if tanya1 == "y":
            keadaan = str(input('apakah pasien sudah sembuh?[y/n]:'))
            if keadaan == "n":
               print("pembayaran dapat dilakukan setelah pasien dinyatakan sembuh")
               backtomenu()
            elif keadaan == "y":
               bayar()
               backtomenu()
         elif tanya1 == "n":
            bayar()
            backtomenu()
      while tanya=="n" and tanya1 == "n":
         backtomenu()
   except ValueError:
      print(" pilih y or n")
      return transaksi()


def update_data_pasien(daftar_pasien, index, key, value):
    if index >= 0 and index < len(daftar_pasien):
        daftar_pasien[index][key] = value
        return True
    else:
        return False


def update():
   print("Update data yang tersedia\n")
   print("check data yang akan diubah \n")
   print(table())
   rows = table()
   try:
      index_pasien = int(input('Masukkan index pasien yang ingin diganti: '))
      if index_pasien < 1 or index_pasien > len(rows):
         print("Index pasien tidak valid, check tabel.")
         return update()
      else:
         print("kata kunci untuk update: nama,kelamin, umur, penyakit, dokter,rawat, harga, stock")
         yg_diganti = str(input("yang akan diganti: "))
         if (yg_diganti == "nama"):
            new_nama = str(input('Masukkan nama baru: '))
            new_nama = new_nama.capitalize()
            success = update_data_pasien(daftar_pasien, index_pasien - 1,'nama',new_nama) 
            if success:
               print(f"Data pasien dengan index {index_pasien} berhasil diperbarui:")
               print(table())  
               backtomenu()
            else:
               print("Gagal memperbarui data pasien.")
               return update()
         elif (yg_diganti == "umur"):
            try:
               new_usia = int(input('Masukkan usia baru: '))
               if (0 < new_usia < 10000000000):
                  new_usia = new_usia
               else:
                  update()
            except ValueError:
               print("Input harus berupa bilangan bulat. Silakan coba lagi.")
               update()
            success = update_data_pasien(daftar_pasien, index_pasien - 1,'Umur',new_usia) 
            if success:
               print(f"Data pasien dengan index {index_pasien} berhasil diperbarui:")
               print(table())  
               backtomenu()
            else:
               print("Gagal memperbarui data pasien.")
               return update()
         elif (yg_diganti == "stock"):
            try:
               new_stock_obat = int(input('Masukkan stock obat yang baru: '))
               if (0 < new_stock_obat < 10000000000):
                  new_stock_obat = new_stock_obat
               else:
                  return update()
            except ValueError:
               return update()
            success = update_data_pasien(daftar_pasien, index_pasien - 1,'stock_obat',new_stock_obat) 
            if success:
               print(f"Data pasien dengan index {index_pasien} berhasil diperbarui:")
               print(table())
               backtomenu()
         elif (yg_diganti == "harga"):
            try:
               new_harga = int(input('Masukkan harga obat yang baru: '))
               if (0 < new_harga < 10000000000):
                  new_harga = new_harga
               else:
                  return add_data()
            except ValueError:
               return update()
            success = update_data_pasien(daftar_pasien, index_pasien - 1,'harga',new_harga) 
            if success:
               print(f"Data pasien dengan index {index_pasien} berhasil diperbarui:")
               print(table())
               backtomenu()
            else:
               print("Gagal memperbarui data pasien.")
               return update()
         elif (yg_diganti == "kelamin"):
            new_kelamin = input('Masukkan gender baru(male/female): ')
            new_kelamin = new_kelamin.capitalize()
            success = update_data_pasien(daftar_pasien, index_pasien - 1,'kelamin',new_kelamin) 
            if success:
               print(f"Data pasien dengan index {index_pasien} berhasil diperbarui:")
               print(table()) 
               backtomenu()
            else:
               print("Gagal memperbarui data pasien.")
               return update()
         elif (yg_diganti == "dokter"):
            new_dokter = input('Masukkan nama dokter: ')
            new_dokter = new_dokter.capitalize()
            success = update_data_pasien(daftar_pasien, index_pasien - 1,'dokter',new_dokter) 
            if success:
               print(f"Data pasien dengan index {index_pasien} berhasil diperbarui:")
               print(table())  
               backtomenu()
            else:
               print("Gagal memperbarui data pasien.")
               return update()
         elif (yg_diganti == "penyakit"):
            new_penyakit = input('Masukkan status penyakit (bahaya/tidak): ')
            new_penyakit = new_penyakit.lower()
            if (new_penyakit == "bahaya") or (new_penyakit == "tidak"):
               new_penyakit = new_penyakit.capitalize()
            else:
               return update()
            success = update_data_pasien(daftar_pasien, index_pasien - 1,'penyakit',new_penyakit) 
            if success:
               print(f"Data pasien dengan index {index_pasien} berhasil diperbarui:")
               print(table())  
               backtomenu()
            else:
               print("Gagal memperbarui data pasien.")
               return update()
         elif (yg_diganti == "rawat "):
            new_rawat_inap = input('Masukkan status penyakit (bahaya/tidak): ')
            new_rawat_inap = new_rawat_inap.lower()
            if (new_rawat_inap == "bahaya") or (new_rawat_inap == "tidak"):
               new_rawat_inap = new_rawat_inap.capitalize()
            else:
               return update()
            success = update_data_pasien(daftar_pasien, index_pasien - 1,'rawat_inap',new_rawat_inap) 
            if success:
               print(f"Data pasien dengan index {index_pasien} berhasil diperbarui:")
               print(table())  
               backtomenu()
            else:
               print("Gagal memperbarui data pasien.")
               return update()   
         else:
               print("Data yang ingin diganti tidak valid (pilih yang diatas).")
               return update()
   except ValueError:
      return update()      

menu_utama()
