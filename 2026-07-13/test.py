import tools
num = tools.grade(85)
print(num)
from tools import grade     #从tools模块引入grade函数
print(grade(65))
#from tools import grade, some_other_func
#grade(55)