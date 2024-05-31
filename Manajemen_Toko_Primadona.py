import psycopg2
import pandas as pd
import os
from prettytable import PrettyTable
from datetime import datetime
now = datetime.now()
date_time = now.strftime("%Y-%m-%d")

conn = psycopg2.connect(database='PRIMADONA', user='postgres', password='November1126', host='localhost', port='5432')
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
    Clear()
    print(" ============================================================ ")
    print(" ==                                                        == ")
    print(" ==            WEBSITE TOKO PRIMADONA JEMBER               == ")
    print(" ==                                                        == ")
    print(" ============================================================ ")
    print(" ==                                                        == ")
    print(" ==                                                        == ")
    print(" ==                                                        == ")
    print(" ==                                                        == ")
    print(" ============================================================ ")
    print(" ==  [1]   Informasi Produk                                == ")
    print(" ==  [2]   Order Produk                                    == ")
    print(" ==  [3]   Informasi Pengorderan Produk                    == ")
    print(" ==  [4]   Riwayat Orderan                                 == ")
    print(" ==  [5]   Profil                                          == ")
    print(" ==  [0]   OUT                                             == ")
    print(" ============================================================ ")
    
def Halaman_admin():
    Clear()
    print(" ============================================================ ")
    print(" ==                                                        == ")
    print(" ==      WEBSITE TOKO PRIMADONA JEMBER KHUSUS ADMIN        == ")
    print(" ==                                                        == ")
    print(" ============================================================ ")
    print(" ==  [1]   AKUN USER                                       == ")
    print(" ==  [2]   ADMIN                                           == ")
    print(" ==  [3]                                                   == ")
    print(" ==  [3]   OUT                                             == ")
    print(" ==  [3]   OUT                                             == ")
    print(" ==  [3]   OUT                                             == ")
    print(" ============================================================ ")
    
    
def Login():
    Clear()  
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
            Clear()
            print(" \u001b[31m============================================================ ")
            print(" ==                                                        == ")
            print(" ==           █░░ █▀█ █▀▀ █ █▄░█   █░█ █▀ █▀▀ █▀█          == ")
            print(" ==           █▄▄ █▄█ █▄█ █ █░▀█   █▄█ ▄█ ██▄ █▀▄          == ")
            print(" ==                                                        == ")
            print(" ============================================================\u001b[0m ")
            username=input("Masukkan Username anda : ")
            password=input("Masukkan password anda : ")
            query = f"SELECT * FROM customers WHERE username_customer AND password_customer"
            cur.execute(query, (username, password))
            user = cur.fetchone()
            if user in query:
                Clear()
                print(" === Selamat datang di Toko Primadona Jember === ")
            else:
                print("Anda salah")
        Masuk_Login()
                
        Halaman_user()
    elif Masuk == "2" :
        Halaman_admin() 
    elif Masuk == "3" :
        Clear()
        Register_Login()
    else:
        Clear()
        print("Ketikkan sesuai perintah untuk dijalankan terlebih dahulu ")
        Login()
def Register():
    Clear()
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
    print(" ==  [1]   USER                                            == ")
    print(" ==  [2]   ADMIN                                           == ")
    print(" ==  [3]   OUT                                             == ")
    print(" ============================================================\u001b[0m ")
    Masuk=input("Menu register : ")
    if Masuk == "1":
        Register_Login()
    elif Masuk == "2" :
        Register_Login()
    elif Masuk == "3" :
        Clear()
        Register_Login()
    else :
        Clear()
        Register()
def Register_Login ():
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
        Masuk = input("                         Sebelum berbelanja, ayo joinkan akun  kamu :  ")
        if Masuk == "1" :
            Clear()
            Login()
        elif Masuk == "2" :
            Register()
        elif Masuk == "3" :
            Clear()
            break
        else:
            Clear()
            print("Lakukan sesuai perintah terlebih dahulu ")
            Register_Login()
Register_Login()