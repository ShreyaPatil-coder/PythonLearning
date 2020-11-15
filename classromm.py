from student import Student
class Classroom:
    def __init__(self,name,class_no,year,student):
        self.name = name
        self.class_no = class_no
        self.year = year
        self.student = student

    def displayinfo(self):
        print("%s is the part of class name is %s.class_no is %s. class year is %s. and adrress is %s" % (self.student.name,self.name,self.class_no,self.year,self.student.address.city))


