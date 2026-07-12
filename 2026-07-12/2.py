import os
students = []
lujing = os.path.dirname(__file__)
file_path = os.path.join(lujing,"scores2.txt")
if os.path.exists(file_path):
    with open(file_path,encoding = 'utf-8') as f:
        for i,line in enumerate(f):
            has_error = False
            student = {}
            num = line.split(  )
            name_num = num[0]
            score_num = num[1]
            try:
                student["姓名"] = name_num.split(":")[1]
            except:
                has_error =True
                print(f"第{i+1}行，{name_num}存在问题，跳过")
            try:
                student["分数"] = score_num.split(":")[1]
            except:
                has_error = True
                print(f"第{i+1}行，{score_num}存在问题，跳过")
            if has_error == False:
                students.append(student)
    print(students)
