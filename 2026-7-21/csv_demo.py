#1. 读 scores.csv
#2. 用 next(reader) 跳过表头
#3. 遍历剩下的行，用 f-string 打印成 张三: 85分, 等级B
import csv
import os
lujing = os.path.dirname(__file__)
file_path = os.path.join(lujing,"scores.csv")
if os.path.exists(file_path):
    with open(file_path,"r",encoding='utf-8') as f:
        reader = csv.reader(f)   #创建读取器
        header = next(reader)   #跳过表头（第一行）,将reader的指针移向第二行
        for row in reader:
            print(f"{row[0]}:{row[1]},{row[2]}")