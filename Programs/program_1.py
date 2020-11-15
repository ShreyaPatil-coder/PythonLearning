from datetime import datetime


class MydateandTime:

    def __init__(self):
        pass

    def currentDateAndTime(self):
        now = datetime.now()
        print("Current date and time : " + str(now))
        print (now.strftime("%Y-%m-%d %H:%M:%S"))