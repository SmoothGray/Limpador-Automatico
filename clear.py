# Para iniciar com o windows, dê win + r e coloque "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup"


import os
import time

os.system("title Cleaner")


delay = 60 #Coloque seu Delay aqui (segundos)
contador = 0 
while True:
	os.system("cls")
	os.system(f"del /S /Q /F C:\\Windows\\Temp")
	os.system("cls")
	os.system(f"del /S /Q /F C:\\Users\\vinicius\\AppData\\Local\\Temp")
	os.system("cls")
	contador = contador +1
	print(f"[+] levas de limpeza: {contador}")
	time.sleep(delay)
