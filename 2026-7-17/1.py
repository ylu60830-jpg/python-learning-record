#复习从文件获取内容并将内容使用列表套字典的方式输出
import os
import chaxun 
import fenzu
import json
count2 = []
lujing = os.path.dirname(__file__)
file_path = os.path.join(lujing,"scores.txt")
if os.path.exists(file_path) :
    with open(file_path, encoding = 'utf-8') as f:
        for line in f :
            count = {}
            num = line.strip()
            name = num.split(",")[0]
            score = int(num.split(",")[1])
            count["name"] = name
            count["score"] = score
            count2.append(count)
        
        for item in count2:
            print(item)
            print(chaxun.chaxun(item["name"],count2))
        print(fenzu.fenzu(count2))
        #循环变量在循环结束后会固定为最后一次循环的值


    json_path = os.path.join(lujing,"data.json")
    with open(json_path,"w",encoding = 'utf-8') as f:
        json.dump(count2,f,ensure_ascii = False)
        print("存储完成")

    with open(json_path,"r",encoding = "utf-8") as f :
        data = json.load(f)
        print("读回来了：", data)
        print("类型是：", type(data))
        print("第一条：", data[0])
            