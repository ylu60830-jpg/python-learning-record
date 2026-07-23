#每行 设备名,状态码。状态码 0 = 正常，非 0 = 异常。
#任务：写 warmup.py，读完所有行，用 has_error 标志变量记录有没有异常设备。最后：
#- 有异常 → 打印 发现异常设备
#- 全正常 → 打印 全部正常
import os
lujing = os.path.dirname(__file__)
file_path = os.path.join(lujing,"check_log.txt")
try:
    with open(file_path,"r",encoding='utf-8') as f:
        has_error = False
        for i, line in enumerate(f):
            num =  line.strip().split(",")
            if int(num[1]) != 0:
                has_error = True
                print(f"第{i+1}行发现异常设备")
        if has_error == False:
            print("全部正常")
except FileNotFoundError:
    print("该文件不存在")