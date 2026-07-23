#1. 逐行 csv.reader 读
#2. 跳过空白行
#3. 用 try/except 抓三种错误：姓名空、分数非数字、等级缺失
#4. 有问题的行 → enumerate 记行号 → 写入 error_log.txt
#5. 干净行 → 收进列表 → 最后用 csv.writer 写出 scores_clean.csv
import csv
import os
biao = []
biao_1 = []
lujing = os.path.dirname(__file__)
file_path = os.path.join(lujing,"scores_raw.csv")
try:
    with open(file_path,"r",encoding='utf-8') as f1:
        reader = csv.reader(f1)     #建读取器
        biaotou = next(reader)      #跳过表头
        for i,line in enumerate(reader,start=2):
            try:
                name = line[0]
                score = line[1]
                grade = line[2]
                if name == "":
                    biao_1.append((i,"姓名空",line))       #元组打包
                    print(f"第{i}行姓名内容为空，跳过")
                elif score == "":
                    biao_1.append((i,"成绩空",line))
                    print(f"第{i}行分数内容为空，跳过")
                elif grade == "":
                    biao_1.append((i,"等级空",line))
                    print(f"第{i}行等级内容为空，跳过")
                else:                   
                    int(score)
                    biao.append(line)
            except IndexError:
                biao_1.append((i,"数据缺失",line))
                print(f"第{i}行数据不完整,跳过")
            except ValueError:
                biao_1.append((i,"内容出错",line))
                print(f"第{i}行内容出错,跳过")
        new_error = os.path.join(lujing,"error_log.txt")
        new_path = os.path.join(lujing,"scores_clean.csv")
        with open(new_error,"w",encoding='utf-8') as f2:
            for i,err_type,row in biao_1:
                f2.write(f"第{i}行 [{err_type}] {row}\n")
        with open(new_path,"w",newline="",encoding='utf-8') as f3:
            writer = csv.writer(f3)     #建写入器
            writer.writerow(biaotou)    #写入表头
            writer.writerows(biao)      #写正式内容文件
except FileNotFoundError:
    print("该文件不存在")