
class kasr:
    def __init__(self, s1,m1,s2,m2):
        self.k1 = s1/m1
        self.k2 = s2/m2
    
    def Sum(self):
        s=self.k1+self.k2
        print("jam : ", s)
    def Sub(self):
        t=self.k1 - self.k2
        print("tafriq : ",t)
    def Mult(self):
        m=self.k1*self.k2
        print("zarb : ",m)
    def Div(self):
        d=self.k1 / self.k2
        print("taqsim : ",d)
s1=int(input("sorat kasr aval : "))
m1=int(input("makhraj kasr aval : "))
s2=int(input("sorat kasr dovom : "))
m2=int(input("makhraj kasr dovom : "))
x = kasr(s1,m1,s2,m2)
x.Sum()
x.Sub()
x.Mult()
x.Div()