class Student:
    def __init__(self, name, age, rollnumber, height, address):
        self.age = age
        self.name = name
        self.rollnumber = rollnumber
        self.height = height
        self.address = address

    def displayinformation(self):
        print("Student name is %s. Age is %s. Rollnumer is %s, Height is %s. Address is (%s %s %s %s %s)" % (
        self.name, self.age, self.rollnumber, self.height, self.address.country, self.address.home_no,
        self.address.city, self.address.street_name, self.address.pincode))
