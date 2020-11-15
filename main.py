# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Programs.program_1 import MydateandTime
from Programs.program_2 import Area
from Programs.program_3 import Name_Surname
from address import Address
from student import Student
from classromm import Classroom
from testcases import Testcases


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # First program

    mydateTime = MydateandTime()
    mydateTime.currentDateAndTime()

    # second program

    area = Area()
    area.area_of_circle(12)

    area.area_of_square(7)

    # program 3

    name = Name_Surname()
    name.lastname_firstname("shreya", "Patil")
    name.lastname_firstname("saurabh", "Mendhe")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# address = Address("101", "444603", "Pune", "India", "abcd")
# student = Student("Shreya", "27", "A2000", "5'4", address)
# address1 = Address("107", "444603", "dhh", "Sweden", "abcd")
# student1 = Student("Saurabh", "27", "A2000", "5'4", address1)
# classroom = Classroom("sdgf", "777", "2021", student)
# testcases = Testcases()
#
# student.displayinformation()
# student1.displayinformation()
# classroom.displayinfo()
# # testcases.scenario1()
# # testcases.scenario2()
# # testcases.scenario3()
# testcases.scenario4()
# testcases.stoptestcases()

