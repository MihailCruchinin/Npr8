class RealString(object):
    def __init__(self, string1, string2):
        self.string1= string1
        self.string2= string2
    def sr(self):
        if len(self.string1)<len(self.string2):
            print("string1<string2")
        if len(self.string1)>len(self.string2):
            print("string1>string2")
        if len(self.string1)==len(self.string2):
            print("string1=string2")
    def __len__(self):
        return [len(self.string1), len(self.string2)]




