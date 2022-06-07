import unittest

from random import randint
import array
from bezout import bezout
from Polynomials.cores import Polynomials
from cubic import solve
from method2 import method_cardano_descartes

"""
Рассмотрим 3 случая
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
    coeffics[3] = coeffics[2] - 2*iy
    b = (-1) * a * (2 * coeffics[2] + coeffics[1])  # b
    c = a * (coeffics[2] * coeffics[2] + coeffics[3] * coeffics[3] + 2 * coeffics[1] * coeffics[2])  # c
    d = (-1) * a * coeffics[1] * (coeffics[2] * coeffics[2] + coeffics[3] * coeffics[3])  # d
    return [a,b,c,d]


#   [0 , 1 ,2   , 3]
#   [a, x0,x1+iy,x1-iy]
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
    c = a * (coeffics[4] * (coeffics[3] + coeffics[2]) + coeffics[1](coeffics[4] + coeffics[3]+coeffics[2]) + coeffics[2]*coeffics[3])  # c
    d = (-1) * a *(coeffics[2] * coeffics[3] * coeffics[4] + coeffics[1](coeffics[2](coeffics[4]+coeffics[2]) + coeffics[2]*coeffics[3]))  # d
    e = a * coeffics[0]*coeffics[1]*coeffics[2]*coeffics[3]*coeffics[4]
    return [a,b,c,d,e]

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
        self.assertEqual(bezout(rand3Coeffs(coeffics)), coeffics)

    def testData7(self):  #7
        self.assertEqual(solve(rand3Coeffs(coeffics)), coeffics)

    def testData8(self):  #8
        self.assertEqual(solve(rand3Coeffs(coeffics)), coeffics)

    def testData9(self):  #9
        self.assertEqual(solve(rand3Coeffs(coeffics)), coeffics)

    def testData10(self):  #10
        self.assertEqual(solve(rand3Coeffs(coeffics)), coeffics)

    def testData11(self):  #11
        self.assertEqual(solve(rand3Coeffs(coeffics)), coeffics)

    def testData12(self):  #12
        self.assertEqual(solve(rand3Coeffs(coeffics)), coeffics)

    def testData13(self):  #13
        self.assertEqual(solve(rand3Coeffs(coeffics)), coeffics)

    def testData14(self):  #14
        self.assertEqual(solve(rand3Coeffs(coeffics)), coeffics)

    def testData15(self):  #15
        self.assertEqual(solve(rand3Coeffs(coeffics)), coeffics)

    def testData16(self):  #16
        self.assertEqual(solve(rand3Coeffs(coeffics)), coeffics)
        
    def testData17(self): #17
        self.assertEqual(solve(rand3CoeffsWithI(coeffics)), coeffics)

    def testData18(self): #18
        self.assertEqual(solve(rand3CoeffsWithI(coeffics)), coeffics)

    def testData19(self): #19
        self.assertEqual(solve(rand3CoeffsWithI(coeffics)), coeffics)

    def testData20(self): #20
        self.assertEqual(solve(rand3CoeffsWithI(coeffics)), coeffics)

    def testData21(self): #21
        self.assertEqual(solve(rand3CoeffsWithI(coeffics)), coeffics)

    def testData22(self): #22
        self.assertEqual(solve(rand3CoeffsWithI(coeffics)), coeffics)

    def testData23(self): #23
        self.assertEqual(solve(rand3CoeffsWithI(coeffics)), coeffics)

    def testData24(self): #24
        self.assertEqual(solve(rand3CoeffsWithI(coeffics)), coeffics)

    def testData25(self): #25
        self.assertEqual(solve(rand3CoeffsWithI(coeffics)), coeffics)

    def testData26(self): #26
        self.assertEqual(solve(rand3CoeffsWithI(coeffics)), coeffics)

    def testData27(self): #27
        self.assertEqual(bezout(rand3CoeffsWithI(coeffics)), coeffics)

    def testData28(self): #28
        self.assertEqual(bezout(rand3CoeffsWithI(coeffics)), coeffics)

    def testData29(self): #29
        self.assertEqual(bezout(rand3CoeffsWithI(coeffics)), coeffics)

    def testData30(self): #30
        self.assertEqual(bezout(rand3CoeffsWithI(coeffics)), coeffics)

    def testData31(self): #31
        self.assertEqual(bezout(rand3CoeffsWithI(coeffics)), coeffics)

    def testData32(self): #32
        self.assertEqual(bezout(rand3CoeffsWithI(coeffics)), coeffics)

    def testData33(self): #33
        self.assertEqual(bezout(rand3CoeffsWithI(coeffics)), coeffics)

    def testData34(self): #34
        self.assertEqual(bezout(rand3CoeffsWithI(coeffics)), coeffics)

    def testData35(self): #35
        self.assertEqual(bezout(rand3CoeffsWithI(coeffics)), coeffics)

    def testData36(self): #36
        self.assertEqual(bezout(rand3CoeffsWithI(coeffics)), coeffics)
        
    def testData37(self): #37
        self.assertEqual(bezout(rand4Coeffs(coeffics)), coeffics)

    def testData38(self): #38
        self.assertEqual(bezout(rand4Coeffs(coeffics)), coeffics)

    def testData39(self): #39
        self.assertEqual(bezout(rand4Coeffs(coeffics)), coeffics)

    def testData40(self): #40
        self.assertEqual(bezout(rand4Coeffs(coeffics)), coeffics)
        
    def testData41(self): #41
        self.assertEqual(bezout(rand4Coeffs(coeffics)), coeffics)

    def testData42(self): #42
        self.assertEqual(bezout(rand4Coeffs(coeffics)), coeffics)

    def testData43(self): #43
        self.assertEqual(bezout(rand4Coeffs(coeffics)), coeffics)

    def testData44(self): #44
        self.assertEqual(bezout(rand4Coeffs(coeffics)), coeffics)
        


if __name__ == '__main__':
    unittest.main()
