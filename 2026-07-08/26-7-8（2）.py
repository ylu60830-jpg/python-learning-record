my_github = {"库1": "python-learning-record", "库2": "skill-DB", "库3": "ai-painter"}  #创建字典my_github，并添加键值对
print(my_github)    #输出字典my_github的全部内容
print(my_github["库1"])     #输出字典my_github中键为"库1"的值
my_github["库4"] = "python-26-7-8(2)"     #添加键值对"库4":"python-26-7-8(2)"到字典my_github中，若已存在则修改
for key, value in my_github.items():    #使用for循环，items()函数将字典my_github中的每个键值对拆分为key和value，并将其输出
    print(key,":",value)