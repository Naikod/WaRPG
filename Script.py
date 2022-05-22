import random
import time
from os import system, name
from datetime import datetime
abc = False

if abc == False:
    	## data section
	myCrit = [60, 30, 10]
	BattleMode = False
	PriceData = [250, 550, 950]
	myHealth = [100, 150 ,250]
	myArmor = [50, 60, 75]
	myStrength = [10, 30, 60]
	lvDarah = 0
	lvArmod = 0
	lvKekuatan = 0
	lvCrit = 0
	myCoin = 10
	abc = True
	
## game section
def Upgrade(item, lv, price):
	global myCoin,lvDarah,lvArmod,lvKekuatan,lvCrit
	confirm = input("Are you sure to trade? y/n\n")
	if confirm == 'y' or confirm == 'Y':
		myCoin = myCoin - price
		if item == 1:
			if lv == 1:
				lvDarah = lv
			elif lv == 2:
				lvDarah = lv
		elif item == 2:
			if lv == 1:
				lvArmod = lv
			elif lv == 2:
				lvArmod = lv
		elif item == 3:
			if lv == 1:
				lvKekuatan = lv
			elif lv == 2:
				lvKekuatan = lv
		elif item == 4:
			if lv == 1:
				lvCrit = lv
			elif lv == 2:
				lvCrit = lv
		print("Successfully bought")
	elif confirm == 'n' or confirm == 'N':
		MenuExit = input("Ketik apapun untuk keluar\n")
	
print("Welcome to the adventure!")

while abc == True:
	system("cls")
	print("Statsmu: ")
	print("Darah:        ",myHealth[lvDarah])
	print("Armod:        ",myArmor[lvArmod])
	print("Kekuatan:     ",myStrength[lvKekuatan])
	print("Critical:     ",myCrit[lvCrit])
	print("Battle Point: ",myCoin)
	MainMenu = input("\nPilih lah menu:\n[info] Information\n[1] Upgrade Stats\n[2] Battle\n[3] Upcoming Update")
	if MainMenu == "1":
		system("cls")
		print("\nSelamat Datang Di WanStore!")
		print("Berikut Katalog Kami:")
		print("[1]Darah Level 2:550BP:HP150")
		print("[2]Darah Level 3:950BP:HP250")
		print("[3]Armor Level 2:550BP:armor60")
		print("[4]Armor Level 3:950BP:armor75")
		print("[5]Kekuatan Level 2:550BP:kekuatan30")
		print("[6]Kekuatan Level 3:950BP:kekuatan60")
		print("[7]Critical Level 2:550BP:Crit 70%")
		print("[8]Critical Level 3:950BP:Crit 90%")
		storemenu = input("Pilih lah salah satu! atau ketik exit untuk keluar\n")
		if storemenu == "1":
			if myCoin > PriceData[1]:
				Upgrade(1, 1, PriceData[1])
			else:
				MenuExit = input("Uang anda tidak cukup!\nPencet apapun untuk kembali.")
		elif storemenu == "2":
			if myCoin > PriceData[2]:
				Upgrade(1, 2, PriceData[2])
			else:
				MenuExit = input("Uang anda tidak cukup!\nPencet apapun untuk kembali.")
		elif storemenu == "3":
			if myCoin > PriceData[1]:
				Upgrade(2, 1, PriceData[1])
			else:
				MenuExit = input("Uang anda tidak cukup!\nPencet apapun untuk kembali.")
		elif storemenu == "4":
			if myCoin > PriceData[2]:
				Upgrade(2, 2, PriceData[2])
			else:
				MenuExit = input("Uang anda tidak cukup!\nPencet apapun untuk kembali.")
		elif storemenu == "5":
			if myCoin > PriceData[1]:
				Upgrade(2, 1, PriceData[1])
			else:
				MenuExit = input("Uang anda tidak cukup!\nPencet apapun untuk kembali.")
		elif storemenu == "6":
			if myCoin > PriceData[2]:
				Upgrade(3, 2, PriceData[2])
			else:
				MenuExit = input("Uang anda tidak cukup!\nPencet apapun untuk kembali.")
		elif storemenu == "7":
			if myCoin > PriceData[1]:
				Upgrade(4, 1, PriceData[1])
			else:
				MenuExit = input("Uang anda tidak cukup!\nPencet apapun untuk kembali.")
		elif storemenu == "8":
			if myCoin > PriceData[2]:
				Upgrade(4, 2, PriceData[2])
			else:
				MenuExit = input("Uang anda tidak cukup!\nPencet apapun untuk kembali.")
	elif MainMenu == "2":
	
		confirm = input("Apakah kamu yakin? y/n\nketik exit untuk keluar\n")
		if confirm == 'y' or confirm == 'Y':
			myHP = myHealth[lvDarah]
			myAm = myArmor[lvDarah]
			mySt = myStrength[lvDarah]
			myCr = myCrit[lvCrit]
			ModeGame = input("Pilihlah mode yang anda inginkan:\n[1] EASY - [2] MEDIUM - [3] HARD\n")
			if ModeGame == '1':
				enemyHealth = int(random.randint(90, 110))
				enemyArmor = int(random.randint(40,55))
				enemyStrength = int(random.randint(10, 12))
				rangebp1 = int(random.randint(50,70))
				rangebp2 = int(random.randint(100,110))
				BattleMode = True
				abc = False
				for i in range(3):
					i = i + 1
					print("Battle will start in",i)
					time.sleep(1)
			elif ModeGame == '2':
				enemyHealth = int(random.randint(110, 150))
				enemyArmor = int(random.randint(55,65))
				enemyStrength = int(random.randint(20, 40))
				rangebp1 = int(random.randint(70,90))
				rangebp2 = int(random.randint(120,210))
				BattleMode = True
				abc = False
				for i in range(3):
					i = i + 1
					print("Battle will start in",i)
					time.sleep(1)
			elif ModeGame == '3':
				enemyHealth = int(random.randint(150, 250))
				enemyArmor = int(random.randint(65,75))
				enemyStrength = int(random.randint(40, 60))
				rangebp1 = int(random.randint(90,100))
				rangebp2 = int(random.randint(210,300))
				BattleMode = True
				abc = False
				for i in range(3):
					i = i + 1
					print("Battle will start in",i)
					time.sleep(1)
		elif confirm == 'exit' or confirm == 'EXIT':
			ccfirm = input("ketik apapun untuk keluar")
	elif MainMenu == "info" or MainMenu == "INFO":
		system("cls")
		print("Information about WaRPG.\nThis game made by hearth, and we/us learn to make a game by using python, this was easiest method ever to make a game, ganre of the game are rpg and fighting, but there's no effect or anything, all just a text, how to play the game is just read the intruction and upgrade you stats to make you more powerful.")
		exitmenu = input("\nPress anything to leave.")
	elif MainMenu == "3":
		confirm = int(input("How many second do you gonna afk farm?\nor, type exit to leave.\n"))
		if confirm > 600:
			print("You can't afk farm more than 10 minutes.!")
			time.sleep(2)
		elif confirm < 0:
			print("error")
			time.sleep(2)
		elif confirm < 600 and confirm > 0:
			for i in range(confirm):
				now = datetime.now()
				currenct_time = now.strftime("%H:%M:%S")
				MineCoin = int(random.randint(5,9))
				print("[",currenct_time,"] Coin mined: + ",MineCoin)
				myCoin = myCoin + MineCoin
		
while BattleMode == True:
	system("cls")
	print("Statsmu:")
	print("Darah:        ",myHP)
	print("Armod:        ",myAm)
	print("Kekuatan:     ",mySt)
	print("Critical:     ",myCr)
	print("---------------------------------------")
	print("Stats Musuh:")
	print("Darah:        ",enemyHealth)
	print("Armor:        ",enemyArmor)
	print("Kekuatan:     ",enemyStrength)
	print("Critical:     ",myCr)
	print("---------------------------------------")
	Pilihan = input("[1] Attack [2] Deffend\n::")
	if Pilihan == '1':
		enemyPilihan = int(random.randint(1,2))
		if enemyPilihan == 1:
			critchance = int(random.randint(1,myCr))
			enemyAttack = int(random.randint(1,enemyStrength))
			myAttack = int(random.randint(1,mySt))
			if critchance == 1:
				myAttack = myAttack * 3
				print("Critical Damage!")
			if enemyAttack == myAttack:
				print("No one got hurt!")
				time.sleep(2)
			else:
				print("You attacked",myAttack,"dmg")
				print("You got attacked",enemyAttack,"dmg")
				time.sleep(2)
				enemyHealth = enemyHealth - myAttack
				myHP = myHP - enemyAttack
		elif enemyPilihan == 2:
			critchance = int(random.randint(1,myCr))
			enemyDefend = int(random.randint(0,enemyArmor))
			myAttack = int(random.randint(1,mySt))
			if critchance == 1:
				myAttack = myAttack * 3
				print("Critical Damage!")
				time.sleep(2)
			if enemyDefend == myAttack:
				print("No one got hurt!")
				time.sleep(2)
			elif enemyDefend > myAttack:
				print("Enemy Success defend")
				time.sleep(2)
			elif enemyDefend < myAttack:
				enemyHealth = enemyHealth - myAttack
				print("You attacked",myAttack,"dmg")
				time.sleep(2)
	if Pilihan == '2':
		enemyPilihan = int(random.randint(1,2))
		if enemyPilihan == 1:
			enemyAttack = int(random.randint(1,enemyStrength))
			myDef = int(random.randint(1,myAm))
			if enemyAttack == myDef:
				print("No one got hurt!")
				time.sleep(2)
			elif enemyAttack > myDef:
				print("You got attacked",enemyAttack,"dmg")
				time.sleep(2)
				myHP = myHP - enemyAttack
			elif enemyAttack < myDef:
				print("You success defend the attack!")
				time.sleep(2)
		if enemyPilihan == 2:
			print("No one got hurt")
			time.sleep(2)
	if myHP < 1:
		print("[-] You lose!")
		BattleMode = False
		abc = True
		time.sleep(3)
	if enemyHealth < 1:
		coinbonus = int(random.randint(rangebp1, rangebp2))
		print("[+] You win! +",coinbonus)
		myCoin = myCoin + coinbonus
		BattleMode = False
		abc = True
		time.sleep(3)
		