ana_branş = ("Yazılım", "Tasarım", "Pazarlama")
tum_ogrenciler = []
ogrenci1 = ["Ahmet", ["Pazarlama"]]
ogrenci2 = ["Mehmet", ["Yazılım"]]
ogrenci3 = ["Mustafa", ["Tasarım"]]

tum_ogrenciler.append(ogrenci1)
tum_ogrenciler.append(ogrenci2)
tum_ogrenciler.append(ogrenci3)

baskan = ["Başkan", ["Yazılım"]]
tum_ogrenciler.insert(0,baskan)
print("toplam kayıtlı öğrenci sayısı: ", len(tum_ogrenciler))

silinecek_isim = input("Kulüpten ayrılacak öğrencinin adını giriniz: ").strip()

silinen_öğrenci = False

for ogrenci in tum_ogrenciler:
    if ogrenci[0] == silinecek_isim:
        tum_ogrenciler.remove(ogrenci)
        silinen_öğrenci = True

if silinen_öğrenci:
    print("öğrenci silindi: ", silinecek_isim)
else:
    print("öğrenci silinmedi.")

son_öğrenciyi_çıkarma = tum_ogrenciler.pop()
print("en son silinen öğrenci: ", son_öğrenciyi_çıkarma[0])

öğrenci_burak = ["Burak Tan", ["Tasarım"]]
tum_ogrenciler.append(öğrenci_burak)

geçici_sıralama = sorted(tum_ogrenciler)
print("alfabetik olarak geçici sıralama: ", geçici_sıralama)
print("değişmediğinin kanıtı: ", tum_ogrenciler)

tum_ogrenciler.sort()
print("kalıcı olarak değişmiş hali: ", tum_ogrenciler)