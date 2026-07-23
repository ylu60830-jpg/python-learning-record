#1. 读昨天的 scores.csv
#2. 把每行数据收集到 rows = [] 列表里
#3. 用 csv.writer 写到 scores_out.csv
#4. 打印「写入完成，共 X 条记录」

import csv
import os
rows =[]
lujing = os.path.dirname(__file__)
file_path = os.path.join(lujing,"scores.csv")
try:
    with open(file_path,"r",encoding='utf-8') as f:  
        reader = csv.reader(f)  #建读取器
        for row in reader:
            rows.append(row)
    new_path = os.path.join(lujing,"scores_out.csv")
    with open(new_path,"w",newline="",encoding='utf-8') as f2:    #写csv时加入newline=""可以防多空行
        writer = csv.writer(f2)     #建修改器
        writer.writerows(rows)      #用writerows吧rows写进去
        print(f"写入完成，共 {len(rows)} 条记录")
except FileNotFoundError:
    print("该文件不存在")

        
