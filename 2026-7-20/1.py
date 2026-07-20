#练习class语法
class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages

    def is_long(self):
        return self.pages >= 300
    
    def describe(self):
        return f"《{self.title}》有{self.pages}页"
    
s1 = Book("漫画",264)
s2 = Book("小说",500)

print(s1.title,s1.describe(),s1.is_long())
print(s2.title,s2.describe(),s2.is_long())
