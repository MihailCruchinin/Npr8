class triangle:
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c
    def is_triangle(self):
        try:
            float(self.a)
            float(self.b)
            float(self.c)
            if self.a<0 or self.b<0 or self.c<0:
                print("No negative number")
            else:
                if self.a+self.b>self.c and self.a+self.c>self.b and self.c+self.b>self.a:
                    print("Right triangle")
                else: print("Wrong triangle")
        except:
            print("Wrong format")
        
    pass




