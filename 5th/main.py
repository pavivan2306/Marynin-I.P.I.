from datetime import datetime
from random import randint
import math
############################################# №1,а: тест на простоту

def Euclid(a,b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def extended_euclid(a, b):
    if (b == 0):
        return a, 1, 0
    d, x, y = extended_euclid(b, a % b)
    return d, y, x - (a // b) * y

def Jacobi(a,n,J):
    i = 0
    while a % 2 == 0:
        a = a / 2
        i += 1
    if i % 2 == 1:
        J = J * (-1)**((n**2-1)/8)
    if a != 1:
        a1 = n % a
        n1 = a
    else:
        a1 = a
        n1 = n
    J = J * (-1) ** (((a - 1) * (n - 1)) / 4)
    if a1 == 0:
        J = 0
    if a1 == 2:
        J = J*((-1)**((n1**2-1)/8))
    if a1 >= 3:
        J = Jacobi(a1, n1, J)
    return J

def Solovey(p, k):
    i = 0
    digit = 0
    if p >= 0 and p <= 3:
        return 1
    while i < k:
        x = randint(1, p-1)
        # print(p - 1, '-------------------------------------------------------------------------   p')
        if p == 1:
            break
        #x = random.randrange(1, p - 1)
        q = (p-1)/2
        if Euclid(x, p) > 1:
           break
        if Euclid(x, p) == 1 and Jacobi(x, p, 1) + p != pow(int(x), int(q), int(p)) and Jacobi(x, p, 1) != pow(int(x), int(q), int(p)):
            break
        else:
            if i == k - 1:
                digit = 1   # => p is a prime digit
        i += 1
    return digit


############################################# №1,б: метод пробних ділень

def TrialDivs(n, B):
    n = str(n)                                      ######створення списку, елементами якого є значення розрядів числа n
    i = 0
    a = []
    while i < len(n):
        a.append(int(n[i]))
        i += 1
    m = [2, 3, 5]                                   ######створення списку, елементами якого є прості числа до кореня з n
    i = m[len(m) - 1] + 1
    while i < 48:
        if Solovey(i, 3) == 1:
            m.append(i)
        i += 1
    dividers = []
    i = 0
    while i < len(m):
        r = [1]
        j = 0
        summ = 0
        while j < len(a) - 1:
            r.append((r[j]*B) % m[i])
            j += 1
        j = 0
        while j < len(a):
            summ += a[len(a)-j-1] * r[j]
            j += 1
        if summ % m[i] == 0:
            dividers.append(m[i])
        i += 1
    return dividers



############################################# №1,в: ρ-метод Полларда

def func(x, n):
    x = (x**2 + 1) % n
    return x
def Pollard(n, x_0, y_0):
    d = 1
    x_i = func(x_0, n)
    y_i = func(func(y_0, n), n)
    while x_i != y_i:
        d = math.gcd(x_i - y_i, n)
        if d != 1:
            break
        x_i = func(x_i, n)
        y_i = func(func(y_i, n), n)
    return d

dividers = []
def Second_Task(n, x_0, y_0):

    while Solovey(n, 100) == 0:
        x = TrialDivs(n, 10)
        if len(x) == 0:
            break
        else:
            while len(x) != 0:
                dividers.append(x[0])
                n = int(n/x[0])
                x.pop(0)
        if Solovey(n, 100) == 1:
            dividers.append(n)
            return dividers

    while Solovey(n, 100) == 0:
        y = Pollard(n, x_0, y_0)
        if y == 1:
            break
        else:
            dividers.append(y)
            n = int(n/y)
        if Solovey(n, 10) == 1:
            dividers.append(n)
            return dividers
    if len(dividers) == 1:
        print('Я не можу знайти канонічний розклад числа')




def SiPoGe(alfa, beta, p):
    if extended_euclid(alfa, p)[1] < 0:
        revalfa = p + extended_euclid(alfa, p)[1]
    else:
        revalfa = extended_euclid(alfa, p)[1]
    print(revalfa, '-----------------------------------------------revalfa')
    dividers = Second_Task(p - 1, 300, 150)
    print(dividers, '- dividers before')
    degrees = []
    i = 0
    while i < len(dividers):
        j = 0
        if dividers[i] == 1:
            dividers.pop(i)
            i -= 1
        else:
            degrees.append(1)
            while j < len(dividers):
                if dividers[i] == dividers[j] and i != j:
                    degrees[i] += 1
                    dividers.pop(j)
                    j -= 1
                j += 1
        i += 1
    print(dividers, '- dividers after with degrees:', degrees)
    r = []
    elofr = []
    i = 0
    while i < len(dividers):
        j = 0
        while j < dividers[i]:
            r_var = pow(alfa, int((p-1)*j/dividers[i]), p)
            elofr.append(r_var)
            j += 1
        r.append(elofr)
        elofr = []
        i += 1
    print(r, '- r with len:', len(r), '\n')
    i = 0
    while i < len(r):
        ghj = r[i]
        print(len(ghj), 'len(ghj) = len(r[i]), i =', i)
        i += 1

    x_list = []
    i = 0
    while i < len(dividers):
        elforx_list = []
        j = 0
        r_curr = r[i]
        while j < degrees[i]:
            k = 0
            deg = 0
            while k < j:
                deg += elforx_list[k - 1] * dividers[i]**k
                k += 1
            var = pow(int(beta*(revalfa**deg)), int((p-1)/dividers[i]**(j+1)), p)
            k = 0
            while k < len(r_curr):
                if var == r_curr[k]:
                    elforx_list.append(k)
                k += 1
            j += 1
        x = 0
        j = 0
        while j < len(elforx_list):
            x = (x + (elforx_list[j] * (dividers[i] ** j))) % dividers[i] **degrees[i]
            j += 1
        x_list.append(x)
        i += 1
    print(x_list, '- x_list')

    i = 0
    x = 0
    while i < len(dividers):
        j = 0
        mult = 1
        while j < len(dividers):
            if j == i:
                pass
            else:
                mult *= dividers[j] ** degrees[j]
            j += 1
        print(mult, ' -  mult')
        if extended_euclid(mult, dividers[i] ** degrees[i])[1] < 0:
            revmult = dividers[i] ** degrees[i] + extended_euclid(mult, dividers[i] ** degrees[i])[1]
        else:
            revmult = extended_euclid(mult, dividers[i] ** degrees[i])[1]
        print(revmult, '- revmult\t', dividers[i] ** degrees[i], '- dividers[i] ** degrees[i]')
        print(extended_euclid(mult, dividers[i] ** degrees[i])[1], 'extended_euclid(mult, dividers[i] ** degrees[i])[1]')
        x += (x_list[i] * mult * revmult) % (p - 1)
        x = x % (p - 1)
        i += 1
    return x
start_time = datetime.now()
print(SiPoGe(76384303, 152159776, 234406987), ' -----  шуканий степінь')
print(datetime.now() - start_time)
