#学习.read和.count的用法
import os
lujing = "D:/CLAUDE/python-tracker/learning-index.json"
if os.path.exists(lujing):
    with open(lujing,encoding ="utf-8") as f:
        neirong = f.read()
        cishu_1 = neirong.count("status")
        cishu_2 = neirong.count("learned")
        print(f"status:{cishu_1}次,learned:{cishu_2}次")