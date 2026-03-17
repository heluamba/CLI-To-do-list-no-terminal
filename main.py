import json
import	sys
import pdb
from utils import * 

fileName = 'tasks.json'


def	show_menu(list_task=[]):
	print("========================================")
	print("           TASK MANAGER                 ")
	print("========================================")
	print(". list")
	print(". add")
	print(". complete")
	print(". delete")
	print(". exit\n")
	print("========================================")

def save_tasks(tasks):
    with open(fileName, "w") as f:
        json.dump(tasks, f, indent=2)


def	add_task(list_task): 
	task = {}
	if list_task:
		list_task.sort(key=lambda x: x["id"])
	if not list_task:
		task['id'] = 1
	else:
		task['id'] = generate_id(list_task)
	task['taskName'] = valid_input("Put the task Name")
	task['status'] = set_status()
	list_task.append(task)
	save_tasks(list_task)


def show_tasks(list_task):
	if not list_task:
		print("List is empty")
		return
	list_task.sort(key=lambda x: x["id"])
	for task in list_task:
		show_field(task)


def	markCompleted(list_task):
	if not list_task:
		return 
	found = False
	id = get_task_id()
	if id == False:
		print("Inavalid id❌")
		return 
	for i, task in enumerate(list_task):
		if id == task['id']:
			list_task[i]['status'] = "COMPLETED"
			found = True
			break
	if not found:
		print("Task not found ❌")
		return
	save_tasks(list_task)


def	delete_task(list_task):
	if list_task == None:
		return 
	id = get_task_id()
	if id == False:
		print("Inavalid id❌")
		return
	for i, task in enumerate(list_task):
		if id == task['id']:
			del list_task[i]
			break
	save_tasks(list_task)

def	exit_program(_):
	sys.exit(0)

def	main():
	cmd = ""
	list_task = read_tasks(fileName)
	commands = {
		'list'     : show_tasks,
		'menu'	   : show_menu,
		'add'      : add_task,
		'complete' : markCompleted,
		'delete'   : delete_task,
		'exit'     : exit_program
		}

	show_menu()
	while True:
		cmd = input("> ")
		action = commands.get(cmd)
		if  callable(action):
			action(list_task)
		else:
			print("Inavlid commnad⁉❌")
main()
