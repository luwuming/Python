class Subject():
    observers=[]
    def __init__(self,name):
        self.name=name
    def attach(self,observer):
         self.observers.append(observer)
    # def getName(self):
    #     return self.name
    # def __get__(self):
    #     return self.name
    # def __set__(self,name):
    #     self.name=name
    def NotifyAll(self):

       for observer in self.observers:
           print(observer.name)
           observer.Update()   #(self)对象

class SchoolMaster(Subject):
    def __init__(self,name):
        Subject.__init__(self,name)

class Observer():
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject
    # def __get__(self):
    #     return self.name
    # def __set__(self,name):
    #     self.name=name
    def Update(self):
        pass
class Teacher(Subject,Observer):
    def __init__(self,name,subject=None):
        self.subject=subject
        Subject.__init__(self,name)
    def getSubject(self):
        return self.subject
    def __get__(self):
        return self.subject
    def __set__(self,subject):
        self.subject=subject
    def Update(self):
        print("%s,做好一点，%s来了\n" % (self.name, self.subject.name))


class WaiMai(Observer):
    def __init__(self,name,teacher):
        Observer.__init__(self,name,teacher)

    def Update(self):
        print("%s,赶紧收摊，%s来了\n"%(self.name,self.subject.name))

class Student(Observer):
    def __init__(self,name,teacher):
        Observer.__init__(self,name,teacher)

    def Update(self):
        print("%s,别撸了，%s要来了,赶紧学习\n"%(self.name,self.subject.name))  #并不需要说明对象类型，父类即可


def main():
    xiaozhang=SchoolMaster("张校长")
    teacher=Teacher("张老师",xiaozhang)
    #print(teacher.name)
    stu1=Student("鲁同学",xiaozhang)
    stu2 = Student("李同学",xiaozhang)
    waimai=WaiMai("张三",xiaozhang)
    xiaozhang.attach(stu1)
    xiaozhang.attach(stu2)
    xiaozhang.attach(waimai)
    xiaozhang.attach(teacher)
    xiaozhang.NotifyAll()


if __name__=="__main__":
    main()