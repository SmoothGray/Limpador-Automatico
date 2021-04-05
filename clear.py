import os
import time

contador = 0 
while True:
	os.system("cls")
	os.system(f"del /S /Q /F C:\\Windows\\Temp")
	os.system("cls")
	os.system(f"del /S /Q /F C:\\Users\\vinicius\\AppData\\Local\\Temp")
	os.system("cls")
	contador = contador +1
	if contador == 1:
		print(f"[+] Arquivos Temporarios Deletados pela {contador} vez")
	else:
		print(f"[+] Arquivos Temporarios Deletados pela {contador} vezes")
	time.sleep(60)