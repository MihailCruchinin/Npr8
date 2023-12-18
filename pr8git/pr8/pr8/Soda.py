class Soda(object):
    def __init__(self,addition=""):
        self.addition = addition;
    def show_my_drink(self):
        if self.addition !="":
            print("Soda with "+ self.addition)
        else:
            print("Regular soda")
    pass



