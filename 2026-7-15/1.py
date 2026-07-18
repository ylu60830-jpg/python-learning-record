#读取所给路径下的文件，对文件数据进行了切割等处理，统计category分类名的出现次数并打印
import os
if os.path.exists("D:/CLAUDE/python-tracker/learning-index.json") :
    with open("D:/CLAUDE/python-tracker/learning-index.json",encoding ='utf-8') as f:
        count = {}
        for i,line in enumerate(f) :
            if "category" in line:
                num = line.split(":")
                wenben = num[1].strip().strip('",')
                count[wenben] = count.get(wenben,0) +1
                #if wenben in count:
                #    count[wenben] += 1
                #else:
                #    count[wenben] = 1
        print(f"{count}")