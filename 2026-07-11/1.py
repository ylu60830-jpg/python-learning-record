import os   #导入操作系统模块
students = []   #创建空列表students
script_dir = os.path.dirname(__file__)  #查找当前文件所在文件夹路径
file_path = os.path.join(script_dir,"scores.txt")   #在文件夹路径后补齐文件
if os.path.exists(file_path):   #判断该文件路径下文件是否存在
    with open(file_path,encoding ='utf-8') as f:    #打开文件显式指定编码并将文件赋值给f，程序运行结束后关闭文件
        for line in f:  #逐行读取f，每轮把一行赋值给line
            students.append(line.strip())   #将line的内容去掉末尾换行符后追加到students列表末尾
        for number in students:       #遍历students，逐个元素赋值给number        
            prats = number.split(  )    #在number中按任意空白字符切割完后赋值给prats
            name_part = prats[0]    #将parts的零号字符赋值给name_prat
            score_part = prats[1]   #将parts的一号字符赋值给score_prat

            print(name_part.split(":")[1])  #输出name_part字符串切割“:”后的一号字符
            print(score_part.split(":")[1])     #输出score_part字符串切割“:”后的一号字符
