import os   
student_list = []
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir,"scores.txt")
if os.path.exists(file_path):
    with open(file_path,encoding='utf-8') as f:
        for line in f:
            students ={}    #在循环里建立字典students
            parts = line.split(  )      #在line中按任意空白字符切割完后赋值给parts
            name_part = parts[0]
            score_part = parts[1]
            students["姓名"] = name_part.split(":")[1]      #将name_part字符串用":"分割后下标[1]的内容写入字典"姓名"后
            students["分数"] = score_part.split(":")[1]     #将score_part字符串用":"分割后下标[1]的内容写入字典"分数"后
            student_list.append(students)       #将字典students追加到列表student_list的末尾
        print(student_list)
def grade(score):       #定义函数grade
    if score >= 100:
        return("SSS")
    elif score >= 90:
        return("S")
    elif score >= 80:
        return("A")
    elif score >= 70:
        return("B")
    else:
        return("C")
for student in student_list:    #遍历student_list，逐个元素赋值给student
    名字 = student["姓名"]
    分数 = student["分数"]
    print(f"{名字} :{grade(int(分数))}")    #f-string格式化：int()转数字→grade()评级→输出"唐三:S"

