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
coeffics = [1, 0, 0, 0]  # первый тест для всех нулевых корней

# при послед тестах вызывать методы обновления коэффициентов

def rand3Coeffs():
    for i in range(1,4):
        coeffics[i] = randint(1, 5)  # получаем 3 рандомных корня
    b = (-1)  * (coeffics[1] + coeffics[2] + coeffics[3])  # b
    c =  (coeffics[1] * coeffics[2] + coeffics[2] * coeffics[3] + coeffics[1] * coeffics[3])  # c
    d = (-1)  * coeffics[1] * coeffics[2] * coeffics[3]  # d
    print("rand3 = ",b,c,d) #ужасный способ дебага
    return [1,b,c,d]

#   [0 ,1 , 2, 3]
#   [a, x0,x1,x2]
#   d = -a*x0*x1*x2
#   a = const
#   c = ax1x2+ax0x1+ax0x2 = a*(x1x2+x0x1+x0x2)
#   b = -2*ax1-ax2-ax0 = -a(x1+x2+x0)

# 1).2
def rand3CoeffsWithI():
    for i in range(1, 3):
        coeffics[i] = randint(1, 5)  # получаем 2 рандомных корня и комплексное число
    iy = complex(0, randint(1, 6))
    coeffics[2] = coeffics[2] + iy
    coeffics[3] = coeffics[2] - 2 * iy
    b = (-1) * (2 * coeffics[2].real + coeffics[1])  # b
    c = (coeffics[2].real * coeffics[2].real + coeffics[3].imag * coeffics[3].imag + 2 * coeffics[1] * coeffics[2].real)  # c
    d = (-1) * coeffics[1] * (coeffics[2].real * coeffics[2].real + coeffics[3].imag * coeffics[3].imag)  # d
    print("rand3I = ",b,c,d) #ужасный способ дебага
    return [1, int(b),int(c),int(d)]


#   [0 , 1 ,2   , 3]
#   [a, x0,x1+iy,x1-iy]
#    d = ax1^2x0+ay^2x0 = -ax0(x1^2+y^2)
#    a = const
#    c = ax1^2+ay^2+2ax0x1 = a(x1^2 + y^2 + 2x0x1)
#    b = -2*ax1-ax0 = -a(2*x1+x0)


coeffics2 = [1,0,0,0,0]
def rand4Coeffs():
    for i in range(1,5):
        coeffics2[i] = randint(1, 5)  # получаем 4 рандомных корня
    b = (-1)*(coeffics2[1]+coeffics2[2]+coeffics2[3]+coeffics2[4])  # b
    c =  (coeffics2[4]*(coeffics2[3]+coeffics2[2])+coeffics2[1]*(coeffics2[4]+coeffics2[3]+coeffics2[2])+coeffics2[2]*coeffics2[3])  # c
    d = (-1)*(coeffics2[2]*coeffics2[3]*coeffics2[4]+coeffics2[1]*(coeffics2[2]*(coeffics2[4]+coeffics2[2])+coeffics2[2]*coeffics2[3]))  # d
    e = coeffics2[1]*coeffics2[2]*coeffics2[3]*coeffics2[4]
    print("rand4 = ",b,c,d,e) #ужасный способ дебага
    return [1,b,c,d,e]

#    [0, 1,  2,  3 , 4 ]
#    [a, x0, x1, x2, x3]
#    a = rand()
#    b = a(-x0 - x1 - x2 - x3) = -a(x0+x1+x2+x3)
#    c = a(x2x3 + x1x3 + x1x2 + x0x3 + x0x2 + x0x1) = a(x3(x2+x1) + x0(x3+x2+x1)+ x1x2)
#    d = a(-x1x2x3 - x0x2x3 - x0x1x3 - x0x1x2) = -a(x1x2x3 + x0(x2(x3+x1)+x1x3))
#    e = a * x0 * x1 * x2 * x3 - должен быть делителем корня


class MyTestCase(unittest.TestCase):

    def testData(self): #1 [1,-3,-9,27] коэффициенты, [1,3,3,-3] мои рандомные корни,корни photomath [3,-3,3] ,корни метода (-15.0, (9+0j), (9+0j))
        self.assertEqual(solve(Polynomials(rand3Coeffs())), coeffics)

    def testData2(self): #1 [-11.0 39.0 -29.0], [1, 1, (5+2j), (5-2j)], [-11.740740740740753, (11.370370370370376[57 chars]95j)], [1, а тут руками считал (5+2i),(5-2i)]
        self.assertEqual(bezout(Polynomials(rand4Coeffs())), coeffics2)

    def testData3(self):  # 3
        self.assertEqual(bezout(Polynomials(rand4Coeffs())), coeffics2)

    def testData4(self):  # 4
        self.assertEqual(bezout(Polynomials(rand4Coeffs())), coeffics2)

    def testData5(self):  # 5
        self.assertEqual(bezout(Polynomials(rand4Coeffs())), coeffics2)

    def testData6(self):  # 6
        self.assertEqual(bezout(Polynomials(rand4Coeffs())), coeffics2)

    def testData7(self):  # 7
        self.assertEqual(solve(Polynomials(rand3Coeffs())), coeffics)

    def testData8(self):  # 8
        self.assertEqual(solve(Polynomials(rand3Coeffs())), coeffics)

    def testData9(self):  # 9
        self.assertEqual(solve(Polynomials(rand3Coeffs())), coeffics)

    def testData10(self):  # 10
        self.assertEqual(solve(Polynomials(rand3Coeffs())), coeffics)

    def testData11(self):  # 11
        self.assertEqual(solve(Polynomials(rand3Coeffs())), coeffics)

    def testData12(self):  # 12
        self.assertEqual(solve(Polynomials(rand3Coeffs())), coeffics)

    def testData13(self):  # 13
        self.assertEqual(solve(Polynomials(rand3Coeffs())), coeffics)

    def testData14(self):  # 14
        self.assertEqual(solve(Polynomials(rand3Coeffs())), coeffics)

    def testData15(self):  # 15
        self.assertEqual(solve(Polynomials(rand3Coeffs())), coeffics)

    def testData16(self):  # 16
        self.assertEqual(solve(Polynomials(rand3Coeffs())), coeffics)

    def testData17(self):  # 17
        self.assertEqual(solve(Polynomials(rand3CoeffsWithI())), coeffics)

    def testData18(self):  # 18
        self.assertEqual(solve(Polynomials(rand3CoeffsWithI())), coeffics)

    def testData19(self):  # 19
        self.assertEqual(solve(Polynomials(rand3CoeffsWithI())), coeffics)

    def testData20(self):  # 20
        self.assertEqual(solve(Polynomials(rand3CoeffsWithI())), coeffics)

    def testData21(self):  # 21
        self.assertEqual(solve(Polynomials(rand3CoeffsWithI())), coeffics)

    def testData22(self):  # 22
        self.assertEqual(solve(Polynomials(rand3CoeffsWithI())), coeffics)

    def testData23(self):  # 23
        self.assertEqual(solve(Polynomials(rand3CoeffsWithI())), coeffics)

    def testData24(self):  # 24
        self.assertEqual(solve(Polynomials(rand3CoeffsWithI())), coeffics)

    def testData25(self):  # 25
        self.assertEqual(solve(Polynomials(rand3CoeffsWithI())), coeffics)

    def testData26(self):  # 26
        self.assertEqual(solve(Polynomials(rand3CoeffsWithI())), coeffics)

    def testData27(self):  # 27
        self.assertEqual(bezout(Polynomials(rand4Coeffs())), coeffics2)

    def testData28(self):  # 28
        self.assertEqual(bezout(Polynomials(rand4Coeffs())), coeffics2)

    def testData29(self):  # 29
        self.assertEqual(bezout(Polynomials(rand4Coeffs())), coeffics2)

    def testData30(self):  # 30
        self.assertEqual(bezout(Polynomials(rand4Coeffs())), coeffics2)

    def testData31(self):  # 31
        self.assertEqual(bezout(Polynomials(rand4Coeffs())), coeffics2)
        


if __name__ == '__main__':
    unittest.main()
