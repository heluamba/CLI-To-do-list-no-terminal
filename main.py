import json
import	sys
from utils import * 

fileName = 'tasks.json'

def	show_menu(list_task=[]):
	print("========================================")
	print("           TASK MANAGER                 ")
	print("========================================")
	print("1. list")
	print("2. add")
	print("3. complete")
	print("4. delete")
	print("5. exit\n")
	print("========================================")

def	add_task(list_task, id=0):
	task = {}
	js = ''
	add_task.id = getattr(add_task, "id", 0) + 1

	task['id'] = add_task.id
	task['taskName'] = valid_input("Put the task Name")
	task['status'] = set_status()
	list_task.append(task)
	js = json.dumps(task)
	with open(fileName, 'a') as f:
		f.write(js + '\n')
		
def show_tasks(list_task):
	list_task = read_tasks(fileName)
	if list_task is None:
		return
	if not list_task:
		print("List is empty")
		return
	for task in list_task:
		show_fild(task)
		
def	markCompleted(list_task):
	js = ''
	id = get_task_id(len(list_task))
	if id == False:
		print("Inavalid id❌")
		return 
	list_task = read_tasks()
	list_task[id - 1]['status'] = "COMPLETAED"
	for task in list_task:
		js += json.dumps(task)
	with open(fileName, 'w') as f:
		f.write(js + '\n')



def	delete_task(list_task):
	js = '' 
	id = get_task_id(len(list_task))
	if id == False:
		print("Inavalid id❌")
		return 
	list_task = read_tasks(fileName)
	for task in list_task:
		js += json.dumps(task)
	with open(fileName, 'w') as f:
		f.write(js)

def	exit(list_task):
	del list_task
	sys.exit(0)

def	main():
	cmd = ""
	list_task = []
	commands = {
		'list'     : show_tasks,
		'menu'	   : show_menu,
		'add'      : add_task,
		'complete' : markCompleted,
		'delete'   : delete_task,
		'exit'     : exit
		}

	show_menu()
	while True:
		cmd = input("> ")
		cmd = commands.get(cmd)
		if  callable(cmd):
			cmd(list_task)
		else:
			print("Inavlid commnad⁉❌")
main()

#read_tasks(fileName)
