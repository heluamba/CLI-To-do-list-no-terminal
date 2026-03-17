import json


def	is_number(val):
	try:
		int(val)
		return (True)
	except ValueError:
		return (False)


def valid_input(prompt):
    while True:
        data = input(prompt + "\n").strip()
        if data:
            return data
        print("Campo não pode estar vazio.")


def	set_status():
	status = ['PENDING', 'DOING', 'COMPLETED']
	nu = 0
	
	print("Select task status")
	print("1-PENDING | 2-DOING | 3-COMPLETED: ")
	while True:
		nu = input()
		if not is_number(nu) or (int(nu) < 1 or int(nu) > 3):
			print("Invalid number[0-3], try agin: ")
		else:
			return(status[int(nu) - 1])


def	show_field(fild):
	print("--------------------------------------")
	print("STASK: " + fild['taskName'])
	print("STATUS: " + fild['status'])
	print("STACK ID: " + str(fild['id']))
	print("--------------------------------------")


def generate_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def	get_task_id():
	id = input("Put the id task: ")
	if not is_number(id) or (int(id) <= 0):
		return (False)
	return (int(id))


def read_tasks(fileName):
    try:
        with open(fileName, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []