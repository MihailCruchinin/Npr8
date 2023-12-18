from Soda import Soda
from Triangle import triangle
from KgToPound import KgToPounds
from Nikola import Nikolay
from RealString import RealString

def cl1():
    soda1= Soda()
    soda2= Soda("hhhh")
    soda1.show_my_drink()
    soda2.show_my_drink()
def cl2(a,b,c):
    Triangle= triangle(a,b,c)
    Triangle.is_triangle()
def cl3(a):
    srav= KgToPounds(a)
    print(srav.pounds)
def cl4():
    nikola=Nikolay("Nikolay")
    maxim=Nikolay("Maxim")
    print(nikola.Name)
    print(maxim.Name)
def cl5(str1, str2):
    rs= RealString(str1, str2)
    rs.sr()
cl5("hhhh","hhhh")