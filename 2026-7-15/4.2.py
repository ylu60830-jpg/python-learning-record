#取所给文件夹路径下以".py"结尾的文件行数并输出对应文件行数结果
import os
count = {}
lujing = "C:/Users/ASUS/Desktop/code/2026/7/2026-7-15"
if os.path.exists(lujing):
    names = os.listdir(lujing)      #取lujing下的文件名组成列表
    for name in names:
        if name.endswith(".py"):    #使用.endswith()判断文件名name是否以.py结尾
            wenjianlj = os.path.join(lujing,name)   #使用os.path.join()将lujing与name(具体文件名称)拼接成完整路径     
            with open(wenjianlj,encoding = 'utf-8') as f:
#                for i,wenjian in enumerate(f):
#                    pass                    
#                count[name] = i+1
#    print(f"{count}")
                hangshu = 0
                for wenjian in f:
                    hangshu += 1
                count[name] = hangshu
    print(count)