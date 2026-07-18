import chaxun
import grade
def fenzu(data):
    result = {}
    for line in data:
        dengji = grade.grade(line["score"])
        if dengji not in result:
            result[dengji] = []
        result[dengji].append(line["name"])
    return result