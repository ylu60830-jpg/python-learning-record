#1. 读 scores.txt → 存成列表套列表（每个里层列表是 [姓名, 语文, 数学, 英语]）
#2. 遍历 → 算出每个人的总分
#3. 打印 姓名 总分
import os
import suanfa
dian_1 = {}
lujing = os.path.dirname(__file__)
file_path = os.path.join(lujing,"scores.txt")
if os.path.exists(file_path) :
    with open(file_path,encoding='utf-8')as f:
        for line in f:
            biao_1 = []
            names,*scores = line.strip().split(",")     #将lien切割后的第一项给names，其余字符串均交给scores
            for num in scores:      #这个循环的目的是为了将scores的字符串转换成数字
                score = int(num)
                biao_1.append(score)
            zongfen = suanfa.suanfa(biao_1)
            dian_1[names] = {"各分数":biao_1 , "总分":zongfen}    
    print(dian_1)

