#!/usr/bin/python
# NOTAS: Para iniciar com o windows, dê win + r e coloque "%AppData%\Microsoft\Windows\Start Menu\Programs\Startup" e coloque seu arquivo para iniciar junto com o win


import os # não mude nada aqui
import time # não mude nada aqui



def upgrade():
	os.system("cls")
	print("[+] Updating")
	os.system("py -m pip install --upgrade pip")
	os.system("cls")
	
	
upgrade()
os.system("title Cleaner")
def main():
	delay = 60 # Coloque seu Delay aqui (segundos)
	# não mude nada daqui pra frente
	contador = 0 
	while True:
	  os.system("cls")
	  os.system(f"del /S /Q /F %AppData%\\Local\\Temp\n")
	  os.system(f"del /S /Q /F C:\\Windows\\Temp\n")
	  os.system("cls")
	  contador = contador +1
	  print(f"[+] levas de limpeza: {contador}")
	  time.sleep(delay)
main()
