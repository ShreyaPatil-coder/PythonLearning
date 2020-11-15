class Address:
    def __init__(self, home_no, pincode, city, country, street_name):
        self.home_no = home_no
        self.pincode = pincode
        self.city = city
        self.country = country
        self.street_name = street_name

    def addressinfo(self):
        print("home no is %s.pincode is %s.city name is %s.country name is %s.street name is %s." % (
        self.home_no, self.pincode, self.city, self.country, self.street_name))
