import time
import os

banner = """
███    ███ ███████ ██████  ██    ██ ███████  █████  
████  ████ ██      ██   ██ ██    ██ ██      ██   ██ 
██ ████ ██ █████   ██   ██ ██    ██ ███████ ███████ 
██  ██  ██ ██      ██   ██ ██    ██      ██ ██   ██ 
██      ██ ███████ ██████   ██████  ███████ ██   ██ 
                                                    

CS 1.6 Config Yapma Programi
Lorex tarafindan kodlanmistir.
Discord : lorex#1661
Size sorulan sorulara dogru cevap veriniz yoksa config calismaz!
Not : Onceden config olusturduysaniz onceki ayarlariniz silinecektir!
---------------------------------------------------------------
"""
os.system("color a")
os.system("title Medusa Config Programi")
print(banner)
sens = input("Fare Hassasiyeti Kac Olacaktir : ")
print("\n")
isim = input("Oyundaki Isminiz Ne olacaktir? : ")
print("\n")
adminsifresi = input("Admin sifreniz ne olacaktir? : ")
print("\n")
maxfpsdegeri = input("Maximum FPS Degeri Kac Olacaktir? : ")
print("\n")
vguimenu = input("Silah alma menusu yazili mi olsun resimli mi?\nYazili ise 0 Resimli Ise 1 yaziniz : ")
print("\n")
rawinput = input("Bu bir steam cs 1.6 kodudur eger crack indirdiyseniz sadece entere basiniz.\nMouse raw input etkinlestirilsin mi ?\nEtkinlestirecekseniz 1 etkinlestirmeyecekseniz 0 yaziniz : ")
print("\n")
fps = input("Bu bir steam cs 1.6 kodudur eger crack indirdiyseniz sadece entere basiniz.\nHareket izi etkinlestirilsin mi?\nEtkinlestirmek fps dususu yaratacaktir.\nEtkinlestirecekseniz 1 etkinlestirmeyecekseniz 0 yaziniz : ")
print("\n")
kaydet = input("Ayarlar kaydedilsin mi? y/n : ")
if kaydet =='n':
    os.system("cls")
    print("Ayarlar kaydedilmeden cikiliyor!")
    time.sleep(2)
sil = os.remove("Medusa.cfg")
olustur = open("Medusa.cfg" , "x") 
olustur.close()
save = open("medusa.cfg" , "w")

save.write("sensitivity "+sens)
save.write("\n")
save.write("name "+isim)
save.write("\n")
save.write("setinfo _pw "+adminsifresi)
save.write("\n")
save.write("fps_max "+maxfpsdegeri)
save.write("\n")
save.write("fps_modem "+maxfpsdegeri)
save.write("\n")
save.write("setinfo _vgui_menus "+vguimenu)
save.write("\n")
save.write("m_rawinput "+rawinput)
save.write("\n")
save.write("gl_vsync "+fps)
save.write("\n")
save.write("echo Medusa_Config_Ayarlari_Etkinlestirildi_!!")
save.write("\n")
save.write("speak activated")
kurulum = input("Ayarlar kaydedilmistir!\nKurulumun nasil yapildigini gormek ister misiniz? y/n : ")
if kurulum =='y':
 os.system("cls")
if kurulum =='n':
    os.system("cls")
    print("Ayarlar kaydedilmistir iyi oyunlar dileriz!")
    exit()
steam = input("Steamden mi giris yapiyorsunuz? y/n")
if steam =='y':
    os.system("cls")
    print("1 - Steami acin cs 1.6 oyununun ustune sag tiklayiniz.")
    print("2 - Ozelliklere tiklayiniz oradan yerel dosyalara gelip goz at diyoruz.")
    print("3 - Medusa.cfg dosyasini cstrikeye atiyoruz")
    print("4 - Oyuna girip konsola exec Medusa.cfg yaziyoruz!")
    print("5 - Config dosyamiz aktiflestirilmistir gule gule kullanabilirsiniz!\n\n")
    print("[!] Bu ekran 15 saniye icinde kapanacaktir.")
    time.sleep(15)
if steam =='n':
    os.system("cls")
    print("1 - Masaustunde kisayol varsa sag tiklayip dosya konumunu ac diyoruz.")
    print("2 - Kisayol yoksa baslata Counter yaziyoruz oyun zaten cikacaktir sag tiklayip dosya konumunu ac diyoruz.")
    print("3 - Medusa.cfg dosyasini cstrikeye atiyoruz.")
    print("4 - Oyuna girip konsola exec Medusa.cfg yaziyoruz")
    print("5 - Config dosyamiz aktiflestirilmistir gule gule kullanabilirsiniz!\n\n")
    print("[!] Bu ekran 15 saniye icinde kapanacaktir.")
    time.sleep(15)
