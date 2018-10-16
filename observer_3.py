class Subject():
    def __init__(self,name):
        self.observers=[]
        self.name=name
    def attach(self,observer):
        print("%s  attach  %s"%(self.name,observer.name))
        self.observers.append(observer)
    def NotifyAll(self):
       for observer in self.observers:
           #print(observer.name)
           observer.Update(self)   #(self)对象

class SchoolMaster(Subject):
    def __init__(self,name):
        Subject.__init__(self,name)

class Observer():
    def __init__(self,name):
        self.name=name
    def Update(self,subject):
        self.subject=subject

class Teacher(Subject,Observer):
    def __init__(self,name):
        Subject.__init__(self,name)
    def Update(self,subject=None):
            self.subject=subject
            print("%s,做好一点，%s来了\n" % (self.name, self.subject.name))


class WaiMai(Observer):
    def __init__(self,name):
        Observer.__init__(self,name)

    def Update(self,subject):
        self.subject=subject
        print("%s,赶紧收摊，%s来了\n"%(self.name,self.subject.name))

class Student(Observer):
    def __init__(self,name):
        Observer.__init__(self,name)

    def Update(self,subject):

        self.subject = subject
        print("%s,别撸了，%s要来了,赶紧学习\n"%(self.name,self.subject.name))  #并不需要说明对象类型，父类即可


def main():
    xiaozhang=SchoolMaster("张校长")
    teacher=Teacher("张老师")
    #print(teacher.name)
    stu1=Student("鲁同学")
    stu2 = Student("李同学")
    waimai=WaiMai("张三")
    xiaozhang.attach(stu1)
    xiaozhang.attach(stu2)
    xiaozhang.attach(waimai)
    xiaozhang.attach(teacher)
    xiaozhang.NotifyAll()

    teacher.attach(stu1)
    teacher.attach(stu2)
    teacher.attach(waimai)
    teacher.NotifyAll()



if __name__=="__main__":
    main()