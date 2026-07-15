import os

# 最终收集所有书的大列表，每个元素是一个小列表 ["类型", "书名"]
book = []

# 拼出 books.txt 的完整路径
lujing = os.path.dirname(__file__)
file_path = os.path.join(lujing, "books.txt")

if os.path.exists(file_path):
    with open(file_path, encoding='utf-8') as f:
        for i, line in enumerate(f):
            try:
                # strip()去换行 → split(":")按冒号切 → 得到 ["科幻","三体"] 这样的小列表
                num = line.strip().split(":")
            except:
                print(f"第{i}行报错,在{line}")
            book.append(num)


        # 字典统计：类型 → 本数
        count = {}
        for item in book:
            leixing = item[0]          # 取小列表第一个元素 = 类型
            if leixing in count:       # 字典里已经有这个类型？
                count[leixing] += 1    # 有 → 本数加1
            else:
                count[leixing] = 1     # 没有 → 第一次见，初始记1
        print(count)

        count2 = {}
        for leixing,shuming in book:
            #leixing = qaq[0]
            #shuming = qaq[1]
            if leixing not in count2:
                count2[leixing] = set()
            count2[leixing].add(shuming)
        for leixing,shuji in count2.items():
            print(f"{leixing}:{len(shuji)}")

else:
    print(f"未寻找到指引路径下文件")
