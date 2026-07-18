#实验：from os import * 会引入 os 模块的全部内容，覆盖内置 open 函数导致后续 open()报错
from os import *
print(dir())