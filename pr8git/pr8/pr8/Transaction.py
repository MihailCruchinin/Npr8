class Transaktion(object):
    def __init__(self, summ, date, cu="USD", cource=1, desc="none"):
       self.__summ=summ
       self.__date=date
       self.__cu=cu
       self.__cource=cource
       self.__desc=desc
    pass
    @property
    def amount(self):
        return self.__summ
    @property
    def date(self):
        return self.__date
    @property
    def cu(self):
        return self.__cu
    @property
    def rate(self):
        return self.__cource

    @property
    def usd(self):
        self.__usd=self.__summ*self.__cource
        return usd


