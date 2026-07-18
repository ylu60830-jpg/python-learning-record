import grade
def chaxun(name,item):
    for num in item:
        if num["name"] == name :
            return grade.grade(num["score"])