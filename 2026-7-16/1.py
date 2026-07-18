#打开并查找2026-7-15文件夹内文件的行数以及文件中是否应用了外部模块
import os
import num
count = {}
jieguo = []
lujing = "C:/Users/ASUS/Desktop/code/2026/7/2026-7-15"
if os.path.exists(lujing):
    names = os.listdir(lujing)      #查询lujing下的文件名组成列表
    for name in names:
        wenjianlj = os.path.join(lujing,name)
        with open(wenjianlj,encoding ='utf-8') as f:
            hangshu = 0
            neirong = f.read() #读取文件内的全部内容
            hangshu =neirong.count('\n') +1     #.count()数字符串里某个东西出现了几次
            jieguo=num.hanshu(neirong)
            print(f"{name}:{hangshu}行:{jieguo}")