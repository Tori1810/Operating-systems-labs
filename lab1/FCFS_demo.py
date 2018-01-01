import process as pr
import random as rnd


global PROCESS_APPEAR_PROBABILITY
global PROCESS_LIST
global FINISHED_PROCESS_LIST
global CURRENT_ITERATION
global CURRENT_PROCESS
global FREE_PROCESSOR
global TASK_NUMBER
global FINISHED_TASK_NUMBER
global CURRENT_TASK_NUMBER




def planning():
	global CURRENT_ITERATION
	global TASK_NUMBER
	global FINISHED_TASK_NUMBER
	global FREE_PROCESSOR
	global CURRENT_PROCESS
	global CURRENT_TASK_NUMBER
	global FINISHED_PROCESS_LIST


	PROCESS_LIST.append(pr.Process(4, 0, 1))
	PROCESS_LIST.append(pr.Process(7, 0, 2))
	PROCESS_LIST.append(pr.Process(1, 0, 3))
	PROCESS_LIST.append(pr.Process(6, 0, 4))
	PROCESS_LIST.append(pr.Process(3, 0, 5))
	while True:
		
		if TASK_NUMBER == FINISHED_TASK_NUMBER:
			break 

		print("-------------------------------------------------------------------------------")
		print("Iteration ", CURRENT_ITERATION)
		print()

		# if CURRENT_TASK_NUMBER < TASK_NUMBER:
		# 	if rnd.random() < PROCESS_APPEAR_PROBABILITY:
		# 		CURRENT_TASK_NUMBER += 1
		# 		PROCESS_LIST.append(pr.Process(rnd.randint(3, 10), CURRENT_ITERATION, CURRENT_TASK_NUMBER))
		# 		print("Task ", CURRENT_TASK_NUMBER, " appeared")
		# 	else:
		# 		print("Task didn't appear")
		# else:
		# 	print("All tasks have already appeared. There will not be other tasks")
				
		if FREE_PROCESSOR and PROCESS_LIST == []:
			print ("Processor is free. There are no task to compute")

		if (FREE_PROCESSOR and PROCESS_LIST):
			FREE_PROCESSOR = False
			CURRENT_PROCESS = PROCESS_LIST.pop(0)
			CURRENT_PROCESS.start_time = CURRENT_ITERATION


			
		if CURRENT_PROCESS != []:
			CURRENT_PROCESS.execute();
			print("Task ", CURRENT_PROCESS.name, " is computing. Time to finish ", CURRENT_PROCESS.time_to_finish)
			for element in PROCESS_LIST:
				element.wait();

			if CURRENT_PROCESS.time_to_finish == 0:
				FREE_PROCESSOR = True
				FINISHED_TASK_NUMBER +=1
				CURRENT_PROCESS.finish_time = CURRENT_ITERATION
				FINISHED_PROCESS_LIST.append(CURRENT_PROCESS)
				CURRENT_PROCESS = []

			

		CURRENT_ITERATION += 1

		print("-------------------------------------------------------------------------------")


def print_table():
	print("Number   | appear time | execute time | start time | finish time | wait time | full time |")
	middle_wait_time = 0
	middle_executive_time = 0
	for element in FINISHED_PROCESS_LIST:
		middle_wait_time += element.wait_time
		middle_executive_time += element.wait_time + element.executive_time
		print("  %5d  |    %5d    |     %5d    |    %5d   |    %5d    |   %5d   |   %5d   |" % (element.name, element.appear_time, element.executive_time, element.start_time, element.finish_time, element.wait_time, element.wait_time+element.executive_time))
	middle_wait_time = middle_wait_time/len(FINISHED_PROCESS_LIST)
	middle_executive_time = middle_executive_time/len(FINISHED_PROCESS_LIST)
	print("Middle wait time for processes = ", middle_wait_time)
	print("Middle executive time with waiting for processes = ", middle_executive_time)		

		
		


if __name__ == '__main__':
	PROCESS_APPEAR_PROBABILITY = 0.3
	PROCESS_LIST = []
	CURRENT_ITERATION = 0
	FREE_PROCESSOR = True
	TASK_NUMBER = 5
	FINISHED_TASK_NUMBER = 0
	CURRENT_PROCESS = []
	CURRENT_TASK_NUMBER = 0
	FINISHED_PROCESS_LIST = []
	planning();
	print_table()
