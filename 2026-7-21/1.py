#1. 读 scores.txt，每行拆出姓名和分数
#2. 写一个 grade(score) 函数：90+ → A，80+ → B，70+ → C，60+ → D，其他 → F
#3. 存成列表套字典：[{"姓名": "张三", "分数": 85, "等级": "B"}, ...]
#4. 用 f-string 逐行打印：张三: 85 → B

import os
import fenzu
biao = []
lujing = os.path.dirname(__file__)
file_path = os.path.join(lujing,"scores.txt")
if os.path.exists(file_path):
    with open(file_path,"r",encoding='utf-8') as f:
        for line in f:
            dian = {}
            name,score = line.strip().split( )
            fenshu = int(score)
            zu = fenzu.grade(fenshu)
            dian
            dian = {"姓名":name,"分数":fenshu,"等级":zu}
            biao.append(dian)
            print(f"{name}:{fenshu}->{zu}")
