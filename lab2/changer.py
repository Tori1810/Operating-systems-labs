
import threading
import random as rnd
import time
import coin as c

global NOMINALS
global BANK
global COIN
global FLAG_1
global FLAG_2
global TURN

def process_1():
	global FLAG_1
	global FLAG_2
	global TURN
	global COIN

	FLAG_1 = True
	while FLAG_2 == True:
		if TURN == 1 :
			FLAG_1 = False
			while TURN == 1:
				pass
			FLAG_1 = True


	COIN = c.Coin(rnd.choice(NOMINALS_FULL))
	print("Coin nominal: ", COIN.nominal)
	TURN = 1
	FLAG_1 = False

	
		
def process_2():
	global COIN
	global FLAG_2
	global FLAG_1
	global TURN
	global BANK


	FLAG_2 = True
	while FLAG_1 == True:
		if TURN == 0:
			FLAG_2 = False
			while TURN == 0:
				pass
			FLAG_2 = True

	print("Please, enter nominal for coin exchange: ")
	
	while True:
		entered_nominal = int(input())
		if (not entered_nominal in BANK):
			print("No such nominal in BANK")
		elif (entered_nominal in NOMINALS and entered_nominal <= COIN.nominal and entered_nominal in BANK):
			break
		else:
			print("Wrong nominal!!! Enter another: ")
                        
	
	summa = 0
	bank_copy = BANK
	exchange_list = []
	exchange = True
	main_coin = entered_nominal
	exchange_list.append(main_coin)
	bank_copy.remove(main_coin)
	summa += main_coin
	while True:
		if (summa < COIN.nominal):
			if (entered_nominal in bank_copy and summa+entered_nominal<=COIN.nominal):
				exchange_list.append(entered_nominal)
				bank_copy.remove(entered_nominal)
				summa += entered_nominal
			else:
				bank_copy.reverse()
				for element in bank_copy:
					if (summa+element<=COIN.nominal):
						bank_copy.remove(element)
						summa += element
						exchange_list.append(element)
				if (summa < COIN.nominal):
					for element in bank_copy:
						if (element < COIN.nominal and element > main_coin):
							break
					if (element > main_coin):
						main_coin = element
						for element in exchange_list:
							bank_copy.append(element)
						bank_copy.sort()
						bank_copy.reverse()
						exchange_list = []
						exchange_list.append(main_coin)
						bank_copy.remove(main_coin)
						summa = main_coin
					else:	
						for element in exchange_list:
							bank_copy.append(element)
						bank_copy.sort()
						bank_copy.reverse()
						exchange_list = []
						summa = 0
						for element in bank_copy:
							if (summa + element <= COIN.nominal):
								summa += element
								exchange_list.append(element)
						for element in exchange_list:
							bank_copy.remove(element)
						if (summa < COIN.nominal):
							exchange = False
							break

		else:
			break

	if (exchange == True):
		COIN.exchange = exchange_list
		BANK = bank_copy
		print("Exchanged list: ")
		print(exchange_list)
		BANK.append(COIN.nominal)
	else:
		print("Cant exchange this coin!")
	
	TURN = 0;
	FLAG_2 = False
	


if __name__ == '__main__':
        NOMINALS_FULL = [2, 5, 10, 25, 50, 100]
        NOMINALS = [1, 2, 5, 10, 25, 50]
        BANK = [1,1,1,2,2,2,2,2,5,5,5,10,10,10,25]
        FLAG_1 = False
        FLAG_2 = False
        TURN = 0
        COIN = 0
        A = threading.Thread(target=process_1)
        B = threading.Thread(target=process_2)
        A.start()
        B.start()
        A.join()
        B.join()

	
