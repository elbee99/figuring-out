
#Finds the greatest common divisor of a pair of numbers
def gcd(m,n):
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n

#Fraction class
class Fraction:
    def __init__(self,top,bottom):
        if type(top) != int or type(bottom) != int:
            raise TypeError('top/bottom must be integers')
        common = gcd(top,bottom)
        self.num = top
        self.den = bottom
        
    def __str__(self):
        return str(self.num)+'/'+str(self.den)
    
    def show(self):
        print(self.num,'/',self.den,sep='')
        
    def __add__(self,other):
        new_num = self.num*other.den + self.den*other.num
        new_den = self.den*other.den
        return Fraction(new_num,new_den)
    
    def __eq__(self,other):
        first_num = self.num*other.den
        second_num = self.den*other.num
        return first_num==second_num
    
    def __sub__(self,other):
        new_num = self.num*other.den + self.den*other.num
        new_den = self.den*other.den
        return Fraction(new_num,new_den)
    
    def __mul__(self,other):
        new_num = self.num*other.num
        new_den = self.den*other.den
        return Fraction(new_num,new_den)
    
    def __truediv__(self,other):
        new_num = self.num*other.den
        new_den = self.den*other.num
        return Fraction(new_num,new_den)
    
    def __lt__(self,other):
        return self.num*other.den < self.den*other.num
    
    def __le__(self,other):
        return self.num*other.den <= self.den*other.num
    
    def __gt__(self,other):
        return self.num*other.den > self.den*other.num
    
    def __ge__(self,other):
        return self.num*other.den >= self.den*other.num
    
    def get_num(self):
        return self.num
    
    
    def get_den(self):
        return self.den
    
if __name__ == '__main__':
    a = Fraction(5,7)
    b = Fraction(2,9)

    a.show()

    prod = a*b
    div = a/b
    add = a+b
    sub = a-b
    lt = a<b
    gt = a>b

    print('a x b =',prod)
    print('a / b =',div)
    print('a + b =',add)
    print('a - b =',sub)
    print('a < b:',lt)
    print(' a > b:',gt)