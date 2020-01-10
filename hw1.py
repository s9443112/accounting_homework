from sympy import Symbol, symbols, sin, cos, tan
from sympy import integrate, diff, solve
from sympy.functions import Abs


def questionA():
    x = Symbol('x')
    f = x*(x**3-1)
    print("questionA")
    print(integrate(f, x))
    print("\n")


def questionB():
    # Not finished.
    x = Symbol('x')
    f = sin**3(x*cos(x))
    print("questionB")
    print(integrate(f,x))
    print("\n")


def questionC():
    x = Symbol('x')
    f = x*((2*x+5)**8)
    print("questionC")
    print(integrate(f, x))
    print("\n")


def questionD():
    x = Symbol('x')
    a, b = symbols('a,b')
    f = (a + b*x**2)/(3*a*x+b*x**3)**1/2
    print("questionD")
    print(integrate(f, x))
    print("\n")


def questionE():
    t = Symbol('t')
    pi = Symbol("π")
    f = cos(pi*t/2)
    print("questionE")
    print(integrate(f, (t, 1, 0)))
    print("\n")


def questionF():
    pi = Symbol("π")
    x = Symbol('x')
    f = x**3+x**4*tan(x)
    print("questionF")
    print(integrate(f, (x, pi/4, -pi/4)))
    print("\n")


def questionG():
    x = Symbol('x')
    f = Abs(2*x-1)
    print("questionG")
    print(integrate(f, (x, 2, 0)))
    print("\n")


def questionH():
    x = Symbol('x')
    y = (x**2+1)/(x**3-1)
    print("questionH")
    print(diff(y, x))
    print("\n")


def questionI():
    s = Symbol('s')
    y = (s-s**1/2)/s**2
    print("questionI")
    print(diff(y, s))
    print("\n")



def questionJ():
    x = Symbol('x')
    f = (2*x**5 + x**4 - 6*x) / x**3
    print("questionJ")
    print(diff(f, x))
    print("\n")

def questionK():
    x = Symbol('x')
    c = Symbol('c')
    f = x/x+c/x
    print("questionK")
    print(diff(f,x))
    print("\n")

def questionL():
    y = Symbol('y')
    A, B = symbols('A,B')
    G = B/A*y**3+B
    print("questionL")
    print(diff(G,y))
    print(diff(G,B))
    print("\n")



def questionM():
    x, y = symbols('x,y')
    fun1 = 4*x + 2*y
    fun2 = 3*x+5*y + 7
    print("questionM")
    print(solve([fun1, fun2], [x, y]))
    print("\n")


def questionN():
    x, y = symbols('x,y')
    fun1 = 4*x-3*y-2
    fun2 = -7*x+4*y-4
    print("questionN")
    print(solve([fun1, fun2], [x, y]))
    print("\n")


def questionO():
    x, y, z = symbols('x,y,z')
    fun1 = 1/x + 1/y + 1/z
    fun2 = 4/x + 3/y + 2/z - 5
    fun3 = 3/x + 2/y + 4/z + 4

    print("questionO")
    print(solve([fun1, fun2, fun3], [x, y, z]))
    print("\n")


questionA()
# questionB()
questionC()
questionD()
questionE()
questionF()
questionG()
questionH()
questionI()
questionJ()
questionK()
questionL()
questionM()
questionN()
questionO()
