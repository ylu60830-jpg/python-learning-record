import os    #导入操作系统模块
script_dir = os.path.dirname(__file__)   #查询本文件所在文件夹路径语法
file_path = os.path.join(script_dir,"hosts.txt")  #在路径后拼接文件名，形成完整路径语法
if os.path.exists(file_path):    #对上步语法进行判断，若存在则执行下一步
    with open(file_path,'r') as f:  #with代码运行结束后自动关闭文件，open打开文件，as f将路径文件装入变量f，r只读取
        for line in f:    #逐行读取文件内容
            print("读到一行：",line.strip())  #输出每一行内容,strip()去掉每行内容的换行符
else: #若不存在则执行下一步
    print("未找到hosts.txt")