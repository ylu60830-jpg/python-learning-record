import os
todo_list =[]
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'todo.txt')
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            todo_list.append(line.strip())
    print("共", len(todo_list), "行")
    print(todo_list)
else:
    print("缺少 todo.txt")