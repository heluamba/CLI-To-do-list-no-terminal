import json

def	is_number(val):
	try:
		int(val)
		return (True)
	except ValueError:
		return (False)

def	valid_input(prompt):
	flag = True
	data = ''

	while True:
		if flag:
			flag = False
			data = input(prompt + "\n")
		if is_number(data):
			data = input("Invalid input, try again:\n")
		else:
			return (data)

def	set_status():
	status = ['PENDING', 'DOING', 'COMPLETED']
	nu = 0;
	
	print("Select task status")
	print("1-PENDING | 2-DOING | 3-COMPLETED: ")
	while True:
		nu = input()
		if not is_number(nu) or (int(nu) < 1 or int(nu) > 3):
			print("Invalid number[0-3], try agin: ")
		else:
			return(status[int(nu) - 1])

def	show_fild(fild):
	print("--------------------------------------")
	print("STASK: " + fild['taskName'])
	print("STATUS: " + fild['status'])
	print("STACK ID: " + str(fild['id']))
	print("--------------------------------------")


def	get_task_id(size):
	id = input("Put the id task: ")
	if not is_number(id) or (int(id) < 0 or int(id) > size):
		return (False)
	return (int(id))


#Read json

def	read_fild(file):
	fild = ''

	for line in file:
		if '}' in line:
			fild += line
			break
		else:
			fild += line
	return (fild)

def	read_tasks(fileName):
	list_task = []
	task = {}
	content = ''

	f = open(fileName, 'r')
	while True:
		content = read_fild(f)
		if not content :
			break
		else:
			task = json.loads(content);
			list_task.append(task)
	f.close();
	return (list_task)
