import time
import os

banner = """
███    ███ ███████ ██████  ██    ██ ███████  █████  
████  ████ ██      ██   ██ ██    ██ ██      ██   ██ 
██ ████ ██ █████   ██   ██ ██    ██ ███████ ███████ 
██  ██  ██ ██      ██   ██ ██    ██      ██ ██   ██ 
██      ██ ███████ ██████   ██████  ███████ ██   ██ 
                                                    

CS 1.6 Config Application
Coded by lorex.
YouTube : https://youtube.com/@lorex7337
Note : If you created before a config file this file deleting.
---------------------------------------------------------------
"""
os.system("color a")
os.system("title Medusa Config Application")
print(banner)
sens = input("Mouse sensitivity : ")
print("\n")
isim = input("Player name : ")
print("\n")
adminsifresi = input("Admin password : ")
print("\n")
maxfpsdegeri = input("Max fps limit : ")
print("\n")
vguimenu = input("Buy menu for visual type 1 for written type 0 : ")
print("\n")
rawinput = input("This code for steam cs.16 if your non-steam click enter. \nMouse raw input?\nFor activation type 1 if not type 0 : ")
print("\n")
fps = input("This code for steam cs.16 if your non-steam click enter.\nEnable motion trail?\nEnable it will create fps drop.\nFor activation type 1 if not type 0 : ")
print("\n")
kaydet = input("Save settings? y/n : ")
if kaydet =='n':
    os.system("cls")
    print("Setting not saved!")
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
save.write("fps_override 1")
save.write("\n")
save.write("echo Activated!")
save.write("\n")
save.write("speak activated")
kurulum = input("Settings saved!\nWant to learn how to enable the config file? y/n : ")
if kurulum =='y':
 os.system("cls")
if kurulum =='n':
    os.system("cls")
    print("Settings saved! Have a good day ^^")
    exit()
steam = input("Are you logging in from steam? y/n")
if steam =='y':
    os.system("cls")
    print("1 - Open Steam right click counter strike.")
    print("2 - Click features")
    print("3 - Copy Medusa.cfg file and paste cstrike folder.")
    print("4 - Open counter and type this to console : exec Medusa.cfg")
    print("5 - Congrulations config activated!\n\n")
    print("[!] This screen will closing in 15 seconds.")
    time.sleep(15)
if steam =='n':
    os.system("cls")
    print("1 - Open cs file location.")
    print("3 - Copy Medusa.cfg file and paste cstrike folder.")
    print("4 - Open counter and type this to console : exec Medusa.cfg")
    print("5 - Congrulations config activated !\n\n")
    print("[!] This screen will closing in 15 seconds.")
    time.sleep(15)
