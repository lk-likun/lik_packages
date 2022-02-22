class Student:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            print(1)
        return cls.instance

    def __init__(self, name, age, school):
        print(2)
        self.name = name
        self.age = age
        self.school = school

    def people(self):
        return self.name, self.age, self.school

    def get_school(self):
        if self.school == '大专':
            return '人上人'
        elif self.school == '本科':
            return '一般'
        else:
            return '高校'


student1 = Student('小明', 18, '985')
print(student1.name)
student2 = Student('小华', 20, '本科')
print(student1.name, student2.name)
# student3 = Student('小刘', 22, '大专')
# print(*student1.people(), student1.get_school())
# print(*student2.people(), student2.get_school())
# print(*student3.people(), student3.get_school())
# print(student1)
