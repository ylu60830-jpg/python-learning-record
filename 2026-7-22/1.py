#1. csv 某行列数不够 → 跳过，打印"第X行数据不完整，跳过"
#2. 分数列不是数字 → 跳过，打印"第X行分数格式错误，跳过"
#3. 正常行 → 照常打印 姓名:分数分,等级

import  csv
import os
lujing = os.path.dirname(__file__)
file_path = os.path.join(lujing,"scores.csv")
try:
    with open(file_path,"r",encoding ='utf-8') as f:
        reader = csv.reader(f)  #创建读取器
        header = next(reader)
        for i,row in enumerate(reader,start=1):
            try:
                name = row[0]
                score = int(row[1])     #如果此处出现问题，使用ValueError
                grade = row[2]  #如果此处出现问题，使用IndexError
                print(f"{name}:{score}分,{grade}")
            except IndexError:      #行太短
                print(f"第{i}行数据不完整，跳过")
            except ValueError:      #分数不是数字
                print(f"第{i}行分数格式错误:{row[1]}，跳过")
except FileNotFoundError:
    print("该文件不存在")