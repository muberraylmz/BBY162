__author__="Müberra Yılmaz"
""" 03.04.2019 / place:Beytepe Kampüsü, Parlar Cafe, Caribou Cafe, Yelken Cafe / with Sabina Amrahova"""
sorular = ['Bilgeliği Temsil Eden Hayvanın Adı Nedir?',
            '"Stary Night" Tablosu Kime Aittir?',
            'Kangal Köpeği İle Ünlü Şehrimiz Aşağıdakilerden Hangisidir?',
            '"Somebody To Love" Şarkısı Kime Aittir?',
            'Otostopçunun Galaksi Rehberi Adlı Kitapta "42" Hangi Anlama Gelmektedir?']
cevaplar = ['D', 'A', 'E', 'B', 'C']
cevapA = ['At', 'Vincent Van Gogh', 'Adana', 'The Beatles', 'Mutluluk']
cevapB = ['Kedi', 'Pablo Picasso', 'Bursa', 'Queen', 'Para']
cevapC = ['Köpek', 'Leonardo Da Vinci', 'Van', 'Coldplay', 'Hayatın, evrenin ve her şeyin anlamı']
cevapD = ['Baykuş', 'Michelangelo', 'Tekirdağ', 'AC/DC', 'Huzur']
cevapE = ['Balık', 'Salvador Dali', 'Sivas', 'Pink Floyd', 'Baharın gelişi']
puan = 0
for i in range(len(sorular)):
    print("Soru " + str(i+1)+":"+sorular[i])
    print("A.) " + cevapA[i])
    print("B.) " + cevapB[i])
    print("C.) " + cevapC[i])
    print("D.) " + cevapD[i])
    print("E.) " + cevapE[i])
    cevap = input("Cevabınızı Giriniz: ")
    if cevaplar[i] == cevap.upper():
        puan +=1
print("Testi Tamamladınız")
print("Aldığınız not: " +str(int((puan/len(sorular))*100)))
input() #Buraya Dikkat, Bu Satır programın kapanmamasını sağlayacak.