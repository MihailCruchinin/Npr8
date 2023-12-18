class KgToPounds:

    def __init__(self, kg):
        self.__kg=kg;
        if isinstance(kg, (int, float)):
            self.__kg = kg
        else:
            raise ValueError("Wrong format")
    @property
    def pounds(self):
        return self.__kg * 2.205

    
    @property    
    def kg(self):
        return self.__kg