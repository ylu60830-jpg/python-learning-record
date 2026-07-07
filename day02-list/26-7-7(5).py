import os   #导入操作系统模块
lyrics_dict = {}    #创建字典lyrics_dict
script_dir = os.path.dirname(__file__)   #查询本文件所在文件夹路径
file_path = os.path.join(script_dir,"config.txt")   #将文件夹路径后拼接上文件名，形成完整路径
if os.path.exists(file_path) :  #查询和判断ile_path中是否存在路径文件，如果存在则进行下一步
    with open(file_path,encoding = 'utf-8') as f:   #打开file_path路径下的文件，用 UTF-8 这套编码规则来解读这个文件，並將读取到的内容放入文件对象f中，代码运行结束后关闭文件
        mylist = f.readlines()  #将文件对象f中的全部内容读取后存储在mylist列表中
        for i, line in enumerate(mylist):   #使用for循环，enumerate()函数将mylist列表中每行的内容前加入索引值 i，并将每行的内容存储在line中
            lyrics_dict[i] = line.strip()   #将line中的内容去掉换行符后添加进lyrics_dict字典中，索引值 i 为键，line.strip()为值
    print(lyrics_dict[3])   #输出lyrics_dict字典中键为3的值
else:   #若不存在则执行下一步
    print("缺少 config.txt")