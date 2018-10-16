
class ID:
    def __init__(self,id):
        self.id=id
        self.obervers=[]

    def attach(self,observer):
        if self==observer.id:  #self.id==observer.id  数字！=对象
            self.obervers.append(observer)



class Observer_Subject:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        id.attach(self)
    def Update(self,subject):
        pass
    def NotifyAll(self):
        for observer in self.id.obervers:
            if self !=observer:
                observer.Update(self)


class Member(Observer_Subject):
    def __init__(self,name,id):
        Observer_Subject.__init__(self,name,id)

    def Update(self,subject):
        print("%s发布信息了，%s快接受！"%(subject.name,self.name))


class Manager(Observer_Subject):
    def __init__(self, name, id):
        Observer_Subject.__init__(self, name, id)

    def Update(self, subject):
        print("%s发布信息了，%s快查看！" % (subject.name, self.name))


def main():
    id=ID(3)
    manager1=Manager("张老师",id)
    manager2 = Manager("李老师", id)
    manager3 = Manager("蔡老师", id)
    manager4 = Manager("王老师", id)
    mem1 =Member("小明",id)
    mem2 = Member("小梁", id)
    mem3 = Member("小才", id)
    mem4 = Member("大明", id)
    print("------",id.obervers)
    mem3.NotifyAll()
    manager1.NotifyAll()

if __name__=="__main__":
    main()