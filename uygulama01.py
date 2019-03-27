puan = 0
print("Bilgeliği Temsil Eden Hayvanın Adı Nedir?")
n = input("Cevabınızı Giriniz : ").casefold()
if n == "Baykuş".casefold():
    puan += 20
    print("Cevabınız doğru, tebrikler!")
    print(str (puan) + " " + "Puan")
else:
    print("Cevabınız Yanlış")
    print(str(puan) + " " + "Puan")

print("Stary Night Tablosu Kime Aittir?")
n = input("Cevabınızı Giriniz : ").casefold()
if n == "Van Gogh".casefold():
    puan += 20
    print("Harika! Cevabınız Doğru")
    print(str(puan) + " " + "Puan")
else:
    print("Cevabınız Yanlış")
    print(str(puan) + " " + "Puan")

print("Kangal Köpeği İle Ünlü Şehrimiz Neresidir?")
n = input("Cevabınızı Giriniz : ").casefold()
if n == "Sivas".casefold():
    puan += 20
    print("Cevabınız doğru, tebrikler!")
    print(str(puan) + " " + "Puan")
else:
    print("Cevabınız Yanlış")
    print(str(puan) + " " + "Puan")

print("Somebody To Love Şarkısı Kime Aittir?")
n = input("Cevabınızı Giriniz : ").casefold()
if n == "Queen".casefold():
    puan += 20
    print("Cevabınız doğru, tebrikler!")
    print(str(puan) + " " + "Puan")
else:
    print("Cevabınız Yanlış")
    print(str(puan) + " " + "Puan")

print("Otostopçunun Galaksi Rehberi Adlı Kitapta 42 Hangi Anlama Gelmektedir?")
n = input("Cevabınızı Giriniz : ").casefold()
if n =="Hayatın evrenin ve her şeyin anlamı".casefold():
    puan += 20
    print("Cevabınız doğru, tebrikler!")
    print(str(puan) + " " + "Puan")
else:
    print("Cevabınız Yanlış")
    print(str(puan) + " " + "Puan")
input() #Buraya Dikkat, Bu Satır programın kapanmamasını sağlayacak.