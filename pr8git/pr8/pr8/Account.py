class Account(object):
    def __init__(self, number: int, tranlist: List[Transaktion]):
        self.__number=number
        self.__name=name
        self.__tranlist=tranlist
    def setname(self, name: string):
        if len(name)>=4:
            self.__name=name
        else: raise ValueError("Need more than 3 letter")
    def getname(self):
        return self.__name
    def __len__(self):
        return len(self.__tranlist)
    @property
    def balance(self):
        a=0
        for tran in self.__tranlist:
            a+=tran.usd
        return
    @property
    def all_usd(self):
        for tran in self.__tranlist:
            if tran.cu!= "USD":
                return False
        return True
    def apply(self, tran: Transaktion):
        self.__tranlist.Append(tran)
