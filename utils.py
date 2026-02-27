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
			data = input("stask catn't be number, try again:\n")
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