import os
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir,"config.txt")
if os.path.exists(file_path):
    with open(file_path,'r') as f:
         for line in f:
            print(line.strip())
else:
    print("缺少 config.txt")