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
    print(" ==  [4]   Searching produk                                == ")
    print(" ==  [5]   Feedback                                        == ")
    print(" ==  [0]   OUT                                             == ")
    print(" ==  [ Untuk masuk inputkan berdasarkan angka ]            == ")
    print(" ============================================================ ")
    Masuk = input(" == Halaman masuk :")
    if Masuk == "1":
        pass
    elif Masuk == "2":
        pass
    elif Masuk == "3":
        pass
    elif Masuk == "4":
        pass
    elif Masuk == "5":
        pass
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
                query = "select id_jenis_produk, jenis_produk from produk "
                cur.execute(query)
                data = cur.fetchall()
                for i in data:
                    mytable.add_row(i)
                print( mytable )
                print(" ============================================================ ")
                Lanjutkan = input("Pilihan anda: ")
                if Lanjutkan == "1":
                    pass
                else:
                    Clear()
                    Tambah_Produk()
                
            elif Mau_Tambah == "3":
                print(" ============================================================ ")
                print(" ==                                                        == ")
                print(" ==             MENAMBAH VARIAN PRODUK                     == ")
                print(" ==                                   [1] Tambah [0] Out   == ")
                print(" ============================================================ ")
                mytable =PrettyTable(["Id Varian produk"," Varian produk "])
                query = "select id_varian_produk, varian_produk from produk "
                cur.execute(query)
                data = cur.fetchall()
                for i in data:
                    mytable.add_row(i)
                print( mytable )
                print(" ============================================================ ")
                Lanjutkan = input("Pilihan anda: ")
                if Lanjutkan == "1":
                    
                    pass
                else:
                    Clear()
                    Tambah_Produk()
            else :
                Clear()
                Halaman_admin()
        Tambah_Produk()
    elif Masuk == "2":
        pass
    elif Masuk == "3":
        pass
    elif Masuk == "4":
        pass
    elif Masuk == "5":
        pass
    elif Masuk == "6":
        pass
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
    print(" ==  [1]   USER                                            == ")
    print(" ==  [2]   ADMIN                                           == ")
    print(" ==  [3]   OUT                                             == ")
    print(" ============================================================ ")
    Masuk = input("Pilihlah akun kamu :  ")
    if Masuk == "1" :
        Clear()
        def Masuk_Login() :
            print(" \u001b[31m============================================================ ")
            print(" ==                                                        == ")
            print(" ==           █░░ █▀█ █▀▀ █ █▄░█   █░█ █▀ █▀▀ █▀█          == ")
            print(" ==           █▄▄ █▄█ █▄█ █ █░▀█   █▄█ ▄█ ██▄ █▀▄          == ")
            print(" ==                                                        == ")
            print(" ============================================================\u001b[0m ")
            username = input("Masukkan Username anda : ")
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
    input_nama = input("Masukkan username anda : ")
    input_pw = input("Masukkan password anda : ")
    input_no_telefon = input("Masukkan nomor telefon anda : ")
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