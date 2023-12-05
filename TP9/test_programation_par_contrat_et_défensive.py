from unittest import TestCase
from programation_par_contrat_et_défensive import Fraction


class TestFraction(TestCase):
    def test___init__(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(-10, 5)
        frac3 = Fraction(10, -5)
        frac4 = Fraction(-10, -5)
        frac5 = Fraction(0, 5)

        # 1 default
        self.assertEqual(frac.numerator, 0, "__init__ : test du numérateur par défaut")
        self.assertEqual(frac.denominator, 1, "__init__ : test du denominator par défaut")
        # 2 normal
        self.assertEqual(frac1.numerator, 10, "__init__ : test du numérateur normal")
        self.assertEqual(frac1.denominator, 5, "__init__ : test du denominator normal")
        # 3 négatif num
        self.assertEqual(frac2.numerator, -10, "__init__ : test du numérateur avec un num  négatif")
        self.assertEqual(frac2.denominator, 5, "__init__ : test du denominator négatif avec un num  négatif")
        # 4 négatif den
        self.assertEqual(frac3.numerator, -10, "__init__ : test du numérateur avec un den  négatif")
        self.assertEqual(frac3.denominator, 5, "__init__ : test du denominator normal avec un den  négatif")
        # 5 nagatif num and den
        self.assertEqual(frac4.numerator, 10, "__init__ : test du numérateur normal avec un den et num  négatif")
        self.assertEqual(frac4.denominator, 5, "__init__ : test du denominator normal avec un den et num négatif")
        # 6 zéro num
        self.assertEqual(frac5.numerator, 0, "__init__ : test du numérateur avec un num égal à 0")
        self.assertEqual(frac5.denominator, 5, "__init__ : test du denominator avec un num égal à 0")
        # 7 raise: zéro den
        self.assertRaises(ZeroDivisionError, Fraction, 1, 0)

        # 8 default (simplifier)
        self.assertEqual(frac.numerator_simplifiee, 0, "__init__ : test du numérateur par défaut")
        self.assertEqual(frac.denominator_simplifiee, 1, "__init__ : test du denominator par défaut")
        # 9 normal (simplifier)
        self.assertEqual(frac1.numerator_simplifiee, 2, "__init__ : test du numérateur normal")
        self.assertEqual(frac1.denominator_simplifiee, 1, "__init__ : test du denominator normal")
        # 10 négatif num (simplifier)
        self.assertEqual(frac2.numerator_simplifiee, -2, "__init__ : test du numérateur avec un num  négatif")
        self.assertEqual(frac2.denominator_simplifiee, 1, "__init__ : test du denominator négatif avec un num  négatif")
        # 11 négatif den (simplifier)
        self.assertEqual(frac3.numerator_simplifiee, -2, "__init__ : test du numérateur avec un den  négatif")
        self.assertEqual(frac3.denominator_simplifiee, 1, "__init__ : test du denominator normal avec un den  négatif")
        # 12 nagatif num and den (simplifier)
        self.assertEqual(frac4.numerator_simplifiee, 2, "__init__ : test du numérateur normal avec un den et num  négatif")
        self.assertEqual(frac4.denominator_simplifiee, 1, "__init__ : test du denominator normal avec un den et num négatif")
        # 13 zéro num (simplifier)
        self.assertEqual(frac5.numerator_simplifiee, 0, "__init__ : test du numérateur avec un num égal à 0")
        self.assertEqual(frac5.denominator_simplifiee, 1, "__init__ : test du denominator avec un num égal à 0")
        pass

    def test___str__(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(-10, 5)
        frac3 = Fraction(10, -5)
        frac4 = Fraction(-10, -5)
        frac5 = Fraction(0, 5)

        # 1 default
        self.assertEqual(frac.__str__(), "0.0/1.0", "__str__ : test du numérateur par défaut")
        # 2 normal
        self.assertEqual(frac1.__str__(), "2.0/1.0", "__str__ : test du numérateur normal")
        # 3 négatif num
        self.assertEqual(frac2.__str__(), "-2.0/1.0", "__str__ : test du numérateur avec un num  négatif")
        # 4 négatif den
        self.assertEqual(frac3.__str__(), "-2.0/1.0", "__str__ : test du numérateur avec un den  négatif")
        # 5 nagatif num and den
        self.assertEqual(frac4.__str__(), "2.0/1.0", "__str__ : test du numérateur normal avec un den et num  négatif")
        # 6 zéro num
        self.assertEqual(frac5.__str__(), "0.0/1.0", "__str__ : test du numérateur avec un num égal à 0")

    def test_as_mixed_number(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(-10, 5)
        frac3 = Fraction(10, -5)
        frac4 = Fraction(-10, -5)
        frac5 = Fraction(0, 5)
        frac6 = Fraction(11, 5)

        # 1 default
        self.assertEqual(frac.as_mixed_number(), "0 + 0.0/1.0", "as_mixed_number : test par défaut")
        # 2.1 normal
        self.assertEqual(frac1.as_mixed_number(), "2 + 0.0/1.0", "as_mixed_number : test  normal 1")
        # 2.2 normal 1
        self.assertEqual(frac6.as_mixed_number(), "2 + 1.0/5.0", "as_mixed_number : test normal 2")
        # 3 négatif num
        self.assertEqual(frac2.as_mixed_number(), "-2 + 0.0/1.0", "as_mixed_number : test avec un num  négatif")
        # 4 négatif den
        self.assertEqual(frac3.as_mixed_number(), "-2 + 0.0/1.0", "as_mixed_number : test avec un den  négatif")
        # 5 nagatif num and den
        self.assertEqual(frac4.as_mixed_number(), "2 + 0.0/1.0",
                         "as_mixed_number : test normal avec un den et num  négatif")
        # 6 zéro num
        self.assertEqual(frac5.as_mixed_number(), "0 + 0.0/1.0", "as_mixed_number : test avec un num égal à 0")

    def test___add__(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(11, 5)
        frac3 = Fraction(-10, 5)
        frac4 = Fraction(10, -5)
        #frac5 = Fraction(-10, -5)
        frac6 = Fraction(0, 5)

        other = Fraction()
        other1 = Fraction(10, 5)
        other2 = Fraction(11, 5)
        other3 = Fraction(-10, 5)
        other4 = Fraction(10, -5)
        other5 = Fraction(-10, -5)
        #other6 = Fraction(0, 5)

        # 1 default
        self.assertEqual(frac.__add__(other).__str__(), "0.0/1.0", "__add__ : test du str par défaut")
        # 2 normal
        self.assertEqual(frac1.__add__(other2).__str__(), "21.0/5.0", "__add__ : test du str normal 1")
        # 3 négatif num
        self.assertEqual(frac3.__add__(other1).__str__(), "0.0/1.0", "__add__ : test du str avec un num negatif ")
        # 4 négatif den
        self.assertEqual(frac4.__add__(other2).__str__(), "1.0/5.0", "__add__ : test du str avec un den  négatif")
        # 5 nagatif num and den
        self.assertEqual(frac2.__add__(other5).__str__(), "21.0/5.0",
                         "__add__ : test du str avec un nagatif num and den")
        # 6 nagatif num and den
        self.assertEqual(frac3.__add__(other5).__str__(), "0.0/1.0",
                         "__add__ : test du str avec un nagatif num and den")
        # 7 nagatif num and den
        self.assertEqual(frac6.__add__(other1).__str__(), "2.0/1.0", "__add__ : test du str normal avec num = 0")
        # 8 zéro num
        self.assertEqual(frac6.__add__(other3).__str__(), "-2.0/1.0",
                         "__add__ : test du str avec un zéro num + negatif num")
        # 9 zéro num
        self.assertEqual(frac6.__add__(other4).__str__(), "-2.0/1.0",
                         "__add__ : test du str avec un zéro num + negatif num")

    def test___sub__(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(11, 5)
        frac3 = Fraction(-10, 5)
        frac4 = Fraction(10, -5)
        #frac5 = Fraction(-10, -5)
        frac6 = Fraction(0, 5)

        other = Fraction()
        other1 = Fraction(10, 5)
        other2 = Fraction(11, 5)
        other3 = Fraction(-10, 5)
        other4 = Fraction(10, -5)
        other5 = Fraction(-10, -5)
        #other6 = Fraction(0, 5)

        # 1 default
        self.assertEqual(frac.__sub__(other).__str__(), "0.0/1.0", "__sub__ : test du str par défaut")
        # 2 normal
        self.assertEqual(frac1.__sub__(other2).__str__(), "-1.0/5.0", "__sub__ : test du str normal 1")
        # 3 négatif num
        self.assertEqual(frac3.__sub__(other1).__str__(), "-4.0/1.0", "__sub__ : test du str avec un num negatif ")
        # 4 négatif den
        self.assertEqual(frac4.__sub__(other2).__str__(), "-21.0/5.0", "__sub__ : test du str avec un den  négatif")
        # 5 nagatif num and den
        self.assertEqual(frac2.__sub__(other5).__str__(), "1.0/5.0",
                         "__sub__ : test du str avec un nagatif num and den")
        # 6 nagatif num and den
        self.assertEqual(frac3.__sub__(other5).__str__(), "-4.0/1.0",
                         "__sub__ : test du str avec un nagatif num and den")
        # 7 nagatif num and den
        self.assertEqual(frac6.__sub__(other1).__str__(), "-2.0/1.0", "__sub__ : test du str normal avec num = 0")
        # 8 zéro num
        self.assertEqual(frac6.__sub__(other3).__str__(), "2.0/1.0",
                         "__sub__ : test du str avec un zéro num + negatif num")
        # 9 zéro num
        self.assertEqual(frac6.__sub__(other4).__str__(), "2.0/1.0",
                         "__sub__ : test du str avec un zéro num + negatif num")

    def test___mul__(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(11, 5)
        frac3 = Fraction(-10, 5)
        frac4 = Fraction(10, -5)
        #frac5 = Fraction(-10, -5)
        frac6 = Fraction(0, 5)

        other = Fraction()
        other1 = Fraction(10, 5)
        other2 = Fraction(11, 5)
        other3 = Fraction(-10, 5)
        other4 = Fraction(10, -5)
        other5 = Fraction(-10, -5)
        #other6 = Fraction(0, 5)

        # 1 default
        self.assertEqual(frac.__mul__(other).__str__(), "0.0/1.0", "__mul__ : test du str par défaut")
        # 2 normal
        self.assertEqual(frac1.__mul__(other2).__str__(), "22.0/5.0", "__mul__ : test du str normal 1")
        # 3 négatif num
        self.assertEqual(frac3.__mul__(other1).__str__(), "-4.0/1.0", "__mul__ : test du str avec un num negatif ")
        # 4 négatif den
        self.assertEqual(frac4.__mul__(other2).__str__(), "-22.0/5.0", "__mul__ : test du str avec un den  négatif")
        # 5 nagatif num and den
        self.assertEqual(frac2.__mul__(other5).__str__(), "22.0/5.0",
                         "__mul__ : test du str avec un nagatif num and den")
        # 6 nagatif num and den
        self.assertEqual(frac3.__mul__(other5).__str__(), "-4.0/1.0",
                         "__mul__ : test du str avec un nagatif num and den")
        # 7 nagatif num and den
        self.assertEqual(frac6.__mul__(other1).__str__(), "0.0/1.0", "__mul__ : test du str normal avec num = 0")
        # 8 zéro num
        self.assertEqual(frac6.__mul__(other3).__str__(), "-0.0/1.0",
                         "__mul__ : test du str avec un zéro num + negatif num")
        # 9 zéro num
        self.assertEqual(frac6.__mul__(other4).__str__(), "-0.0/1.0",
                         "__mul__ : test du str avec un zéro num + negatif num")

    def test___truediv__(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(11, 5)
        frac3 = Fraction(-10, 5)
        frac4 = Fraction(10, -5)
        #frac5 = Fraction(-10, -5)
        frac6 = Fraction(0, 5)

        other = Fraction()
        other1 = Fraction(10, 5)
        other2 = Fraction(11, 5)
        other3 = Fraction(-10, 5)
        #other4 = Fraction(10, -5)
        other5 = Fraction(-10, -5)
        other6 = Fraction(0, 5)

        # 1 default
        self.assertRaises(ZeroDivisionError, frac.__truediv__, other)
        # 2 normal
        self.assertEqual(frac1.__truediv__(other2).__str__(), "10.0/11.0", "__truediv__ : test du str normal 1")
        # 3 négatif num
        self.assertEqual(frac3.__truediv__(other1).__str__(), "-1.0/1.0",
                         "__truediv__ : test du str avec un num negatif ")
        # 4 négatif den
        self.assertEqual(frac4.__truediv__(other2).__str__(), "-10.0/11.0",
                         "__truediv__ : test du str avec un den  négatif")
        # 5 nagatif num and den
        self.assertEqual(frac2.__truediv__(other5).__str__(), "11.0/10.0",
                         "__truediv__ : test du str avec un nagatif num and den")
        # 6 nagatif num and den
        self.assertEqual(frac3.__truediv__(other5).__str__(), "-1.0/1.0",
                         "__truediv__ : test du str avec un nagatif num and den")
        # 7 nagatif num and den
        self.assertRaises(ZeroDivisionError, frac6.__truediv__, other1)
        # 8 zéro num
        self.assertRaises(ZeroDivisionError, frac6.__truediv__, other3)
        # 9 zéro num
        self.assertRaises(ZeroDivisionError, frac2.__truediv__, other6)
        # 10 result dénominator not negative
        self.assertEqual(frac1.__truediv__(other3).__str__(), "-1.0/1.0","__truediv__ : test pour ne pas avoir un  dénominator negative")

    def test___pow__(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(11, 5)
        frac3 = Fraction(-10, 5)
        #frac4 = Fraction(10, -5)
        #frac5 = Fraction(-10, -5)
        frac6 = Fraction(0, 5)

        other = Fraction()
        other1 = Fraction(10, 5)
        other2 = Fraction(11, 5)
        other3 = Fraction(-10, 5)
        other4 = Fraction(10, -5)
        other5 = Fraction(-10, -5)
        #other6 = Fraction(0, 5)

        # 1 default
        self.assertEqual(frac.__pow__(other), 1.0, "__pow__ : test du str par défaut")
        # 2 normal
        self.assertEqual(frac1.__pow__(other2), 4.595, "__pow__ : test du str normal 1")
        # 3 négatif num
        self.assertEqual(frac3.__pow__(other1), 4.0, "__pow__ : test du str avec un num negatif ")
        # 4 négatif den
        # 5 nagatif num and den
        self.assertEqual(frac2.__pow__(other5), 4.84, "__pow__ : test du str avec un nagatif num and den")
        # 6 nagatif num and den
        self.assertEqual(frac3.__pow__(other5), 4.0, "__pow__ : test du str avec un nagatif num and den")
        # 7 nagatif num and den
        self.assertEqual(frac6.__pow__(other1), 0, "__pow__ : test du str normal avec num = 0")
        # 8 zéro num
        self.assertRaises(ValueError, frac6.__pow__, other3)
        # 9 zéro num
        self.assertRaises(ValueError, frac6.__pow__, other4)

    def test___eq__(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        #frac2 = Fraction(11, 5)
        frac3 = Fraction(-10, 5)
        frac4 = Fraction(10, -5)
        #frac5 = Fraction(-10, -5)
        frac6 = Fraction(0, 5)
        frac7 = Fraction(1, 2)

        other = Fraction()
        other1 = Fraction(10, 5)
        other2 = Fraction(11, 5)
        other3 = Fraction(-10, 5)
        other4 = Fraction(10, -5)
        other5 = Fraction(-10, -5)
        other6 = Fraction(0, 5)
        other7 = Fraction(2, 4)

        # 1 default
        self.assertEqual(frac.__eq__(other), True, "__add__ : test par défaut")
        # 2 normal
        self.assertEqual(frac1.__eq__(other2), False, "__add__ : test normal")
        # 3 négatif num
        self.assertEqual(frac3.__eq__(other1), False, "__add__ : test avec un num et den negatif ")
        # 4 négatif den
        self.assertEqual(frac4.__eq__(other4), True, "__add__ : test avec un den négatif")
        # 5 nagatif num and den
        self.assertEqual(frac1.__eq__(other5), True, "__add__ : test avec un nagatif num and den")
        # 6 nagatif num and den
        self.assertEqual(frac3.__eq__(other5), False, "__add__ : test avec un nagatif num and den")
        # 7 nagatif num and den
        self.assertEqual(frac6.__eq__(other1), False, "__add__ : test normal avec num = 0")
        # 8 zéro num
        self.assertEqual(frac6.__eq__(other3), False, "__add__ : test avec un zéro num + negatif num")
        # 9 zéro num
        self.assertEqual(frac6.__eq__(other6), True, "__add__ : test avec deux zéro num ")
        # 1/2 = 2/4
        self.assertEqual(frac7.__eq__(other7), True, "__add__ : test avec deux zéro num ")

    def test___float__(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(11, 5)
        frac3 = Fraction(-10, 5)
        frac4 = Fraction(10, -5)
        frac5 = Fraction(-10, -5)
        frac6 = Fraction(0, 5)

        # 1 default
        self.assertEqual(frac.__float__(), 0.0, "__float__ : test du str défaut")
        # 2 normal
        self.assertEqual(frac1.__float__(), 2.0, "__float__ : test du str normal 1")
        # 3 normal
        self.assertEqual(frac2.__float__(), 2.2, "__float__ : test du str normal 2")
        # 4 négatif num
        self.assertEqual(frac3.__float__(), -2.0, "__float__ : test du str avec un num negatif ")
        # 5 négatif den
        self.assertEqual(frac4.__float__(), -2.0, "__float__ : test du str avec un den négatif")
        # 6 nagatif num and den
        self.assertEqual(frac5.__float__(), 2.0, "__float__ : test du str avec un num et den  nagatif ")
        # 7 zéro num
        self.assertEqual(frac6.__float__(), 0.0, "__float__ : test du str avec  zéro en num")

    def test_is_greater(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(11, 5)
        #frac3 = Fraction(-10, 5)
        #frac4 = Fraction(10, -5)
        frac5 = Fraction(-10, -5)
        #frac6 = Fraction(0, 5)

        other = Fraction()
        other1 = Fraction(10, 5)
        other2 = Fraction(11, 5)
        other3 = Fraction(-10, 5)
        #other4 = Fraction(10, -5)
        #other5 = Fraction(-10, -5)
        #other6 = Fraction(0, 5)

        # 1 default
        self.assertEqual(frac.is_greater(other), False, "is_greater : avec tout par  est  par défaut")
        # 2 normal
        self.assertEqual(frac1.is_greater(other2), False, "is_greater : où tout est normal")
        # 3 self = other
        self.assertEqual(frac1.is_greater(other1), False, "is_greater : avec self = other")
        # 4 self > other
        self.assertEqual(frac2.is_greater(other1), True, "is_greater : avec self > other")
        # 5 self < other
        self.assertEqual(frac1.is_greater(other2), False, "is_greater : avec self < other")
        # 6 negatif
        self.assertEqual(frac5.is_greater(other3), True, "is_greater : avec des negatif")

    def test_is_smaller(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(11, 5)
        frac3 = Fraction(-10, 5)
        #frac4 = Fraction(10, -5)
        #frac5 = Fraction(-10, -5)
        #frac6 = Fraction(0, 5)

        other = Fraction()
        other1 = Fraction(10, 5)
        other2 = Fraction(11, 5)
        #other3 = Fraction(-10, 5)
        #other4 = Fraction(10, -5)
        other5 = Fraction(-10, -5)
        #other6 = Fraction(0, 5)

        # 1 default
        self.assertEqual(frac.is_smaller(other), False, "is_smaller : avec tout par  est  par défaut")
        # 2 normal
        self.assertEqual(frac1.is_smaller(other2), True, "is_smaller : où tout est normal")
        # 3 self = other
        self.assertEqual(frac1.is_smaller(other1), False, "is_smaller : avec self = other")
        # 4 self > other
        self.assertEqual(frac2.is_smaller(other1), False, "is_smaller : avec self > other")
        # 5 self < other
        self.assertEqual(frac1.is_smaller(other2), True, "is_smaller : avec self < other")
        # 6 negatif
        self.assertEqual(frac3.is_smaller(other5), True, "is_smaller : avec des negatif")

    def test___rest__(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(11, 5)
        frac3 = Fraction(-10, 5)
        frac4 = Fraction(10, -5)
        #frac5 = Fraction(-10, -5)
        frac6 = Fraction(0, 5)

        other = Fraction()
        other1 = Fraction(10, 5)
        other2 = Fraction(11, 5)
        other3 = Fraction(-10, 5)
        #other4 = Fraction(10, -5)
        other5 = Fraction(-10, -5)
        other6 = Fraction(0, 5)

        # 1 default
        self.assertRaises(ZeroDivisionError, frac.__rest__, other)
        # 2 normal
        self.assertEqual(frac1.__rest__(other2).__str__(), "2.0", "__rest__ : test du str normal 1")
        # 3 négatif num
        self.assertEqual(frac3.__rest__(other1).__str__(), "0.0", "__rest__ : test du str avec un num negatif ")
        # 4 négatif den
        self.assertEqual(frac4.__rest__(other2).__str__(), "0.2", "__rest__ : test du str avec un den  négatif")
        # 5 nagatif num and den
        self.assertEqual(frac2.__rest__(other5).__str__(), "0.2", "__rest__ : test du str avec un nagatif num and den")
        # 6 nagatif num and den
        self.assertEqual(frac3.__rest__(other5).__str__(), "0.0", "__rest__ : test du str avec un nagatif num and den")
        # 7 nagatif num and den
        self.assertEqual(frac6.__rest__(other1).__str__(), "0.0", "__rest__ : test du str avec un nagatif num and den")
        # 8 zéro num
        self.assertEqual(frac6.__rest__(other3).__str__(), "-0.0", "__rest__ : test du str avec un nagatif num and den")
        # 9 zéro num
        self.assertRaises(ZeroDivisionError, frac2.__rest__, other6)

    def test___reverse__(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(-10, 5)
        frac3 = Fraction(10, -5)
        frac4 = Fraction(-10, -5)
        frac5 = Fraction(0, 5)
        frac6 = Fraction(11, 5)

        # 1 default
        self.assertEqual(frac.__reverse__().__str__(), "0.0/1.0", "__reverse__ : test par défaut")
        # 2.1 normal
        self.assertEqual(frac1.__reverse__().__str__(), "-2.0/1.0", "__reverse__ : test  normal 1")
        # 2.2 normal 1
        self.assertEqual(frac6.__reverse__().__str__(), "-11.0/5.0", "__reverse__ : test normal 2")
        # 3 négatif num
        self.assertEqual(frac2.__reverse__().__str__(), "2.0/1.0", "__reverse__ : test avec un num  négatif")
        # 4 négatif den
        self.assertEqual(frac3.__reverse__().__str__(), "2.0/1.0", "__reverse__ : test avec un den  négatif")
        # 5 nagatif num and den
        self.assertEqual(frac4.__reverse__().__str__(), "-2.0/1.0",
                         "__reverse__ : test normal avec un den et num  négatif")
        # 6 zéro num
        self.assertEqual(frac5.__reverse__().__str__(), "0.0/1.0", "__reverse__ : test avec un num égal à 0")

    def test___neg__(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(-10, 5)
        frac3 = Fraction(10, -5)
        frac4 = Fraction(-10, -5)
        frac5 = Fraction(0, 5)
        frac6 = Fraction(11, 5)

        # 1 default
        self.assertEqual(frac.__neg__().__str__(), "0.0/1.0", "__neg__ : test par défaut")
        # 2.1 normal
        self.assertEqual(frac1.__neg__().__str__(), "-2.0/1.0", "__neg__ : test  normal 1")
        # 2.2 normal 1
        self.assertEqual(frac6.__neg__().__str__(), "-11.0/5.0", "__neg__ : test normal 2")
        # 3 négatif num
        self.assertEqual(frac2.__neg__().__str__(), "-2.0/1.0", "__neg__ : test avec un num  négatif")
        # 4 négatif den
        self.assertEqual(frac3.__neg__().__str__(), "-2.0/1.0", "__neg__ : test avec un den  négatif")
        # 5 nagatif num and den
        self.assertEqual(frac4.__neg__().__str__(), "-2.0/1.0", "__neg__ : test normal avec un den et num  négatif")
        # 6 zéro num
        self.assertEqual(frac5.__neg__().__str__(), "0.0/1.0", "__neg__ : test avec un num égal à 0")

    def test___abs__(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(-10, 5)
        frac3 = Fraction(10, -5)
        frac4 = Fraction(-10, -5)
        frac5 = Fraction(0, 5)
        frac6 = Fraction(11, 5)

        # 1 default
        self.assertEqual(frac.__abs__().__str__(), "0.0/1.0", "__abs__ : test par défaut")
        # 2.1 normal
        self.assertEqual(frac1.__abs__().__str__(), "2.0/1.0", "__abs__ : test  normal 1")
        # 2.2 normal 1
        self.assertEqual(frac6.__abs__().__str__(), "11.0/5.0", "__abs__ : test normal 2")
        # 3 négatif num
        self.assertEqual(frac2.__abs__().__str__(), "2.0/1.0", "__abs__ : test avec un num  négatif")
        # 4 négatif den
        self.assertEqual(frac3.__abs__().__str__(), "2.0/1.0", "__abs__ : test avec un den  négatif")
        # 5 nagatif num and den
        self.assertEqual(frac4.__abs__().__str__(), "2.0/1.0", "__abs__ : test normal avec un den et num  négatif")
        # 6 zéro num
        self.assertEqual(frac5.__abs__().__str__(), "0.0/1.0", "__abs__ : test avec un num égal à 0")

    def test_is_zero(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(11, 5)
        frac3 = Fraction(0, 5)
        frac4 = Fraction(0, -5)
        frac5 = Fraction(4, 5)
        frac6 = Fraction(5, 5)

        # 1 default
        self.assertEqual(frac.is_zero(), True, "is_zero : où self à ses parametres par défaut")
        # 2 normal
        self.assertEqual(frac2.is_zero(), False, "is_zero : où tout est normal")
        # 3 integer
        self.assertEqual(frac1.is_zero(), False, "is_zero :ou self est un integer")
        # 4 zero
        self.assertEqual(frac3.is_zero(), True, "is_zero : ou self est égal à 0")
        # 5 negative zero
        self.assertEqual(frac4.is_zero(), True, "is_zero : ou self est égal à un zéro negatif")
        # 6 proper
        self.assertEqual(frac5.is_zero(), False, "is_zero : ou self est proper")
        # 7 unit
        self.assertEqual(frac6.is_zero(), False, "is_zero : ou self est un unit")

    def test_is_integer(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(11, 5)
        frac3 = Fraction(0, 5)
        frac4 = Fraction(0, -5)
        frac5 = Fraction(4, 5)
        frac6 = Fraction(5, 5)

        # 1 default
        self.assertEqual(frac.is_integer(), True, "is_integer : où self à ses parametres par défaut")
        # 2 normal
        self.assertEqual(frac2.is_integer(), False, "is_integer : où tout est normal")
        # 3 integer
        self.assertEqual(frac1.is_integer(), True, "is_integer :ou self est un integer")
        # 4 zero
        self.assertEqual(frac3.is_integer(), True, "is_integer : ou self est égal à 0")
        # 5 negative zero
        self.assertEqual(frac4.is_integer(), True, "is_integer : ou self est égal à un zéro negatif")
        # 6 proper
        self.assertEqual(frac5.is_integer(), False, "is_integer : ou self est proper")
        # 7 unit
        self.assertEqual(frac6.is_integer(), True, "is_integer : ou self est un unit")

    def test_is_proper(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(11, 5)
        frac3 = Fraction(0, 5)
        frac4 = Fraction(0, -5)
        frac5 = Fraction(4, 5)
        frac6 = Fraction(5, 5)

        # 1 default
        self.assertEqual(frac.is_proper(), True, "is_proper : où self à ses parametres par défaut")
        # 2 normal
        self.assertEqual(frac2.is_proper(), False, "is_proper : où tout est normal")
        # 3 integer
        self.assertEqual(frac1.is_proper(), False, "is_proper :ou self est un integer")
        # 4 zero
        self.assertEqual(frac3.is_proper(), True, "is_proper : ou self est égal à 0")
        # 5 negative zero
        self.assertEqual(frac4.is_proper(), True, "is_proper : ou self est égal à un zéro negatif")
        # 6 proper
        self.assertEqual(frac5.is_proper(), True, "is_proper : ou self est proper")
        # 7 unit
        self.assertEqual(frac6.is_proper(), False, "is_proper : ou self est un unit")

    def test_is_unit(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        frac2 = Fraction(11, 5)
        frac3 = Fraction(0, 5)
        frac4 = Fraction(0, -5)
        frac5 = Fraction(4, 5)
        frac6 = Fraction(5, 5)

        # 1 default
        self.assertEqual(frac.is_unit(), False, "is_unit : où self à ses parametres par défaut")
        # 2 normal
        self.assertEqual(frac2.is_unit(), False, "is_unit : où tout est normal")
        # 3 integer
        self.assertEqual(frac1.is_unit(), False, "is_unit :ou self est un integer")
        # 4 zero
        self.assertEqual(frac3.is_unit(), False, "is_unit : ou self est égal à 0")
        # 5 negative zero
        self.assertEqual(frac4.is_unit(), False, "is_unit : ou self est égal à un zéro negatif")
        # 6 proper
        self.assertEqual(frac5.is_unit(), False, "is_unit : ou self est proper")
        # 7 unit
        self.assertEqual(frac6.is_unit(), True, "is_unit : ou self est un unit")

    def test_is_adjacent_to(self):
        frac = Fraction()
        frac1 = Fraction(10, 5)
        #frac2 = Fraction(-10, 5)
        frac3 = Fraction(5, 5)
        frac4 = Fraction(-10, -5)
        frac5 = Fraction(-5, 5)
        frac6 = Fraction(11, 5)

        other = Fraction()
        other1 = Fraction(10, 5)
        other2 = Fraction(-10, 5)
        #other3 = Fraction(10, -5)
        #other4 = Fraction(-10, -5)
        other5 = Fraction(0, 5)
        other6 = Fraction(5, 5)

        # 1 default
        self.assertEqual(frac.is_adjacent_to(other), False, "is_adjacent_to : test par défaut")
        # 2 normal
        self.assertEqual(frac6.is_adjacent_to(other1), True, "is_adjacent_to : test  normal 1")
        # 3 equal
        self.assertEqual(frac1.is_adjacent_to(other1), False, "is_adjacent_to : ou other et self sont identique ")
        # 4 adjacent +1
        self.assertEqual(frac3.is_adjacent_to(other1), True, "is_adjacent_to : ou il sont adjacent +1")
        # 5 adjacent -1
        self.assertEqual(frac3.is_adjacent_to(other5), True, "is_adjacent_to : ou il sont adjacent -1")
        # 6 adjacent -1 negatif
        self.assertEqual(frac5.is_adjacent_to(other2), True, "is_adjacent_to : ou il sont adjacent -1 en négatif")
        # 7 adjacent -1 negatif et zero
        self.assertEqual(frac5.is_adjacent_to(other5), True,"is_adjacent_to : ou il sont adjacent -1 en négatif et zéro")
        # 8 adjacent  full negatif and positif
        self.assertEqual(frac4.is_adjacent_to(other6), True,"is_adjacent_to : ou il sont adjacent full négatif et posifir")
