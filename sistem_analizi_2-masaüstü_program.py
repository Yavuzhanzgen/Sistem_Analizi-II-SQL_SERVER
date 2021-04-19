import sys
import mysql.connector
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
import time

kullanici_veri={}

def Pc_arayuz(kullanici_ismi,kullanici_soyisim,kullanici_nick,kullanici_sifre,kullanici_posta):
    connection = mysql.connector.connect(
        host = "local",
        user = "root",
        password = "",
        database = "proje_kullanicilari"
    )
    cursor = connection.cursor()

    sql = "INSERT INTO kullanici_listesi(kullanici_isim,kullanici_soyisim,kullanici_nick,kullanici_sifre,kullanici_eposta) VALUES (%s,%s,%s,%s,%s)"
    values = (kullanici_ismi,kullanici_soyisim,kullanici_nick,kullanici_sifre,kullanici_posta)
    cursor.execute(sql, values)

    try:
        connection.commit()
        print(f'{cursor.rowcount} tane kayit eklendi')
        print(f'son eklenen kaydin id:{cursor.lastrowid}')
    except mysql.connector.Error as err:
        print("hata",err)
    finally:
        connection.close()
        print("database baglantisi kapandi")
    
def window():
    app= QApplication(sys.argv) # app degiskenine sistem agünmanların hepsini verir
    win =QMainWindow() # ana ekranı windows degiskenine atar


    def K_ekle(self):
        print("veriler ekleniyor...")
        time.sleep(2)
        print("eklenen veriler")
        print(f'isim: {txt_K_isim.text()} soyad:{txt_K_Soyisim.text()} nick: {txt_K_Nick.text()} sifre:{txt_K_Sifre.text()}')
        
        kullanici_veri["kullanici_adi"] = txt_K_isim.text()
        kullanici_veri["kullanici_soyad"] = txt_K_Soyisim.text()
        kullanici_veri["kullanici_nick"] = txt_K_Nick.text()
        kullanici_veri["kullanici_sifre"] = txt_K_Sifre.text()
        kullanici_veri["kullanici_posta"] = txt_K_Posta.text()

        kullanici_ismi = kullanici_veri["kullanici_adi"]
        kullanici_soyisim = kullanici_veri["kullanici_soyad"]
        kullanici_nick = kullanici_veri["kullanici_nick"]
        kullanici_sifre = kullanici_veri["kullanici_sifre"]
        kullanici_posta = kullanici_veri["kullanici_posta"]
        
        Pc_arayuz(kullanici_ismi,kullanici_soyisim,kullanici_nick,kullanici_sifre,kullanici_posta)
        sys.exit()
    win.setWindowTitle("api admin kayit") #tablonun adini degistirir
    win.setGeometry(100,100,300,300) # pencere ayarini yapar
    win.setWindowIcon(QIcon("mikrofon.jpg")) #tabloya icon verir
   
    lbl_K_isim = QtWidgets.QLabel(win)
    lbl_K_isim.setText("İsminiz: ")
    lbl_K_isim.move(10,10)

    txt_K_isim = QtWidgets.QLineEdit(win)
    txt_K_isim.move(110,10)

    lbl_K_soyisim = QtWidgets.QLabel(win)
    lbl_K_soyisim.setText("Soy isminiz: ")
    lbl_K_soyisim.move(10,50)

    txt_K_Soyisim = QtWidgets.QLineEdit(win)
    txt_K_Soyisim.move(110,50)

    lbl_K_nick = QtWidgets.QLabel(win)
    lbl_K_nick.setText("Kullanici adi:")
    lbl_K_nick.move(10,90)

    txt_K_Nick = QtWidgets.QLineEdit(win)
    txt_K_Nick.move(110,90)

    lbl_K_sifre = QtWidgets.QLabel(win)
    lbl_K_sifre.setText("Sifrenizi giriniz:")
    lbl_K_sifre.move(10,130)

    txt_K_Sifre = QtWidgets.QLineEdit(win)
    txt_K_Sifre.move(110,130)

    lbl_K_Posta = QtWidgets.QLabel(win)
    lbl_K_Posta.setText("Sifrenizi giriniz:")
    lbl_K_Posta.move(10,170)

    txt_K_Posta = QtWidgets.QLineEdit(win)
    txt_K_Posta.move(110,170)


    btn_kayit = QtWidgets.QPushButton(win)
    btn_kayit.setText("KAYİT OL")
    btn_kayit.move(110,230)
    btn_kayit.clicked.connect(K_ekle)

    win.show() #tasariyi gösterir
    sys.exit(app.exec_()) # çıkış yapma yeri ekler kırmızı çarpı

    admin_kullanci_veri ={
        "kisi adi": txt_K_isim,
        "kisi soyad" : txt_K_Soyisim,
        "kisi nick" : txt_K_Nick,
        "kisi sifre" : txt_K_Sifre
    }
    print(kullanici_veri)
