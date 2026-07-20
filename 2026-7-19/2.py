#把学生按等级分组——A 等（总分 ≥ 270）、B 等（240~269）、C 等（200~239）、D 等（<
#200）。输出 {等级: [名字列表]}，比如 {"A": ["孙九", "王五"], ...}。
import os
import suanfa
import fenzu
dian= {}
lujing = os.path.dirname(__file__)
file_path = os.path.join(lujing,"scores.txt")
if os.path.exists(file_path):
    with open(file_path,encoding='utf-8') as f:
        for line in f :
            biao = []
            names,*scores = line.strip().split(",")
            for num in scores:
                score =int(num) 
                biao.append(score)
            zongfen = suanfa.suanfa(biao)
            zubie =fenzu.fenzu(zongfen)
            if zubie not in dian:
                dian[zubie] = []    #在字典组别的后面创建空列表
            dian[zubie].append(names)
        print(dian)