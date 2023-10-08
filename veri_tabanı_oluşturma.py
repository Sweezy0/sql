import sqlite3
con=sqlite3.connect("siirket.db")
cursor=con.cursor()
isim=input("Lütfen isminizi girin:")
soyisim=input("Lütfen soy isminizi girin:")
yas=int(input(("Lütfen yaşınızı girin:")))
adres=input("Lütfen adresinizi girin:")
maas=float(input("Lütfen maaşınızı girin:"))
def veri_gir(isim,soyisim,yas,adres,maas):
    cursor.execute("INSERT INTO elemanlar VALUES(?,?,?,?,?,?)",(None,isim,soyisim,yas,adres,maas))
    con.commit()
veri_gir(isim,soyisim,yas,adres,maas)
con.close()