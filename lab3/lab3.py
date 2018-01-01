
import random as rnd
import process as pr

global MEMORY_SIZE
global QUEUE
global MEMORY
global PROCESS_NUM


def SetMemory():
	global MEMORY_SIZE
	global FREE_MEMORY_SIZE
	if MEMORY_SIZE != -1:
		print("Memory size already set")
	else:
		print("Enter memory size:")
		while MEMORY_SIZE < 0:
			MEMORY_SIZE = int(input())
			if MEMORY_SIZE > 0:
				break
			else:
				print("Enter right size")


def AddProcess():
	global PROCESS_NUM
	global MEMORY
	global QUEUE
	global MEMORY_SIZE

	if MEMORY_SIZE > 0:
		new_process = pr.Process(rnd.randint(1, 10)*10)
		PROCESS_NUM +=1
		new_process.num = PROCESS_NUM
		if MEMORY == []:
			new_process.addr = 0;
			MEMORY.append(new_process)
		else:
			QUEUE.append(new_process)
			buff = MEMORY[0]
			i = 0
			for element in MEMORY:
				if element != buff:
					if (element.addr - (buff.addr + buff.size)) >= new_process.size:
						new_process.addr = buff.addr + buff.size
						QUEUE.remove(new_process)
						MEMORY.insert(i, new_process)
						break
					else:
						buff = element
				i+=1
			if new_process in QUEUE:
				if (MEMORY_SIZE - (buff.addr + buff.size)) >= new_process.size:
					new_process.addr = buff.addr + buff.size 
					QUEUE.remove(new_process)
					MEMORY.append(new_process)


def FillMemory():
	global QUEUE
	global MEMORY

	buff_queue = QUEUE
	for process in QUEUE:
		buff = MEMORY[0]
		i=0
		for element in MEMORY:
			if element != buff:
				if (element.addr - (buff.addr + buff.size)) >= process.size:
					process.addr = buff.addr + buff.size
					buff_queue.remove(process)
					MEMORY.insert(i, process)
					break
				else:
					buff = element
			else:
				if buff.addr > 0 and buff.addr >= process.size:
					process.addr = 0
					buff_queue.remove(process)
					MEMORY.insert(i, process)
					break
			i+=1
		if process in buff_queue:
			if (MEMORY_SIZE - (buff.addr + buff.size)) >= process.size:
				process.addr = buff.addr + buff.size
				buff_queue.remove(process)
				MEMORY.append(process)
	QUEUE = buff_queue


def FinishProcess():
	global QUEUE
	global MEMORY

	print("Enter number of process: ")
	num = int(input())
	flag = 0
	for element in MEMORY:
		if element.num == num:
			flag = 1
			process = element
			break
	if flag == 0:
		print("No such process in memory! ")
	MEMORY.remove(process)
	FillMemory()


def SqueezeMemory():
	if MEMORY != []:
		i=0
		for element in MEMORY:
			if i>0:
				if element.addr > (MEMORY[i-1].addr + MEMORY[i-1].size):
					element.addr = MEMORY[i-1].addr + MEMORY[i-1].size
			i+=1
		FillMemory()

	else:
		print("Memory is empty")

def GetAddres():
	global QUEUE
	global MEMORY

	print("Enter number of process: ")
	num = int(input())
	flag = 0
	for element in MEMORY:
		if element.num == num:
			flag = 1
			process = element
			break
	if flag == 0:
		print("No such process in memory! ")
	else:
		print("Enter virtual address: ")
		virtual_address = int(input())
		if virtual_address > process.size:
			print("Wrong virtual addres!")
		else:
			print("Real addres: ", process.addr + virtual_address)

def PrintMemoryState():
	print()
	print("MEMORY: ", MEMORY_SIZE)
	print("----------------------------------------------------")
	print("|  number  |  start_addr  |  finish_addr  |  size  |")
	print("----------------------------------------------------")
	for element in MEMORY:
		print("|  %6d  |  %10d  |  %11d  |  %4d  |" %(element.num, element.addr, element.addr + element.size, element.size))
	print("____________________________________________________")
	print()
	print("QUEUE: ")	
	print("----------------------------------------------------")
	print("|  number  |  start_addr  |  finish_addr  |  size  |")
	print("----------------------------------------------------")
	for element in QUEUE:
		print("|  %6d  |  %10d  |  %11d  |  %4d  |" %(element.num, element.addr, element.addr + element.size, element.size))
	print("____________________________________________________")


def Menu():
	ch = 0
	while ch != '6':
		print()
		print("Print memory state: 0")
		print("Set memory: 1")
		print("Add process: 2")
		print("Finish process: 3")
		print("Squeeze memory: 4")
		print("Get real address: 5")
		print("Finish program: 6")
		print()

		ch = input()
		if ch == '0':
			PrintMemoryState()
		elif ch == '1':
			SetMemory()
		elif ch == '2':
			AddProcess()
		elif ch == '3':
			FinishProcess()
		elif ch == '4':
			SqueezeMemory()
		elif ch == '5':
			GetAddres()
		elif ch == '6':
			break
		else:
			continue


if __name__ == '__main__':
	MEMORY_SIZE = -1
	PROCESS_NUM = 0
	QUEUE = []
	MEMORY = []
	Menu()