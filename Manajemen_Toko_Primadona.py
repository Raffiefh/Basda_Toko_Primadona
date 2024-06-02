import psycopg2
import pandas as pd
import os
import time
from prettytable import PrettyTable
from datetime import datetime
now = datetime.now()
date_time = now.strftime("%Y-%m-%d")

conn = psycopg2.connect(database='Primadona_Toko',user='postgres', password='Raffi20005..', host='localhost', port=5432)
cur = conn.cursor()

import datetime

current_time = datetime.datetime.now()
formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')


# # Mengimport sistem fitur Clear()
import os
# # Mengimport pandas 
import pandas as pd
# # Fungsi Clear 
def Clear():
    import platform
    if platform.system() == "Linux":
        print("\x1b[H\x1b[2J")
    elif platform.system() == "Darwin":
        print("\033[2J\033[;H")
    elif platform.system() == "Windows":
        os.system("cls")
        ## Halaman User
        
## Halaman User 

def Halaman_user():
    print(" ============================================================ ")
    print(" ==                                                        == ")
    print(" ==            WEBSITE TOKO PRIMADONA JEMBER               == ")
    print(" ==                                                        == ")
    print(" ============================================================ ")
    query = "select TO_CHAR(NOW(),'Tanggal : [ DD-MM-YYYY ],             [  HH.MI  ]') from produk limit 1"
    cur.execute(query)
    data = cur.fetchall()
    for i in (data):
        print(f" == {i} ==")
    print(" ============================================================ ")
    mytable =PrettyTable([" Nama produk ", " Harga produk ", "EXP", "Jenis produk"])
    query = "select p.produk, p.harga, TO_CHAR(p.kadaluarsa :: DATE,'dd-mm-yyyy'), jp.jenis_produk from produk p join jenis_produk jp on (p.id_jenis_produk = jp.id_jenis_produk) where p.ketersediaan_produk = '1'"
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        mytable.add_row(i)
    print( mytable )
    print(" ============================================================ ")
    print(" ==  [1]   Order produk                                    == ")
    print(" ==  [2]   Membeli pre order                               == ")
    print(" ==  [3]   Riwayat Pembelian                               == ")
    print(" ==  [4]   Hapus Pembelian                                 == ")
    print(" ==  [5]   Feedback                                        == ")
    print(" ==  [0]   OUT                                             == ")
    print(" ==  [ Untuk masuk inputkan berdasarkan angka ]            == ")
    print(" ============================================================ ")
    Masuk = input(" == Halaman masuk :")
    if Masuk == "2":
        print(" ============================================================ ")
        print(" ==  [1]   Pre Order produk                                == ")
        print(" ==  [2]   Hapus Order                                     == ")
        print(" ==  [3]   Lihat Pre order                                 == ")
        print(" ==  [0]   Out                                             == ")
        print(" ============================================================ ")
        Masuk2 = input("== Halaman masuk ==")
        if Masuk2 == "1":
            Clear()
            def tambah_preorder(cur, conn):
                query = "SELECT id_admin, id_customer, id_jenis_pembayaran, tanggal_pre_order, no_antrian_pre_order, catatan_pesanan, id_status_pesanan FROM pre_order"
                cur.execute(query)
                data = cur.fetchall()

                table = PrettyTable()
                table.field_names = ["id_admin", "id_customer", "id_jenis_pembayaran", "tanggal_pre_order", "no_antrian_pre_order", "catatan_pesanan", "id_status_pesanan"]
                for row in data:
                    table.add_row(row)
                print(table)

                id_admin = int(input("Masukkan ID Admin: "))
                id_customer = int(input("Masukkan ID Customer: "))
                id_jenis_pembayaran = int(input("Masukkan ID Jenis Pembayaran: "))
                tanggal_pre_order = input("Masukkan Tanggal Pre-order: ")
                no_antrian_pre_order = int(input("Masukkan Nomor Antrian Pre-order: "))
                catatan_pesanan = input("Masukkan Catatan Pesanan: ")
                id_status_pesanan = int(input("Masukkan ID Status Pesanan: "))

                query = """
                    INSERT INTO pre_order (id_admin, id_customer, id_jenis_pembayaran, tanggal_pre_order, no_antrian_pre_order, catatan_pesanan, id_status_pesanan)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    RETURNING id_pre_order
                """
                cur.execute(query, (id_admin, id_customer, id_jenis_pembayaran, tanggal_pre_order, no_antrian_pre_order, catatan_pesanan, id_status_pesanan))
                id_pre_order = cur.fetchone()[0]
                conn.commit()
                return id_pre_order
            tambah_preorder()
        if Masuk2 == "2":
            Clear()
            def hapus_preorder(cur, conn):
                query = "SELECT id_admin, id_customer, id_jenis_pembayaran, tanggal_pre_order, no_antrian_pre_order, catatan_pesanan, id_status_pesanan FROM pre_order"
                cur.execute(query)
                data = cur.fetchall()

                table = PrettyTable()
                table.field_names = ["id_admin", "id_customer", "id_jenis_pembayaran", "tanggal_pre_order", "no_antrian_pre_order", "catatan_pesanan", "id_status_pesanan"]
                for row in data:
                    table.add_row(row)
                print(table)

                id_pre_order = int(input("Masukkan ID Pre-order yang ingin dihapus: "))
                query = "DELETE FROM pre_order WHERE id_pre_order = %s"
                cur.execute(query, (id_pre_order,))
                conn.commit()
            hapus_preorder()
        if Masuk2 == "3":
            Clear()
            def lihat_preorder(cur, conn, id_pre_order=None):
                if not id_pre_order:
                    id_pre_order = int(input("Masukkan ID Pre-order yang ingin dilihat : "))

                if id_pre_order:
                    query = "SELECT * FROM pre_order WHERE id_pre_order = %s"
                    cur.execute(query, (id_pre_order,))
                else:
                    query = "SELECT * FROM pre_order"
                    cur.execute(query)
    
                preorder = cur.fetchall()
                return preorder
            lihat_preorder()
        else:
            Clear()
            Halaman_user()
    elif Masuk == "1":
        pass
    elif Masuk == "3":
        Clear()
        print(" ============================================================ ")
        print(" ==                                                        == ")
        print(" ==        FEEDBACK WEBSITE TOKO PRIMADONA JEMBER          == ")
        print(" ==   [1] RIWAYAT ORDERAN [2] RIWAYAT PREORDER [3] OUT     == ")
        print(" ==                                                        == ")
        print(" ============================================================ ")
        while True:
            Masuk2 = input(" Halaman masuk :")
            if Masuk2 == "1":
                def riwayat_order_customer():
                    print("\n========= Riwayat Order Customer =========\n")
                    nama_customer = input("Masukkan nama customer : ")
                    query_order = "SELECT d.id_detail_order, c.nama_customer, o.tanggal_order, sp.status_pesanan, p.produk, p.harga, d.jumlah_order, (p.harga*d.jumlah_order) as total_pembayaran, jp.jenis_pembayaran, c.alamat " \
                                "FROM orders o " \
                                "JOIN customer c ON(c.id_customer = o.id_customer) " \
                                "JOIN jenis_pembayaran jp ON(jp.id_jenis_pembayaran = o.id_jenis_pembayaran) " \
                                "JOIN status_pesanan sp ON(sp.id_status_pesanan = o.id_status_pesanan) " \
                                "JOIN detail_order d ON(d.id_order = o.id_order) " \
                                "JOIN produk p ON(p.id_produk = d.id_produk) " \
                                "WHERE c.nama_customer = %s" \
                                "ORDER BY o.tanggal_order ASC " 

                    cur.execute(query_order, (nama_customer,))
                    data = cur.fetchall()
                        
                    if not data:
                        print(f"Data administrasi untuk nama customer {nama_customer} tidak ditemukan")
                    else:
                        table = PrettyTable()
                        table.field_names = ["ID Detail Order", "Nama Customer", "Tanggal Order", "Status Pesanan", "Produk", "Harga Produk", "Jumlah Order", "Total Pembayaran", "Jenis Pembayaran", "Alamat"]
                            
                    for row in data:
                        table.add_row(row)
                            
                        Clear()
                        print(table)

                        cur.close()
                        conn.close()
                riwayat_order_customer()
                Masuk2 = input(" Halaman masuk :")
            elif Masuk2 == "2":
                def riwayat_pre_order_customer():
                    print("\n========= Riwayat Pre Order Customer=========\n")
                    nama_customer = input("Masukkan nama customer : ")
                    query_pre_order = "SELECT dp.id_detail_pre_order, c.nama_customer, po.tanggal_pre_order, sp.status_pesanan, p.produk, p.harga, dp.jumlah_pre_order, po.catatan_pesanan, (p.harga*dp.jumlah_pre_order) as total_pembayaran, jp.jenis_pembayaran, c.alamat " \
                                        "FROM pre_order po " \
                                        "JOIN customer c ON(c.id_customer = po.id_customer) " \
                                        "JOIN jenis_pembayaran jp ON(jp.id_jenis_pembayaran = po.id_jenis_pembayaran) " \
                                        "JOIN status_pesanan sp ON(sp.id_status_pesanan = po.id_status_pesanan) " \
                                        "JOIN detail_pre_order dp ON(dp.id_pre_order = po.id_pre_order) " \
                                        "JOIN produk p ON(p.id_produk = dp.id_produk) " \
                                        "WHERE c.nama_customer = %s" \
                                        "ORDER BY po.tanggal_pre_order ASC "
                    
                    cur.execute(query_pre_order, (nama_customer,))
                    data = cur.fetchall()
                        
                    if not data:
                        print(f"Data administrasi untuk nama customer {nama_customer} tidak ditemukan")
                    else:
                        table = PrettyTable()
                        table.field_names = ["ID Detail Pre Order", "Nama Customer", "Tanggal Pre Order", "Status Pesanan", "Produk", "Harga Produk", "Jumlah Pre Order", "Catatan Pesanan", "Total Pembayaran", "Jenis Pembayaran", "Alamat"]
                        
                    for row in data:
                        table.add_row(row)
                        
                        Clear()
                        print(table)

                        cur.close()
                        conn.close()
                riwayat_pre_order_customer()
            else:
                Clear()
                Halaman_user()
    elif Masuk == "4":
        pass
    elif Masuk == "5":
        def Feedback():
            Clear()
            print(" ============================================================ ")
            print(" ==                                                        == ")
            print(" ==        FEEDBACK WEBSITE TOKO PRIMADONA JEMBER          == ")
            print(" ==                                                        == ")
            print(" ============================================================ ")
            mytable =PrettyTable(["Nama pengguna"," Tanggal ", " Komentar "])
            query = "select c.nama_customer, TO_CHAR(f.tanggal_feedback :: DATE,'dd-mm-yyyy'), f.komentar from feedback f join customer c on (f.id_customer = c.id_customer)"
            cur.execute(query)
            data = cur.fetchall()
            for i in data:
                mytable.add_row(i)
            print( mytable )
            print(" ============================================================ ")
            Mau_Feedback=input('Apakah kamu ingin memeasukkan Feedback [Y][T]: ')
            if Mau_Feedback == "Y":
                try :
                    Feedback_saya= input("Saran dan komentar anda: ")
                    query = f"INSERT INTO feedback (tanggal_feedback,komentar, id_customer) VALUES ('{formatted_time}', '{Feedback_saya}', {user_id})"
                    cur.execute(query, (formatted_time, Feedback_saya, user_id))
                    conn.commit()
                    Clear()
                    print(" Anda berhasil menambahkan produk")
                    Halaman_user()
                except:
                        Clear()
                        print("Mohon maaf saat ini kami tidak menerima respon")
                        Halaman_user()
            else :
                Feedback()
                print(" Masukkan berdasarkan printah")
        Feedback()
    elif Masuk == "0":
        Clear()
    else :
        Clear()
        print("Harap menginputkan data dengan benar")
        Halaman_user()
        
def Halaman_admin():
    print(" ============================================================ ")
    print(" ==                                                        == ")
    print(" ==      WEBSITE TOKO PRIMADONA JEMBER KHUSUS ADMIN        == ")
    print(" ==                                                        == ")
    print(" ============================================================ ")
    query = "select count(produk) from produk where ketersediaan_produk = '1' limit 1"
    cur.execute(query)
    data = cur.fetchall()
    for i in (data):
        print(f"  == Produk yang dijual hari ini {i} ")
    print(" ============================================================ ")
    print(" ==  [1]   Menambahkan bagian produk                       == ")
    print(" ==  [2]   Melihat pembelian                               == ")
    print(" ==  [3]   Mengubah produk                                 == ")
    print(" ==  [4]   Update pesanan                                  == ")
    print(" ==  [5]   Menghapus bagian produk                         == ")
    print(" ==  [6]   Melihat riwayat pembelian                       == ")
    print(" ==  [7]   Menambahkan jenis pembayaran                    == ")
    print(" ==  [0]   OUT                                             == ")
    print(" ============================================================ ")
    Masuk = input(" == Halaman masuk :")
    if Masuk == "1":
        Clear()
        def Tambah_Produk():
            print(" ============================================================ ")
            print(" ==                                                        == ")
            print(" ==            MENAMBAH BAGIAN PRODUK                      == ")
            print(" ==                                                        == ")
            print(" ============================================================ ")
            print(" ===================    RINCIAN PRODUK     ================== ")
            mytable =PrettyTable(["Id produk"," Nama produk ", " Harga produk ", "EXP", "Jenis produk", "Penjualan hari ini"])
            query = "select p.id_produk, p.produk, p.harga, TO_CHAR(p.kadaluarsa :: DATE,'dd-mm-yyyy'), jp.jenis_produk , p.ketersediaan_produk from produk p join jenis_produk jp on (p.id_jenis_produk = jp.id_jenis_produk)"
            cur.execute(query)
            data = cur.fetchall()
            for i in data:
                mytable.add_row(i)
            print( mytable )
            print(" ===================    RINCIAN JENIS      ================== ")
            mytable=PrettyTable(["Id produk"," Jenis produk "])
            query = "select id_jenis_produk, jenis_produk from jenis_produk "
            cur.execute(query)
            data = cur.fetchall()
            for j in data:
                mytable.add_row(j)
            print( mytable )
            print(" ============================================================ ")
            print(" ===  [1] LANJUT TAMBAH PRODUK [0]  LANJUT OUT           ==== ")
            print(" ===  [2] LANJUT TAMBAH JENIS  [3]  LANJUT TAMBAH VARIAN ==== ")
            print(" ============================================================ ")
            Mau_Tambah = input("  Apakah anda ingin menambahkan bagian-bagian produk: ")
            if Mau_Tambah == "1":
                Clear()
                print(" ============================================================ ")
                print(" ==                                                        == ")
                print(" ==                    MENAMBAH PRODUK                     == ")
                print(" ==                                   [1] Tambah [0] Out   == ")
                print(" ============================================================ ")
                mytable =PrettyTable(["Id produk"," Nama produk ", " Harga produk ", "EXP", "Jenis produk", "Penjualan hari ini"])
                query = "select p.id_produk, p.produk, p.harga, TO_CHAR(p.kadaluarsa :: DATE,'dd-mm-yyyy'), jp.jenis_produk , p.ketersediaan_produk from produk p join jenis_produk jp on (p.id_jenis_produk = jp.id_jenis_produk)"
                cur.execute(query)
                data = cur.fetchall()
                for i in data:
                    mytable.add_row(i)
                print( mytable )
                print(" ============================================================ ")
                mytable=PrettyTable(["Id produk"," Jenis produk "])
                query = "select id_jenis_produk, jenis_produk from jenis_produk "
                cur.execute(query)
                data = cur.fetchall()
                for j in data:
                    mytable.add_row(j)
                print( mytable )
                print(" ============================================================ ")
                Lanjutkan = input("Pilihan anda: ")
                if Lanjutkan == "1":
                    try :
                        products= input("Input nama produk : ")
                        harga = int(input("Input harga produk (ex. 2000) : "))
                        kadaluarsa = input("Input tanggal kadaluarsa (ex. 2026-11-07): ")
                        gambar_produk = input("Input link gambar produk : ")
                        print("0 jika barang tidak ingin dijual 1 jika akan dijual")
                        ketersediaan_produk = input("Input ketersediaan produk (0/1) : ")
                        id_jenis_produk = int(input("Input ID Jenis Produk : "))
                        query = f"INSERT INTO produk (produk, harga, kadaluarsa, gambar_produk, ketersediaan_produk, id_jenis_produk) VALUES ('{products}', {harga}, '{kadaluarsa}', '{gambar_produk}', '{ketersediaan_produk}', {id_jenis_produk})"
                        cur.execute(query, (products, harga, kadaluarsa, gambar_produk, ketersediaan_produk, id_jenis_produk))
                        conn.commit()
                        Clear()
                        print(" Anda berhasil menambahkan produk")
                        Halaman_admin()
                    except:
                        Clear()
                        print("Mohon maaf data yang anda inputkan salah")
                        Halaman_admin()
                else:
                    Clear()
                    Tambah_Produk()
            elif Mau_Tambah == "2":
                Clear()
                print(" ============================================================ ")
                print(" ==                                                        == ")
                print(" ==             MENAMBAH JENIS PRODUK                      == ")
                print(" ==                                   [1] Tambah [0] Out   == ")
                print(" ============================================================ ")
                mytable =PrettyTable(["Id produk"," Jenis produk "])
                query = "select id_jenis_produk, jenis_produk from jenis_produk "
                cur.execute(query)
                data = cur.fetchall()
                for i in data:
                    mytable.add_row(i)
                print( mytable )
                print(" ============================================================ ")
                Lanjutkan = input("Pilihan anda: ")
                if Lanjutkan == "1":
                    try:
                        jenis_produk = input("Input jenis produk : ")
                        query = f"INSERT INTO jenis_produk (jenis_produk) VALUES ('{jenis_produk}')"
                        cur.execute(query, (jenis_produk))
                        conn.commit()
                        Clear()
                        print(" Anda berhasil menambahkan produk")
                        Halaman_admin()
                    except:
                        Clear()
                        print("Mohon maaf data yang anda inputkan salah")
                        Halaman_admin()
                else:
                    Clear()
                    Tambah_Produk()
                
            elif Mau_Tambah == "3":
                Clear()
                print(" ============================================================ ")
                print(" ==                                                        == ")
                print(" ==             MENAMBAH VARIAN PRODUK                     == ")
                print(" ==                                   [1] Tambah [0] Out   == ")
                print(" ============================================================ ")
                mytable =PrettyTable(["Id Varian produk"," Varian produk "])
                query = "select id_varian_produk, varian_produk from varian_produk "
                cur.execute(query)
                data = cur.fetchall()
                for i in data:
                    mytable.add_row(i)
                print( mytable )
                print(" ============================================================ ")
                Lanjutkan = input("Pilihan anda: ")
                if Lanjutkan == "1":
                    try:
                        varian_produk = input("Input varian produk : ")
                        query = f"INSERT INTO varian_produk (varian_produk) VALUES ('{varian_produk}')"
                        cur.execute(query, (varian_produk))
                        conn.commit
                        Clear()
                        print(" Anda berhasil menambahkan produk")
                        Halaman_admin()
                    except:
                        Clear()
                        print("Mohon maaf data yang anda inputkan salah")
                        Halaman_admin()
                else:
                    Clear()
                    Tambah_Produk()
            else :
                Clear()
                Halaman_admin()
        Tambah_Produk()
    elif Masuk == "2":
        Clear()
        def Riwayat_TP():
            print(" ============================================================ ")
            print(" ==                                                        == ")
            print(" ==                 INFORMASI PEMBELIAN                    == ")
            print(" ==             [1]PREORDER [2]ORDER [0]OUT                == ")
            print(" ==                                                        == ")
            print(" ============================================================ ")
            Info = input("Pilihlah angka untuk melanjutkan : ")
            if Info == "1":
                def riwayat_order_admin():
                    print("\n========= Riwayat Order Admin=========\n")
                    query_order = "SELECT d.id_detail_order, c.nama_customer, o.tanggal_order, sp.status_pesanan, p.produk, p.harga, d.jumlah_order, (p.harga*d.jumlah_order) as total_pembayaran, jp.jenis_pembayaran, c.alamat " \
                    "FROM orders o " \
                    "JOIN customer c ON(c.id_customer = o.id_customer) " \
                    "JOIN jenis_pembayaran jp ON(jp.id_jenis_pembayaran = o.id_jenis_pembayaran) " \
                    "JOIN status_pesanan sp ON(sp.id_status_pesanan = o.id_status_pesanan) " \
                    "JOIN detail_order d ON(d.id_order = o.id_order) " \
                    "JOIN produk p ON(p.id_produk = d.id_produk) " \
                    "ORDER BY o.tanggal_order ASC "  

                    cur.execute(query_order)
                    data = cur.fetchall()

                    table = PrettyTable()
                    table.field_names = ["ID Detail Order", "Nama Customer", "Tanggal Order", "Status Pesanan", "Produk", "Harga Produk", "Jumlah Order", "Total Pembayaran", "Jenis Pembayaran", "Alamat"]
                        
                    for row in data:
                        table.add_row(row)
                        
                        Clear()
                        print(table)

                        cur.close()
                        conn.close()
                riwayat_order_admin()
                Riwayat_TP()
            elif Info == "2":
                def riwayat_pre_order_admin():
                    print("\n========= Riwayat Pre Order Admin=========\n")
                    query_pre_order = "SELECT dp.id_detail_pre_order, c.nama_customer, po.tanggal_pre_order, sp.status_pesanan, p.produk, p.harga, dp.jumlah_pre_order, po.catatan_pesanan, (p.harga*dp.jumlah_pre_order) as total_pembayaran, jp.jenis_pembayaran, c.alamat " \
                                    "FROM pre_order po " \
                                    "JOIN customer c ON(c.id_customer = po.id_customer) " \
                                    "JOIN jenis_pembayaran jp ON(jp.id_jenis_pembayaran = po.id_jenis_pembayaran) " \
                                    "JOIN status_pesanan sp ON(sp.id_status_pesanan = po.id_status_pesanan) " \
                                    "JOIN detail_pre_order dp ON(dp.id_pre_order = po.id_pre_order) " \
                                    "JOIN produk p ON(p.id_produk = dp.id_produk) " \
                                    "ORDER BY po.tanggal_pre_order ASC "  

                    cur.execute(query_pre_order)
                    data = cur.fetchall()

                    table = PrettyTable()
                    table.field_names = ["ID Detail Pre Order", "Nama Customer", "Tanggal Pre Order", "Status Pesanan", "Produk", "Harga Produk", "Jumlah Pre Order", "Catatan Pesanan", "Total Pembayaran", "Jenis Pembayaran", "Alamat"]
                        
                    for row in data:
                        table.add_row(row)
                        
                        Clear()
                        print(table)

                        cur.close()
                        conn.close()

                Clear()
                riwayat_pre_order_admin()
                Halaman_admin()
            else :
                Clear()
                Halaman_admin()
    elif Masuk == "3":
        Clear()
        def Update_Bagian():
            print(" ============================================================ ")
            print(" ==                                                        == ")
            print(" ==                 UPDATE BAGIAN PRODUK                   == ")
            print(" ==            [1]PRODUK [2]JENIS [3]VARIAN [0] Out        == ")
            print(" ==                                                        == ")
            print(" ============================================================ ")
            Masuk_Update = input("Masukkan nomor sesuai dengan bagian yang ingin diupdate: ")
            if Masuk_Update == "1":
                Clear()
                query = "SELECT * FROM produk"
                cur.execute(query)
                data = cur.fetchall()
                nama_kolom = ["id_produk","Produk","Harga","Kadaluarsa","Gambar_Produk","id_jenis_produk"]
                df= pd.DataFrame(data,columns=nama_kolom)
                print(df)

                ngubah_produk = input(f"Masukkan nama produk: ") 
                id_produk = input(f'Masukkan id varinya :')
                query_mengubah = f"UPDATE produk SET produk = '{ngubah_produk}' WHERE id_produk = %s"
                kolom=(id_produk) 
                cur.execute(query_mengubah,kolom)
                conn.commit()
                print("========== Data berhasil diupdate ==========")
                Update_Bagian()
            elif Masuk_Update == "2":
                Clear()
                query = "SELECT * FROM jenis_produk"
                cur.execute(query)
                data = cur.fetchall()
                nama_kolom = ["id_jenis_produk","jenis_produk"]
                df= pd.DataFrame(data,columns=nama_kolom)
                print(df)

                ngubah_jenis = input(f"Masukkan Nama Jenis Produk: ") 
                id_varian = input(f'Masukkan idnya :')
                query_mengubah = f"UPDATE jenis_produk SET jenis_produk = '{ngubah_jenis}' WHERE id_jenis_produk = %s"
                kolom=(id_varian) 
                cur.execute(query_mengubah,kolom)
                conn.commit()
                print("========== Data berhasil diupdate ==========")
                
                Update_Bagian()
            elif Masuk_Update == "3":
                Clear()
                query = "SELECT * FROM varian_produk"
                cur.execute(query)
                data = cur.fetchall()
                nama_kolom = ["id_varian_produk","varian_produk"]
                df= pd.DataFrame(data,columns=nama_kolom)
                print(df)

                ngubah_varian = input(f"Masukkan nama varian: ") 
                id_varian = input(f'Masukkan idnya :')
                query_mengubah = f"UPDATE varian_produk SET varian_produk = '{ngubah_varian}' WHERE id_varian_produk = %s"
                kolom=(id_varian) 
                cur.execute(query_mengubah,kolom)
                conn.commit()
                print("========== Data berhasil diupdate ==========")

                Update_Bagian()
            elif Masuk_Update == "0":
                Clear()
                print("Mohon sesuaikan data anda")
                Update_Bagian()
            else: 
                Clear()
                Halaman_admin()
    elif Masuk == "4":
        Clear()
        def Perbarui_Status():
            print(" ============================================================ ")
            print(" ==                                                        == ")
            print(" ==                     PERBARUI STATUS                    == ")
            print(" ==  [1]STATUS ORDER [2]STATUS PRE ORDER [3]JENIS [0] Out  == ")
            print(" ==                                                        == ")
            print(" ============================================================ ")
            PS=input("Perbarui Status: ")
            
    elif Masuk == "5":
        Clear()
        def Menghapus():
            print(" ============================================================ ")
            print(" ==                                                        == ")
            print(" ==                 HAPUS BAGIAN PRODUK                    == ")
            print(" ==            [1]PRODUK [2]VARIAN [3]JENIS [0] Out        == ")
            print(" ==                                                        == ")
            print(" ============================================================ ")
            Hapus_tertentu = input("Masukkan nomor sesuai dengan nomor yang ingin dihapus: ")
            if Hapus_tertentu == "1":
                def read_Admin_menghapus_produk():
                    Clear()
                    def Melihat_produk(cur):
                        print(" ============================================================ ")
                        print("  --         Hapus produk yang tidak tersedia             -- ")
                        print(" ============================================================ ")
                        mytable =PrettyTable(["Id  produk", "Nama produk"," Harga "," Kadaluarsa ","Gambar produk", "Jenis produk"])
                        query = "select p.id_produk, p.produk, p.harga, TO_CHAR(p.kadaluarsa :: DATE,'dd-mm-yyyy'),p.gambar_produk, j.jenis_produk from produk p join jenis_produk j on (p.id_jenis_produk=j.id_jenis_produk)"
                        # query = "select p.id_produk, p.produk, p.harga, TO_CHAR(p.kadaluarsa :: DATE,'dd-mm-yyyy'),p.gambar_produk,
                        # j.jenis_produk from produk p join jenis_produk j on (p.id_jenis_produk=j.id_jenis_produk)"
                        cur.execute(query)
                        data = cur.fetchall()
                        for i in data:
                            mytable.add_row(i)
                        print(mytable)
                        print(" ============================================================ ")
                    Melihat_produk(cur)
                    while True:
                        id_van = input("Id produk yang ingin dihapus  : ")
                        query_delete = f"DELETE FROM produk produk WHERE id_produk = '{id_van}'"
                        try : 
                            cur.execute(query_delete)
                            conn.commit()
                            cur.close()
                            conn.close()
                            rows_deleted = cur.rowcount
                            if rows_deleted > 0 :
                                Clear()
                                print(" ============================================================ ")
                                print("               Anda berhasil menghapus varian produk")
                                print(" ============================================================ ")
                                break
                            else :
                                Clear()
                                print(" ============================================================ ")
                                print(" Mohon maaf data yang anda inputkan sedang terikat dengan ")
                                print(" data yang lainnya, Harap hapus data yang sedang tak terikat")
                                print(" ============================================================ ")
                                break
                        except psycopg2.Error or Exception:
                            Clear()
                            print(" ============================================================ ")
                            print(" ==  Terdapat kesalahan menghapus                             ")
                            print(" ============================================================ ")
                            print(" ==  Mohon memasukkan data anda dengan benar ")
                            print(" ============================================================ ")
                            break
                    read_Admin_menghapus_produk()
            elif Hapus_tertentu == "3":
                def read_Admin_menghapus_jenis():
                    Clear()
                    def Melihat_jenis_produk(cur):
                        print(" ============================================================ ")
                        print("  --           Hapus jenis yang tidak digunakan            -- ")
                        print(" ============================================================ ")
                        mytable =PrettyTable([" Id jenis produk ", " Nama jenis produk "])
                        query = "SELECT * FROM jenis_produk"
                        cur.execute(query)
                        data = cur.fetchall()
                        for i in data:
                            mytable.add_row(i)
                        print(mytable)
                        print(" ============================================================ ")
                    Melihat_jenis_produk(cur)
                    while True:
                        id_jen = input("Nomor jenis yang ingin dihapus  : ")
                        query_delete = f"DELETE FROM jenis_produk jenis_produk WHERE id_jenis_produk = '{id_jen}'"
                        try : 
                            cur.execute(query_delete)
                            conn.commit()
                            cur.close()
                            conn.close()
                            rows_deleted = cur.rowcount
                            if rows_deleted > 0 :
                                Clear()
                                print(" ============================================================ ")
                                print("               Anda berhasil menghapus jenis produk")
                                print(" ============================================================ ")
                                break
                            else :
                                Clear()
                                print(" ============================================================ ")
                                print(" Mohon maaf data yang diinputkan tidak ada,")
                                print(" Harap memasukkan data anda dengan benar")
                                print(" ============================================================ ")
                                break
                        except psycopg2.Error or Exception:
                            Clear()
                            print(" ============================================================ ")
                            print(" ==  Terdapat kesalahan menghapus, data bersifat terikat      ")
                            print(" ============================================================ ")
                            print(" ==  Mohon memasukkan data yang tidak terpakai                ")
                            print(" ============================================================ ")
                            break
                    read_Admin_menghapus_jenis()
            elif Hapus_tertentu == "2":
                def read_Admin_menghapus_varian():
                    Clear()
                    def Melihat_varian_produk(cur):
                        print(" ============================================================ ")
                        print("  --         Hapus varian yang tidak digunakan             -- ")
                        print(" ============================================================ ")
                        mytable =PrettyTable([" Id varian produk ", " Nama varian produk "])
                        query = "SELECT * FROM varian_produk"
                        cur.execute(query)
                        data = cur.fetchall()
                        for i in data:
                            mytable.add_row(i)
                        print(mytable)
                        print(" ============================================================ ")
                    Melihat_varian_produk(cur)
                    while True:
                        id_van = input("Nomor varian yang ingin dihapus  : ")
                        query_delete = f"DELETE FROM varian_produk varian_produk WHERE id_varian_produk = '{id_van}'"
                        try : 
                            cur.execute(query_delete)
                            conn.commit()
                            cur.close()
                            conn.close()
                            rows_deleted = cur.rowcount
                            if rows_deleted > 0 :
                                Clear()
                                print(" ============================================================ ")
                                print("               Anda berhasil menghapus varian produk")
                                print(" ============================================================ ")
                                break
                            else :
                                Clear()
                                print(" ============================================================ ")
                                print(" Mohon maaf data yang anda inputkan sedang terikat dengan ")
                                print(" data yang lainnya, Harap hapus data yang sedang tak terikat")
                                print(" ============================================================ ")
                                break
                        except psycopg2.Error or Exception:
                            Clear()
                            print(" ============================================================ ")
                            print(" ==  Terdapat kesalahan menghapus                             ")
                            print(" ============================================================ ")
                            print(" ==  Mohon memasukkan data anda dengan benar ")
                            print(" ============================================================ ")
                            break
                read_Admin_menghapus_varian()
                
            else :
                Clear()
                Halaman_admin()
    elif Masuk == "6":
        pass
    elif Masuk == "7":
        Clear()
        def Menu():
            Clear()
            print ("\u001b[33m+==============================+")
            print ("|        MENAMBAH JENIS PEMBAYARAN      |")
            print ("+==============================+\u001b[0m")
            Pilih = input ("\u001b[33m|1. Masukkan Jenis Pembayaran  |\n|2. Hapus Jenis Pembayaran     |\n|0. Keluar                     |\n\nPilih : \u001b[0m")
            print ('\u001b='*20)

            if Pilih == '1':
                query = "SELECT * FROM jenis_pembayaran"
                cur.execute(query)
                data = cur.fetchall()

                table = PrettyTable()
                table.field_names = ["id_jenis_pembayaran", "jenis_pembayaran"]
                for row in data:
                    table.add_row(row)
                print(table)

                    # Meminta input dari pengguna
                input_id_jenis_pembayaran = int(input("Masukkan Idnya : "))
                input_jenis_pembayaran = input("Masukkan Jenis Pembayaran\n ex : Dana, ShopeePay : ")
                input_kolom1 = input("Masukkan Nama Kolom Pertama: ")
                input_kolom2 = input("Masukkan Nama Kolom Kedua: ")
                input_kolom3 = input("Masukkan Nama Kolom Ketiga: ")

            #         # Buat tabel baru
                table_name = input("Masukkan Nama Tabel Baru: ")
                create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} (id_jenis_pembayaran INTEGER NOT NULL, {input_kolom1} VARCHAR(50) NOT NULL, {input_kolom2} VARCHAR(50) NOT NULL, {input_kolom3} VARCHAR(50) NOT NULL)"
                cur.execute(create_table_query)
                conn.commit()

            #         # Insert data ke tabel jenis_pembayaran
                query = "INSERT INTO jenis_pembayaran (id_jenis_pembayaran, jenis_pembayaran) VALUES (%s,%s)"
                cur.execute(query, (input_id_jenis_pembayaran, input_jenis_pembayaran))
                conn.commit()

            #         # Menampilkan data jenis_pembayaran setelah penambahan
                query = "SELECT * FROM jenis_pembayaran"
                cur.execute(query)
                data = cur.fetchall()

                table = PrettyTable()
                table.field_names = ["id_jenis_pembayaran", "jenis_pembayaran"]
                for row in data:
                    table.add_row(row)
                print(table)

                if Pilih == '2':
                    print ('='*20)
                    query = "SELECT * FROM jenis_pembayaran"
                    cur.execute(query)
                    data = cur.fetchall()
                    table = PrettyTable()
                    table.field_names = ["id_jenis_pembayaran", "jenis_pembayaran"]
                    for row in data:
                        table.add_row(row)
                    print(table)
                    print("Hapus Jenis Pembayaran")
                    input_id_jenis_pembayaran = int(input("Masukkan ID Jenis Pembayaran yang akan dihapus : "))
                    query_delete = f"DELETE FROM jenis_pembayaran WHERE id_jenis_pembayaran = {input_id_jenis_pembayaran}"
                    cur.execute(query_delete)
                    conn.commit()
                    query = "SELECT * FROM jenis_pembayaran"
                    cur.execute(query)
                    data = cur.fetchall()
                    table = PrettyTable()
                    table.field_names = ["id_jenis_pembayaran", "jenis_pembayaran"]
                    for row in data:
                        table.add_row(row)
                    print(table)

                elif Pilih == '0':
                    cur.close()
                    conn.close()
            Menu()
    elif Masuk == "0":
            Clear()
    else :
            Clear()
            print("Harap menginputkan data dengan benar")
            Halaman_user()

def Login():  
    print(" \u001b[31m============================================================ ")
    print(" ==                                                        == ")
    print(" ==         █▀▄▀█ █▀▀ █▄░█ █░█   █░░ █▀█ █▀▀ █ █▄░█        == ")
    print(" ==         █░▀░█ ██▄ █░▀█ █▄█   █▄▄ █▄█ █▄█ █ █░▀█        == ")
    print(" ==                                                        == ")
    print(" ============================================================\u001b[0m ")
    print(" ==  [1]   CUSTOMER                                        == ")
    print(" ==  [2]   ADMIN                                           == ")
    print(" ==  [3]   OUT                                             == ")
    print(" ============================================================ ")
    Masuk = input("Pilihlah akun kamu :  ")
    if Masuk == "1" :
        Clear()
        def Masuk_Login() :
            print(" \u001b[31m============================================================ ")
            print(" ==                                                        == ")
            print(" ==  █░░ █▀█ █▀▀ █ █▄░█   █▀▀ █░█ █▀ ▀█▀ █▀█ █▀▄▀█ █▀▀ █▀█ == ")
            print(" ==  █▄▄ █▄█ █▄█ █ █░▀█   █▄▄ █▄█ ▄█ ░█░ █▄█ █░▀░█ ██▄ █▀▄ ==")
            print(" ==                                                        == ")
            print(" ============================================================\u001b[0m ")
            username = input("Masukkan nama lengkap anda : ")
            password=input("Masukkan password anda : ")
            query = f"SELECT * FROM customer WHERE nama_customer = %s AND password_customer = %s"
            cur.execute(query, (username, password))
            user = cur.fetchone()
            if user:
                Clear()
                print(" ===    Selamat datang di Toko Primadona Jember    === ")
                global user_id
                user_id = user[0]
                Halaman_user()
            else:
                Clear()
                print("Mohon maaf akun atau password anda tidak sesuai")
                Login()
        Masuk_Login()


    elif Masuk == "2" :
        Clear()
        def Masuk_Login_Admin() :
            print(" \u001b[31m============================================================ ")
            print(" ==                                                        == ")
            print(" ==       █░░ █▀█ █▀▀ █ █▄░█   ▄▀█ █▀▄ █▀▄▀█ █ █▄░█        == ")
            print(" ==       █▄▄ █▄█ █▄█ █ █░▀█   █▀█ █▄▀ █░▀░█ █ █░▀█        == ")
            print(" ==                                                        == ")
            print(" ============================================================\u001b[0m ")
            username=input("Masukkan Username admin : ")
            password=input("Masukkan password admin : ")
            query = f"SELECT * FROM admin WHERE username = %s AND password_admin = %s"
            cur.execute(query, (username, password))
            user = cur.fetchone()
            if user:
                Clear()
                print(" ===    Selamat datang di Toko Primadona Jember    === ")
                Halaman_admin()
            else:
                Clear()
                print(" Mohon maaf akun Admin anda tidak valid ")
                Login()
        Masuk_Login_Admin()
        Clear()
    elif Masuk == "3" :
        Clear()
        Register_Login()
    else:
        Clear()
        print("Ketikkan sesuai perintah untuk dijalankan terlebih dahulu ")
        Login()
def Register_Customer():
    input_nama = input("Masukkan nama anda : ")
    input_pw = input("Masukkan password anda : ")
    input_no_telefon = input("Masukkan nomor telepon anda : ")
    input_alamat = input("Masukkan alamat anda : ")

    query = "SELECT * FROM customer WHERE nama_customer = %s OR no_telepon = %s"
    cur.execute(query, (input_nama, input_no_telefon))
    result = cur.fetchone()

    if result:
        Clear()
        print("Data User atau email atau nomor telefon yang anda masukkan telah digunakan. Sila coba lagi.")
    else:
        query = "INSERT INTO customer (nama_customer, no_telepon, password_customer, alamat) VALUES (%s, %s, %s, %s)"
        cur.execute(query, (input_nama, input_no_telefon, input_pw, input_alamat))
        conn.commit()
        Clear()
        print("Pendaftaran akun anda berhasil")

def Register():
    print(" \u001b[31m============================================================ ")
    print(" ==                                                        == ")
    print(" ==    █▀▄▀█ █▀▀ █▄░█ █░█   █▀█ █▀▀ █▀▀ █ █▀ ▀█▀ █▀▀ █▀█   == ")
    print(" ==    █░▀░█ ██▄ █░▀█ █▄█   █▀▄ ██▄ █▄█ █ ▄█ ░█░ ██▄ █▀▄   == ")
    print(" ==                                                        == ")
    print(" ============================================================\u001b[0m ")
    print(" \u001b[33m==                     MENU REGISTER                      == ")
    print(" ==    Selamat datang di menu register  Primadona Jember   == ")
    print(" ==            kami tunggu kehadiran kalian                == ")
    print(" ============================================================ ")
    print(" ==  [1]   MASUK                                           == ")
    print(" ==  [0]   OUT                                             == ")
    print(" ============================================================\u001b[0m ")
    Masuk=input("Menu register : ")
    if Masuk == "1":
        Register_Customer()
        Register()
    ## Rizale
    elif Masuk == "0" :
        Clear()
        Register_Login()
    else :
        Clear()
        print("Masukkan data dengan benar")
        Register()
        

def Register_Login():
    while True:
        Clear()
        print("")
        print("\u001b[33m████████╗░█████╗░██╗░░██╗░█████╗░  ██████╗░██████╗░██╗███╗░░░███╗░█████╗░██████╗░░█████╗░███╗░░██╗░█████╗░")
        print("╚══██╔══╝██╔══██╗██║░██╔╝██╔══██╗  ██╔══██╗██╔══██╗██║████╗░████║██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔══██╗")
        print("░░░██║░░░██║░░██║█████═╝░██║░░██║  ██████╔╝██████╔╝██║██╔████╔██║███████║██║░░██║██║░░██║██╔██╗██║███████║")
        print("░░░██║░░░██║░░██║██╔═██╗░██║░░██║  ██╔═══╝░██╔══██╗██║██║╚██╔╝██║██╔══██║██║░░██║██║░░██║██║╚████║██╔══██║")
        print("   ██║░░░╚█████╔╝██║░╚██╗╚█████╔╝  ██║░░░░░██║░░██║██║██║░╚═╝░██║██║░░██║██████╔╝╚█████╔╝██║░╚███║██║░░██║")
        print("   ╚═╝░░░░╚════╝░╚═╝░░╚═╝░╚════╝░  ╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝\u001b[0m")
        print("")
        print("\u001b[38;5;166m                         ============================================================= ")
        print("                         ==                                                         == ")
        print("                         == 🛒 SELAMAT DATANG DI WEBSITE TOKO PRIMADONA JEMBER 🧁   == ")
        print("                         ==                                                         == ")
        print("                         == disini kami menyediakan produk oleh-oleh jember yang    == ")
        print("                         == dapat kamu pesan dari rumah                             == ")
        print("                         ==                                                         == ")
        print("                         ==                                         [📧][📦][☎️ ]    == ")
        print("                         =============================================================")
        print("                         ==  [1]   LOGIN                                            ==")
        print("                         ==  [2]   REGISTER                                         ==")
        print("                         ==  [3]   OUT                                              ==")
        # print("                         ==  Masukkan berdasarkan angkanya                          ==")
        print("                         =============================================================\u001b[0;5;166m")
        Masuk = input("                         Sebelum berbelanja, ayo joinkan akun kamu :  ")
        if Masuk == "1" :
            Clear()
            Login()
        elif Masuk == "2" :
            Clear()
            Register()
            Register_Login()
        elif Masuk == "3" :
            Clear()
            break
        else:
            Clear()
            print("Lakukan sesuai perintah terlebih dahulu ")
            Register_Login()
Register_Login()