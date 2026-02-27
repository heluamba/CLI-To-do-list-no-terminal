import json
from utils import * 

def	show_menu():
	print("========================================")
	print("           TASK MANAGER                 ")
	print("========================================")
	print("1. Listar tarefas")
	print("2. Adicionar tarefa")
	print("3. Concluir tarefa")
	print("4. Deletar tarefa")
	print("5. Sair")

def	add_task(list_task, id):
	task = {}
	task['id'] = id
	task['taskName'] = valid_input("Put the task Name")
	task['status'] = set_status()
	list_task.append(task)


def	main():
	file = 'tasks.json'

list_task = []
add_task(list_task, 0)

print(list_task)

