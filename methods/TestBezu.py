import unittest

from random import randint
import array
from bezout import bezout
from Polynomials.cores import Polynomials

"""
Рассмотрим 3 случая и в каждом из них ещё 2
1).1 Пусть будет коэффициент при x^3 = rand()
    Тогда имеем общий вид ax^3 + bx^2 + cx + d = 0
    И корни выглядят, как a(x-x0)(x-x1)(x-x2) =>
    => в общем виде оно выглядит следующим образом
    (x-x0)(a(x-x1)(x-x2)) = x(a(x-x1)(x-x2)) - x0(a(x-x1)(x-x2)) = 
    = x(ax^2 +ax1x2-ax1x-ax2x) - x0(ax^2 +ax1x2-ax1x-ax2x)) = 
    ax^3 + ax1x2x-ax1x^2-ax2x^2 - ax0x^2 - ax0x1x2 +ax0x1x +ax0x2x = 
    (a)x^3 + x^2 (-ax1 -ax2 - ax0) + x(ax1x2 + ax0x1 + ax0x2) - ax0x1x2

    [a,x0,x1,x2,b,c,d]
    d = -a*x0*x1*x2
    a = const
    c = ax1x2+ax0x1+ax0x2 = a*(x1x2+x0x1+x0x2)
    b = -ax1-ax2-ax0 = -a(x1+x2+x0)

    1).2для комплексных чисел
    [a,x0,x1,iy,b,c,d]
    (x-x0)(a(x-(x1+iy))(x-(x1-iy))) = ax^3 + x^2(-2*ax1-ax0)+ x(ax1^2+ay^2+2ax0x1) - ax1^2x0 - ay^2x0
    d = ax1^2x0+ay^2x0 = -ax0(2*x1^2+y^2)
    a = const
    c = ax1^2+ay^2+2ax0x1 = a(x1^2 + y^2 + 2x0x1)
    b = -2*ax1-ax0 = -a(2*x1+x0)


2) Пусть будет коэффициент при x^3 = 1
    И корни выглядят, как (x-x0)(x-x1)(x-x2)

    2).1[a,x0,x1,x2]
    d = -1*x0*x1*x2
    a = 1
    c = 1x1x2+1x0x1+1x0x2 = x1x2+x0x1+x0x2
    b = -1x1-1x2-1x0 = (-1)*(x1+x2+x0)

    2).2для комплексных чисел
    [a,x0,x1,iy]
    (x-x0)(a(x-(x1+iy))(x-(x1-iy))) = ax^3 + x^2(-2*ax1-ax0)+ x(ax1^2+ay^2+2ax0x1) - ax1^2x0 - ay^2x0
    d = -ax1^2x0-ay^2x0 = -x0(2*x1^2+y^2)
    a = 1
    c = ax1^2+ay^2+2ax0x1 = (x1^2 + y^2 + 2x0x1)
    b = -2*ax1-ax0 = -(2*x1+x0)

3) Пусть будет коэффициент при x^4 = rand()
    И корни выглядят, как a(x-x0)(x-x1)(x-x2)(x-x3)

    [a, x0,x1,x2,x3]
    a = rand()
    b = a(-x0-x1-x2-x3)
    c = a(x2x3 + x1x3 + x1x2 + x0x3 + x0x2 + x0x1)
    d = a(-x1x2x3-x0x2x3-x0x1x3-x0x1x2)
    e = a*x0*x1*x2*x3
"""

# 1).1
coeffics = [0, 0, 0, 0]  # первый тест для всех нулевых корней

# начальные коэффициенты
a = 0
b = 0
c = 0
d = 0

# при послед тестах вызывать методы обновления коэффициентов

def rand3Coeffs(coeffics):
    for i in range(3):
        coeffics[i] = randint(-100, 100)  # получаем 3 рандомных корня
    a = randint(-100,100)
    coeffics.insert(0, a)
    b = (-1) * a * (coeffics[1] + coeffics[2] + coeffics[3])  # b
    c = a * (coeffics[1] * coeffics[2] + coeffics[2] * coeffics[3] + coeffics[1] * coeffics[3])  # c
    d = (-1) * a * coeffics[1] * coeffics[2] * coeffics[3]  # d
    return [a,b,c,d]


#   [0 ,1 , 2, 3]
#   [a, x0,x1,x2]
#   d = -a*x0*x1*x2
#   a = const
#   c = ax1x2+ax0x1+ax0x2 = a*(x1x2+x0x1+x0x2)
#   b = -2*ax1-ax2-ax0 = -a(x1+x2+x0)

# 1).2
def rand3CoeffsWithI(coeffics):
    for i in range(2):
        coeffics[i] = randint(-100, 100)  # получаем 2 рандомных корня и комплексное число
    a = randint(-100, 100)
    coeffics.insert(0,a)
    iy = complex(0,randint(-100,100))
    coeffics[2] = coeffics[2] + iy
    coeffics[3] = coeffics[3] - iy
    b = (-1) * a * (2 * coeffics[2] + coeffics[1])  # b
    c = a * (coeffics[2] * coeffics[2] + coeffics[3] * coeffics[3] + 2 * coeffics[1] * coeffics[2])  # c
    d = (-1) * a * coeffics[1] * (coeffics[2] * coeffics[2] + coeffics[3] * coeffics[3])  # d
    return [a,b,c,d]


#   [0 , 1 ,2, 3]
#   [a, x0,x1,iy]
#    d = ax1^2x0+ay^2x0 = -ax0(x1^2+y^2)
#    a = const
#    c = ax1^2+ay^2+2ax0x1 = a(x1^2 + y^2 + 2x0x1)
#    b = -2*ax1-ax0 = -a(2*x1+x0)



def rand4Coeffs(coeffics):
    for i in range(4):
        coeffics[i] = randint(-100, 100)  # получаем 4 рандомных корня
    a = randint(-100,100)
    coeffics.insert(0, a)
    b = (-1)* a * (coeffics[1] + coeffics[2] + coeffics[3] + coeffics[4])  # b
    c = a * (coeffics[1] * coeffics[2] + coeffics[2] * coeffics[3] + coeffics[1] * coeffics[3])  # c
    d = (-1) * a * coeffics[1] * coeffics[2] * coeffics[3]  # d
    return [a,b,c,d]



#    [0, 1,  2,  3 , 4 ]
#    [a, x0, x1, x2, x3]
#    a = rand()
#    b = a(-x0 - x1 - x2 - x3) = -a(x0+x1+x2+x3)
#    c = a(x2x3 + x1x3 + x1x2 + x0x3 + x0x2 + x0x1) = a(x3(x2+x1) + x0(x3+x2+x1)+ x1x2)
#    d = a(-x1x2x3 - x0x2x3 - x0x1x3 - x0x1x2) = -a(x1x2x3 + x0(x2(x3+x1)+x1x3))
#    e = a * x0 * x1 * x2 * x3

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.bezu = bezout(Polynomial(coeffics))  # создаём объект и инициализируем его коэффициентами

    def testData(self): #1
        self.assertEqual(self.bezu, coeffics)  # сперва пишем метод класса, который выводит корни,
                                                                   # затем пишем  массив с корнями для сравнения
    def testData2(self): #2
        self.assertEqual(bezout(rand3Coeffs(coeffics)), coeffics)

    def testData3(self): #3
        self.assertEqual(bezout(rand3Coeffs(coeffics)), coeffics)

    def testData4(self): #4
        self.assertEqual(bezout(rand3Coeffs(coeffics)), coeffics)

    def testData5(self): #5
        self.assertEqual(bezout(rand3Coeffs(coeffics)), coeffics)

    def testData6(self): #6
        self.assertEqual(bezout(rand3CoeffsWithI(coeffics)), coeffics)

    def testData7(self): #7
        self.assertEqual(bezout(rand3CoeffsWithI(coeffics)), coeffics)

    def testData8(self): #8
        self.assertEqual(bezout(rand3CoeffsWithI(coeffics)), coeffics)

    def testData9(self): #9
        self.assertEqual(bezout(rand3CoeffsWithI(coeffics)), coeffics)

    def testData10(self): #10
        self.assertEqual(bezout(rand3CoeffsWithI(coeffics)), coeffics)


































if __name__ == '__main__':
    unittest.main()
