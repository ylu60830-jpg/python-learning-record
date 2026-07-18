#重新学习json的语法
import json
import os
lujing = "C:/Users/ASUS/Desktop/code/2026/7/2026-7-18"
student = {
    "姓名":"",
    "年龄": 20,
    "及格": True,
    "科目": ["语文","数学","英语"]
}
json_path = os.path.join(lujing,"text.json")
os.makedirs(lujing,exist_ok = True)
with open(json_path,"w",encoding = 'utf-8') as f:
    json.dump(student,f,ensure_ascii=False)
    print("存储完成")
#json.dump(student, f, ensure_ascii=False) 拆解
#     json.dump(
#      student,              # ① 要存的东西：你的字典
#      f,                    # ② 写到哪：文件对象（那扇"打开的门"），不是路径！
#      ensure_ascii=False    # ③ 中文开关：False = 正常显示中文，True = 转成 \uXXXX
#  )
with open(json_path,"r",encoding='utf-8') as f:
    data = json.load(f)
    print(f"读回:{data}")