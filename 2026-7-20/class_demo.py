#class 语法的学习
#class 关键字：告诉python 定义一个类型
# Student 是类名，习惯首字母大写
class Student:
    #pass  pass 是占位符
    def __init__(self,name,score):  #self自己,name参数1,score参数2
        self.name = name  #将接收进来的name值给这个学生的name属性
        self.score = score  #将接收进来的score值赋给这个学生的score属性

    def check_pass(self):
        return self.score >= 60
s1 = Student("张三",85)     #此时self为s1
s2 = Student("李四",55)

print(s1.name,s1.check_pass())
print(s2.name,s2.check_pass())