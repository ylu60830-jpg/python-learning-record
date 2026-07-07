import os   #导入操作系统模块
mylist =[]  #创建空列表
script_dir = os.path.dirname(__file__)  #查询本文件所在文件夹路径
file_path = os.path.join(script_dir,"config.txt")   #将路径拼接齐全
if os.path.exists(file_path):   #对上步语法进行判断，若存在则执行下一步
    with open(file_path,'r') as f:  #打开并只读取file_path完备路径下的文件，并放入函数f中，代码运行结束后关闭文件
        for line in f:  #逐行读取文件内容，并将读取到的内容储存进line中
            mylist.append(line.strip())  #将line中的内容去掉换行符后添加进mylist列表中
        print("共",len(mylist),"行")  #输出mylist列表中有多少行
        print(mylist)   #输出mylist列表中的内容
else:   #若不存在则执行下一步
    print("缺少 config.txt")