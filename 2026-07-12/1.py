import os
students= []
name =[]
lujing = os.path.dirname(__file__)
file_path = os.path.join(lujing,"scores.txt")
if os.path.exists(file_path):
    with open(file_path,encoding = 'utf-8') as f:
        for line in f:
            student = {}
            num = line.split(  )
            name_num = num[0]
            score_num = num[1]
            student["姓名"] = name_num.split(":")[1]
            student["分数"] = score_num.split(":")[1]
            name.append(student["姓名"])        #
            students.append(student)
    for i in range(len(students)):
        print(f"第{i+1}行:{students[i]}")
    set(name)
    print(f"{len(set(name))}")
#主要学习了range(len(students)):
#set(name)
#    print(f"{len(set(name))}")
