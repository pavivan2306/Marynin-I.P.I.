from random import randint
import math
import pandas as pd
from datetime import datetime
############################################# №1,а: тест на простоту

def Euclid(a,b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

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
    while i < k:
        x = randint(1, p-1)
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


############################################# №1,г: Метод Брiлхарта-Моррiсона

def Brill_Morr(n):
    a = 1/(2**(1/2))                                                    ##############  факторна база
    L = math.exp((math.log2(n)*math.log2(math.log2(n)))**(1/2))
    B = [-1]
    counter = 2
    while counter < L**a:
        if Solovey(counter, 10) + Jacobi(counter, n, 1) == 2:
            B.append(counter)
        counter += 1

    a = []                                                              ##############  ланцюговий дріб
    n_root = n ** (1/2)
    v_0 = 1
    alfa_0 = n_root
    a.append(int(alfa_0))
    u_0 = a[0]
    i = 1
    while i <= len(B):
        v_i = (n - u_0 ** 2) / v_0
        alfa_i = (n**(1/2) + u_0) / v_i
        a.append(int(alfa_i))
        u_i = a[i] * v_i - u_0
        u_0 = u_i
        v_0 = v_i
        i += 1

    b = []                                                              ##############  B-гладкі числа
    b_1 = 1
    b_2 = 0
    i = 0
    while i <= len(B):
        b.append((a[i]*b_1 + b_2) % n)
        b_2 = b_1
        b_1 = b[i]
        i += 1

    forfuturex = []
    i = 0
    while i < len(b):
        forfuturex.append(b[i])
        i += 1

    i = 0
    while i <= len(B):
        b[i] = pow(b[i], 2, n)
        if b[i] > int(n/2):
            b[i] = b[i] - n
        i += 1
#######################################################################################################################
    B_last = []
    b_last = []
    df = pd.DataFrame()
    i = 1
    while i <= len(B):
        df.insert(i - 1, B[i-1], 0)
        i += 1
    i = 0
    k = 0
    while i < len(b):
        vect_rozk = pd.DataFrame()
        l = 0
        while l < len(B):
            vect_rozk.insert(l, B[l], 0)
            l += 1
        l = 0
        while l < len(B):
            vect_rozk.at[b[i], B[l]] = 0
            l += 1
        j = 1
        x = b[i]
        y = 0
        if x < 0:
            x = x * (-1)
            vect_rozk.at[b[i], B[0]] = 1
        else:
            vect_rozk.at[b[i], B[0]] = 0

        while j < len(B) and x != 1:
            if x % B[j] == 0:
                x = x / B[j]
                vect_rozk.loc[b[i]].at[B[j]] += 1
                j = 0
            if j == len(B) - 1:
                y = 1
                break
            j += 1
        i += 1
        if y == 0:
            df = df.append(vect_rozk, ignore_index = False)
            b_last.append(b[i-1])
        else:
            forfuturex.pop(k)
            k -= 1
        k += 1
    df.to_excel("NTA lab1.xlsx")
    i = 0
    k = 0
    while i < len(B):
        j = 0
        x = 0
        while j < len(b_last):
            x += df.iat[j, i]
            j += 1
        if x == 0:
            if k == len(B) - 1:
                df.drop(df.columns[[i]], axis=1, inplace=True)
                break
            else:
                df.drop(df.columns[[i]], axis=1, inplace=True)
            i = i - 1
        else:
            B_last.append(B[k])
        i += 1
        k += 1
    #df.to_excel("NTA lab1 1.xlsx")                                          # остаточний датафрейм зі степенями розкладу
                                                                            # гладких чисел (у рядках) по мінімальній
                                                                            # факторній базі (елементи-назви стовпчиків)
    i = 0
    k = 0
    while i < len(B_last):
        j = 0
        cheker = 0
        while j < len(b_last):
            if df.iat[j, i] % 2 == 1:
                cheker += 1
            j += 1
        if cheker == 1:
            if k == len(B_last) - 1:
                df.drop(df.columns[[i]], axis=1, inplace=True)
                B_last.pop(i)
                break
            else:
                df.drop(df.columns[[i]], axis=1, inplace=True)
                B_last.pop(i)
            i -= 1
        k += 1
        i += 1

    df.to_excel("NTA lab1 1.xlsx")
    vectors = []
    counter_list = []

    def Search(m, count_list):
        a = 1
        vectors1 = []
        let = 0
        while let < len(m):
            vectors1.append(m[let])
            let += 1
        i = 0
        X = 1
        while i < len(count_list):
            j = count_list[i]
            X = (X * forfuturex[j]) % n
            i += 1
        Y = 1
        i = 0
        while i < len(vectors1):
            j = 0
            while j < len(B_last):
                if B_last[j] == -1:
                    if vectors1[i] < 0:
                        vectors1[i] = - vectors1[i]
                        j += 1

                if vectors1[i] % B_last[j] == 0:
                    vectors1[i] = vectors1[i] / B_last[j]
                    Y = (Y * B_last[j]) % n
                    j -= 1
                j += 1
            i += 1
        Y = int(math.sqrt(Y))
        if X != Y and X != n - Y:
            a = math.gcd(int(X+Y) % n, n)
        return a


    a_b = []
    def Recurc_Func(x, y, x_prev):
        a = 0           # рядок
        b = 0           # стовпчик
        gsd = 1
        vectors.append(b_last[x])
        counter_list.append(x)
        while b < len(B_last):
            if df.iat[x, b] % 2 == 1:
                if b == y:
                    pass
                else:
                    checker_y = 0
                    while a < len(b_last):
                        if df.iat[a, b] % 2 == 1:
                            let = 0
                            while let < len(a_b):
                                if [a, b] == a_b[let]:
                                    let = 'a'
                                    break
                                let += 1
                            if a != x and a != x_prev and let != 'a':
                                checker_y = 1
                                gcd = Search(vectors, counter_list)
                                if gcd != 1:
                                    return gcd
                                Recurc_Func(a, b, x)
                            else:
                                pass
                        if checker_y == 0 and a == len(b_last) - 1:
                            gcd = Search(vectors, counter_list)
                            if gcd != 1:
                                return gcd
                            vectors.pop(len(vectors) - 1)
                            counter_list.pop(len(vectors))
                            return 1
                        a += 1
            if b == len(B_last) - 1:
                gsd = Search(vectors, counter_list)
                if gsd != 1:
                    break
                vectors.pop(len(vectors) - 1)
                counter_list.pop(len(vectors))
            b += 1
        if len(vectors) == 0:
            return 1
        return gsd

    result = 1
    i = 0
    while i < len(b_last):                                                          #по гладким числам
        result = Recurc_Func(i, -1, -1)
        if result != 1:
            break
        i += 1
    return result

############################################# №2
dividers = []
def Second_Task(n, x_0, y_0):

    while Solovey(n, 1000) == 0:
        x = TrialDivs(n, 10)
        if len(x) == 0:
            break
        else:
            while len(x) != 0:
                dividers.append(x[0])
                print('Дільник', x[0], 'отримано методом пробних ділень.')
                n = int(n/x[0])
                x.pop(0)
        if Solovey(n, 1000) == 1:
            dividers.append(n)
            print('Дільник', n, 'отримано тому що це просте число.')
            return dividers

    while Solovey(n, 1000) == 0:
        y = Pollard(n, x_0, y_0)
        if y == 1:
            break
        else:
            dividers.append(y)
            print('Дільник', y, 'отримано ρ-методом Полларда.')
            n = int(n/y)
        if Solovey(n, 1000) == 1:
            dividers.append(n)
            print('Дільник', n, 'отримано тому що це просте число.')
            return dividers

    while Solovey(n, 1000) == 0:
        z = Brill_Morr(n)
        if z == 1:
            break
        else:
            dividers.append(z)
            print('Дільник', z, 'отримано методом Брiлхарта-Моррiсона.')
            n = int(n/z)
        if Solovey(n, 1000) == 1:
            dividers.append(n)
            print('Дільник', n, 'отримано тому що це просте число.')
            return dividers

    if len(dividers) == 1:
        print('Я не можу знайти канонічний розклад числа')





# Візуалізація:)
print('Вітаю! Для початку роботи введіть `1`')
continuer = input()
while continuer != 0:
    print('Виберіть задачу, яку маєте бажання виконати:\n'
          '1) факторизація ρ-методу Полларда - введіть 1\n'
          '2) факторизація Брiлхарта-Моррiсона - введіть 2\n'
          '3) канонічний розклад числа - введіть 3\n'
          '4) перевірити число на простоту за Соловеєм-Штрассеном - введіть 4\n')

    continuer = int(input())

    if continuer == 1:
        print('Ви обрали факторизацію ρ-методом Полларда\n'
              'Для роботи алгоритму необхідно ввести значення n, x_0, y_0 почергово!,\n'
              'де n - число, що потрібно факторизувати, x_0 та y_0 - координати початкової точки кривої.\n'
              'У якості x_0 та y_0 рекомендую обрирати 150;0 або 300;150.\n')
        n = int(input())
        x_0 = int(input())
        y_0 = int(input())
        print('Виконується факторизація числа', n , 'із координати початкової точки кривої x_0 =', x_0, 'та y_0 =', y_0)
        start_time = datetime.now()
        x = Pollard(n, x_0, y_0)
        diff = datetime.now() - start_time
        print('Дільники числа n =', n, 'це:', x, 'та', int(n/x))
        print('Час роботи алгоритму(год,хв,сек.):', diff)

    if continuer == 2:
        print('Ви обрали факторизацію Брiлхарта-Моррiсона\n'
              'Для роботи алгоритму необхідно ввести значення n - числa, що потрібно факторизувати.\n'
              'Попереджаю, що даний алгоритм може працювати як 40 секунд, так і до години часу.\n'
              'Також можлива велика кількість попереджень.\n')
        n = int(input())
        print('Виконується факторизація числа', n , '...')
        start_time = datetime.now()
        x = Brill_Morr(n)
        diff = datetime.now() - start_time
        print('Дільники числа n =', n, 'це:', x, 'та', int(n/x))
        print('Час роботи алгоритму(год,хв,сек.):', diff)

    if continuer == 3:
        print('Ви обрали канонічний розклад числа\n'
              'Для роботи алгоритму необхідно ввести значення n, x_0, y_0 почергово!,\n'
              'де n - число, що потрібно розкласти, x_0 та y_0 - координати початкової точки кривої у методі Поларда,\n'
              'який використовується в алгоритмі.'
              'У якості x_0 та y_0 рекомендую обрирати 150;0 або 300;150.\n')
        n = int(input())
        x_0 = int(input())
        y_0 = int(input())
        print('Виконується розклад числа', n)
        start_time = datetime.now()
        x = Second_Task(n, x_0, y_0)
        diff = datetime.now() - start_time
        print('Канонічний розклад числа n:', x)
        print('Час роботи алгоритму(год,хв,сек.):', diff)

    if continuer == 4:
        print('Ви обрали перевірку числа на простоту за Соловеєм-Штрассеном\n'
              'Для роботи алгоритму необхідно ввести значення p, k почергово!,\n'
              'де p - число, що потрібно перевірити, k - кількість перевірок, що здійснюється алгоритмом.\n')
        p = int(input())
        k = int(input())
        print('Виконується перевірка на простоту числа', p)
        start_time = datetime.now()
        x = Solovey(p, k)
        diff = datetime.now() - start_time
        if x == 1:
            print('Число', p, 'просте.')
        else:
            print('Число', p, 'складене.')
        print('Час роботи алгоритму(год,хв,сек.):', diff)

    print('Ви бажаєте продовжити роботу алгоритму? Якщо так, то введіть 1, якщо ні, то 0')
    continuer = int(input())
    print('-----------------------------------------------------------------\n')

