#根据每个人的总分进行分组
def fenzu(zongfen):
    if zongfen>=270:
        return "A"
    elif zongfen >= 240:
        return "B"
    elif zongfen >= 200:
        return "C"
    else:
        return "D"