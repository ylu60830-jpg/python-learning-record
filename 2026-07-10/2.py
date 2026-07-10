def grade(score):       #定义grade函数，参数为score,设置了四种情况
    if score >= 90:
        print("优秀") 
    elif score >= 80:
        print("良好")
    elif score >= 60:
        print("及格")
    else:
        print("不及格")


def grade2(score):       #定义grade函数，参数为score,设置了四种情况
    if score >= 90:
        return("优秀") 
    elif score >= 80:
        return("良好")
    elif score >= 60:
        return("及格")
    else:
        return("不及格")
grade(85)   #调用函数，将参数85放入函数中运行
a = grade(85)   #调用grade函数时触发print导致再一次输出函数运行结果
print("a=",a)
grade2(85)   #调用函数，将参数85放入函数中运行,将函数运行结果返回存储，不输出
b = grade2(85)
print("b=",b)