import math
import pandas as pd
import openpyxl
a = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
str(a)
l = len(a)
alphabet = []
k = 0
while(k!=l):
    alphabet.append(a[k])
    k = k + 1
print(len(alphabet))
def extended_euclid(a, b):
    if (b == 0):
        return a, 1, 0
    d, x, y = extended_euclid(b, a % b)
    return d, y, x - (a // b) * y

def linear_comparison(X, XX, Y, YY, m):
    m = m ** 2
    # print(X, ' --  X')
    # print(XX, ' --  XX')
    x = X - XX
    y = Y - YY
    list1 = []
    list2 = []
    #print(x, ' --  x', m, ' --  m')
    d = math.gcd(x, m)
    if d == 1:
        a = extended_euclid(x, m)[1] * y
        b = (Y - a * X) % m
        if a < 0 or a > m:
            a = a % m
        if b < 0 or b > m:
            b = b % m
        list1.append(a)
        list2.append(b)
        return list1, list2
    else: #y % d != 0:
        if y / d - int(y / d) != 0:
            return 0
        else:
            #print(d, ' --  d')
            a_1 = int(x / d)
            b_1 = int(y / d)
            m_1 = int(m / d)
            #print(extended_euclid(a_1, m_1)[1], ' --  extended_euclid(a_1, m_1)[1]')
            x_0 = (b_1 * extended_euclid(a_1, m_1)[1]) % m
            list1.append(x_0)
            i = 1
            while i < d:
                list1.append(x_0 + i * m_1)
                i += 1
            list2 = []
            i = 0
            while i < len(list1):
                list2.append((Y - list1[i] * X) % m_1)
                i += 1
            return list1, list2

def frequency_bigrams(text):
    text = open(text, 'r')
    text = text.read()
    text = str(text)
    df = pd.DataFrame(0,
                      columns=['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
                               'с', 'т', 'у', 'ф', 'х', 'ц',
                               'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'],
                      index=['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
                             'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я'])
    i = 0
    while i < len(text) - 1:
        j = 0
        while j < len(alphabet):
            k = 0
            if text[i] == alphabet[j]:
                while k < len(alphabet):
                    if text[i + 1] == alphabet[k]:
                        df.iat[j, k] += 1
                        break
                    k += 1
                break
            j += 1
        i += 2

    df.to_excel("df_07.xlsx")
    # [в, м] = 51; [м, ь] = 44; [й, в] = 31; [р, м] = 30; [в, щ] = 29  --  це для тестового шифротексту
    #
    # [c, т] = ?; [н, о] = ?; [т, о] = ?; [н, а] = ?; [е, н] = ?
#frequency_bigrams('07.txt')

mcb1 = [11, 11]
mcb2 = [19, 11]
mcb3 = [5, 1]
mcb4 = [22, 11]
mcb5 = [11, 5]

# mcb1 = [2, 12]
# mcb2 = [12, 27]
# mcb3 = [9, 2]
# mcb4 = [16, 12]
# mcb5 = [3, 22]

lmcb1 = [17, 18]
lmcb2 = [13, 14]
lmcb3 = [18, 14]
lmcb4 = [13, 0]
lmcb5 = [5, 13]

def lengthsearch2(a):
    a = open(a, 'r')
    a = a.read()
    a = str(a)
    D_r = []
    r = 6
    while r < 32:
        D = 0
        i = 0
        while i < len(a) - r:
            if a[i] == a[i + r]:
                D += 1
            i += 1
        D_r.append(D)
        r += 1
    print(D_r, ' --  D_r')
# lengthsearch2('07.txt')

def task2(a):
    counterlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    while i < len(a):
        j = 0
        while j < len(alphabet):
            if a[i] == alphabet[j]:
                counterlist[j] += 1
                break
            j += 1
        i += 1
    I = 0
    i = 0
    while i < len(counterlist):
        I += counterlist[i] * (counterlist[i] - 1)
        i += 1
    I = I/(len(a) * (len(a) - 1))
    return I

def decrypt(text, l1, l2, l3, l4):
    text = open(text, 'r')
    text = text.read()
    text = str(text)
    X = l1[0] * 31 + l1[1]
    XX = l2[0] * 31 + l2[1]
    Y = l3[0] * 31 + l3[1]
    YY = l4[0] * 31 + l4[1]
    if linear_comparison(X, XX, Y, YY, 31) == 0:
        return 0#'ПОМИЛКА! НЕ МОЖЛИВО РОЗВЯЗАТИ РІВНЯННЯ'
    list_a = linear_comparison(X, XX, Y, YY, 31)[0]
    list_b = linear_comparison(X, XX, Y, YY, 31)[1]
    print('list_a:', list_a)
    print('list_b:', list_b)
    # print(list_a, ' --  list_a')
    # print(list_b, ' --  list_b')
    textlist = []
    i = 0
    while i < len(text) - 1:
        var1 = 0
        var2 = 0
        j = 0
        while j < len(alphabet):
            if text[i] == alphabet[j]:
                var1 = j
            if text[i + 1] == alphabet[j]:
                var2 = j
            j += 1
        textlist.append(var1 * 31 + var2)
        i += 2

    i = 0
    indexes = []
    while i < len(list_a):
        j = 0
        while j < len(list_b):
            k = 0
            textlist1 = []
            textlist2 = []
            while k < len(textlist):
                var = (extended_euclid(list_a[i], 961)[1] * (textlist[k] - list_b[j])) % 961
                textlist1.append(var)
                textlist2.append([alphabet[int(var/31)], alphabet[var - int(var/31) * 31]])
                k += 1

            print(textlist2)
            textlist3 = str(textlist2)
            textlist3 = textlist3.replace('[', '')
            textlist3 = textlist3.replace(']', '')
            textlist3 = textlist3.replace(',', '')
            textlist3 = textlist3.replace("'", '')
            textlist3 = textlist3.replace(' ', '')
            #print('textlist3:', textlist3)
            qwerty = task2(textlist3)
            indexes.append(qwerty)
            #print(textlist3)
            if qwerty == 0.05508408250098322:
                print(textlist3)
                print(l1, l2, l3, l4, '1, l2, l3, l4')
                var = open('07 -- decrypted.txt', 'w')
                var.write(str(textlist3))

            j += 1
        i += 1
    #print('indexes:', indexes)
    return indexes
#decrypt('V7.txt', [17, 18], [13, 14], [2, 12], [12, 27])
#decrypt('07.txt', [13, 14], [17, 18], [22, 11], [11, 5])

mcb = [mcb1, mcb2, mcb3, mcb4, mcb5]
lmcb = [lmcb1, lmcb2, lmcb3, lmcb4, lmcb5]




finalindexes = []
indexes = []
i = 0
while i < len(mcb):
    i1 = 0
    while i1 < len(mcb):
        if i1 != i:
            j = 0
            while j < len(lmcb):
                j1 = 0
                while j1 < len(lmcb):
                    if j1 != j:
                        #print(lmcb[j], lmcb[j1], mcb[i], mcb[i1], 'lmcb[j], lmcb[j1], mcb[i], mcb[i1]')
                        indexes = decrypt('07.txt', lmcb[j], lmcb[j1], mcb[i], mcb[i1])
                        k = 0
                        if indexes != 0:
                            while k < len(indexes):
                                finalindexes.append(indexes[k])
                                k += 1
                            #print('---------------------------------------------------------------------------------------\n')
                    j1 += 1
                j += 1
        i1 += 1
    i += 1
print('len(finalindexes):', len(finalindexes))
print(type(finalindexes[0]))
print(max(finalindexes), ' --  max(finalindexes)')
