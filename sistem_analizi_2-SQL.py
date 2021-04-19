import speech_recognition as sr
from gtts import gTTS
import os
import sys
import pyttsx3
from playsound import playsound
import random
import time
import mysql.connector
import getpass
import sistem_analizi_program

r = sr.Recognizer()

kullanici_sesli_bilgi = [] #kisinin sesli girdisi kayit edilir satir 167


def kayit():
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
         voice = r.recognize_google(audio,language='tr-TR')

        except sr.UnknownValueError:
            print("seni algilayamadim")
            
        except sr.RequestError:
            print("sistem calismiyor")

        return voice

    """gelen veriyi oku fonksiyon """

def soyle(string):
    tts = gTTS(string,lang='tr')
    rand = random.randint(1,10000)
    file = "ses-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

soyle("sistem arayüzüne hoşgeldiniz ")
print("""
        1-Kullanici Giris
        2-Kullanici Kayit
    """)
soyle("Yapmak istenilen işlemin numarasini girin")

islem = int(input(":"))
if islem == 1:
    soyle("Merhaba kayitli kullanici kullanici bilgilerinizi giriniz:")
    def vericek():
        baglanti = mysql.connector.connect(
        host = "local",
        user = "root",
        password = "",
        database = "proje_kullanicilari"
        )
        liste = []

        cursor = baglanti.cursor ()

        veriler = cursor.execute('SELECT * From kullanici_listesi')
        result = cursor.fetchall()
        
        for degerler in result:
            liste.append(degerler)
        print(liste)

        uzunluk = len(liste)
        print(f'listenin uzunlugu: {uzunluk} adet veriden olusmaktadir')

        kullanici_nick = input("id: ")
        kullanici_passwd = getpass.getpass(prompt="password:")


        soyle("alınan veriler analiz ediliyor")
        time.sleep(1)
        liste1 = []

        c = 0
        i = 0

        while i <= uzunluk:
            try:
                aranan_username = kullanici_nick in liste[c]
                aranan_sifre = kullanici_passwd in liste[c]

                if (aranan_username == True) and (aranan_sifre == True):
                    soyle(f'girilen degerin bulundugu satır{c}')
                    print("degerlerin bulundugu satırlar ekrana yazılıyor")
                    time.sleep(1)
                    print(liste[c])
                    
                    for satir in liste[c]:
                        liste1.append(satir)
                    break

                elif (aranan_username ==False) or (aranan_sifre == False):
                    c+=1
                i+=1
            except IndexError:
                break

        try:
            print(f'degerlerin bulundugu liste:{c} . satır')       
            
            if(liste1[4] == kullanici_nick) and (liste1[5]==kullanici_passwd):
                print("sistemde kayitli bir kullanicisiniz")
            elif(liste1[4] == kullanici_nick) and (liste1[5]!=kullanici_passwd):
                print("hatali sifre girdiniz")
            elif(liste1[4] != kullanici_nick) and(liste1[5] ==kullanici_passwd):
                print("hatali kullanici adi")
            
            kisi_isim = liste1[0]
            kisi_soyad = liste1[1]
            kisi_nick = liste1[2]
            kisi_sifre = liste1[3]
            kisi_posta = liste1[4]


            kisiler ={
                "kisi_adi": kisi_isim,
                "kisi_soyadi": kisi_soyad,
                "kisi_username":kisi_nick,
                "kisi_password": kisi_sifre,
                "kisi_eposta" : kisi_posta
            }
        except IndexError:
            print("hata var")
    vericek()

elif islem==2:
    kullanici_verileri = {}  #kullanicinin bilgileri sözlük halinde tutulur
    soyle("Burada mikrofonunuzun aktif olması gerekir mikrofonunuz aktif  ise '1' değil ise '2' giriniz")
    islem2 = int(input(":"))
    def Kullanici_ekle(Kisi_bilgi_isim,Kisi_bilgi_soyad,Kisi_bilgi_kisisel_kimlik,Kisi_bilgi_sifre,Kisi_bilgi_posta):
        connection = mysql.connector.connect(
        host = "local", user ="root", password ="", database = "proje_kullanicilari" 
        )
        cursor = connection.cursor()

        sql = "INSERT INTO kullanici_listesi(kullanici_isim,kullanici_soyisim,kullanici_nick,kullanici_sifre,kullanici_eposta) VALUES (%s,%s,%s,%s,%s)"
        values = (Kisi_bilgi_isim,Kisi_bilgi_soyad,Kisi_bilgi_kisisel_kimlik,Kisi_bilgi_sifre,Kisi_bilgi_posta)
        cursor.execute(sql,values)


        try:
            connection.commit()
            print(f'{cursor.rowcount} tane kayit eklendi')
            print(f'son eklenen kaydin id:{cursor.lastrowid}')
        except mysql.connector.Error as err:
            print("hata:",err)
        
        finally:
            connection.close()
            print("database baglantisi kapandi")
    

    
    if islem2 == 1:
        i = 1
        while i <6:
            if i ==1:
                try:
                    soyle("isminizi soyleyiniz: ")
                    sesler = kayit()

                    dosya = open("ses.txt","a",encoding="utf-8")
                    dosya.write(sesler)
                    dosya.close()
                    kullanici_sesli_bilgi.append(sesler)
                    kullanici_verileri["kullanici_adi"] = sesler
                    i+=1
                except UnboundLocalError:
                    print("1. except blogu aktif")
                    time.sleep(0.5)
                    kullanici_Adi_M = input("isim giriniz..s")
                    dosya = open("sex.txt","a",encoding="utf-8")
                    dosya.write(kullanici_Adi_M)
                    dosya.close()
                    kullanici_verileri["kullanici_adi"] = kullanici_Adi_M
                    i+=1
            elif i ==2:
                try:
                    print("ikinci blok calisti")
                    soyle("soy isminizi soyleyiniz..")
                    sesler = kayit()
                    dosya = open("ses.txt","a",encoding="utf-8")
                    dosya.write(sesler)
                    dosya.close()
                    kullanici_sesli_bilgi.append(sesler)
                    kullanici_verileri["kullanici_soyad"] = sesler
                    i+=1
                except UnboundLocalError:
                    print("2. except blogu aktif")
                    time.sleep(0.5)
                    kullanici_Soyad_M = input("Soyad giriniz: ")
                    dosya = open("ses.txt","a",encoding="utf-8")
                    dosya.write(kullanici_Soyad_M)
                    dosya.close()
                    kullanici_verileri["kullanici_soyad"]=kullanici_Soyad_M
                    i+=1
            elif i ==3:
                try:
                    print("ucuncu blok calisti")
                    soyle("kullanici adinizi soyleyiniz..")
                    sesler = kayit()
                    dosya = open("ses.txt","a",encoding="utf-8")
                    dosya.write(sesler)
                    dosya.close()
                    kullanici_sesli_bilgi.append(sesler)
                    kullanici_verileri["kullanici_nick"] = sesler
                    i+=1
                except UnboundLocalError:
                    print("3. except blogu aktif")
                    time.sleep(0.5)
                    kullanici_username_M = input("Username giriniz: ")
                    dosya = open("ses.txt","a",encoding="utf-8")
                    dosya.write(kullanici_username_M)
                    dosya.close()
                    kullanici_verileri["kullanici_nick"] = kullanici_username_M
                    i+=1
            elif i ==4:
                try:
                    print("dorduncu blok calisti")
                    soyle("password giriniz:")
                    sesler = kayit()
                    dosya = open("ses.txt","a",encoding="utf-8")
                    dosya.write(sesler)
                    dosya.close()
                    kullanici_sesli_bilgi.append(sesler)
                    kullanici_verileri["Kullanici_pswd"] = sesler
                    i+=1

                except UnboundLocalError as err:
                
                    print("4. except blogu aktif")
                    time.sleep(0.5)
                    kullanici_pswd_M = input("psswd giriniz: ")
                    dosya = open("ses.txt","a",encoding="utf-8")
                    dosya.write(kullanici_pswd_M)
                    dosya.close()
                    kullanici_verileri["Kullanici_pswd"] = kullanici_pswd_M
                    i+=1

            elif i ==5:
                try:
                    print("besinci blok calisti")
                    soyle("elektronik posta adresinizi soyleyiniz")
                    sesler = kayit()
                    dosya =  open("ses.txt","a",encoding="utf-8")
                    dosya.write(sesler)
                    dosya.close()
                    kullanici_verileri["Kullanici_posta"] = sesler
                    i+=1
                except UnboundLocalError:
                    print("besinci except calisti")
                    soyle("lutfen elektronik posta adresinizi girin")
                    eposta = input("lutfen elektronik posta adresinizi giriniz: ")
                    dosya = open("ses.txt","a",encoding="utf-8")
                    dosya.write(eposta)
                    dosya.close()
                    kullanici_verileri["Kullanici_posta"] = eposta
                    i+=1
            else:
                break
        
        Kisi_bilgi_isim = kullanici_verileri["kullanici_adi"]
        Kisi_bilgi_soyad = kullanici_verileri["kullanici_soyad"]
        Kisi_bilgi_kisisel_kimlik = kullanici_verileri["kullanici_nick"]
        Kisi_bilgi_sifre = kullanici_verileri["Kullanici_pswd"]
        Kisi_bilgi_posta = kullanici_verileri["Kullanici_posta"]
        print(kullanici_verileri)
        Kullanici_ekle(Kisi_bilgi_isim,Kisi_bilgi_soyad,Kisi_bilgi_kisisel_kimlik,Kisi_bilgi_sifre,Kisi_bilgi_posta)
    
    elif islem2 == 2:
        soyle("Manuel giris ekranına hosgeldiniz")

        kullanici_verileri_2 = {}

        j = 1
        soyle("lütfen İSTENİLEN BİLGİLERİ GİRİNİZ")
        print("_____________MANUEL GİRİS______________")

        while j <6:
            if j ==1:
                kisinin_adi_manuel = input("isim: ")
                kullanici_verileri_2["Kisi_isim"] = kisinin_adi_manuel
                j+=1
            
            elif j ==2:
                kisinin_soyadi_manuel = input("soyad: ")
                kullanici_verileri_2["Kisi_soyad"] = kisinin_soyadi_manuel
                j+=1
            
            elif j ==3:     
                kisinin_niki_manuel = input("nick: ")
                kullanici_verileri_2["Kisi_nick"] = kisinin_niki_manuel
                j+=1
            
            elif j ==4:
                kisinin_psswd_manuel = input("password: ")
                kullanici_verileri_2["Kisi_password"] = kisinin_psswd_manuel
                j+=1
            
            elif j == 5:
                kisinin_posta_manuel = input("posta: ")
                kullanici_verileri_2["Kisi_posta"] = kisinin_posta_manuel
                j+=1
            
            elif j ==6:
                break

        Kisinin_Adi_Manuel = kullanici_verileri_2["Kisi_isim"]
        Kisinin_Soyadi_Manuel = kullanici_verileri_2["Kisi_soyad"]
        Kisinin_nick_Manuel = kullanici_verileri_2["Kisi_nick"]
        Kisinin_psswd_Manuel = kullanici_verileri_2["Kisi_password"]
        Kisinin_posta_Manuel = kullanici_verileri_2["Kisi_posta"]
        
    Kullanici_ekle(Kisinin_Adi_Manuel,Kisinin_Soyadi_Manuel,Kisinin_nick_Manuel,Kisinin_psswd_Manuel,Kisinin_posta_Manuel)

elif islem ==3:
    sistem_analizi_program.window()