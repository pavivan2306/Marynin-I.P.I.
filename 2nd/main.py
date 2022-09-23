import random
import pandas as pd
import openpyxl
al = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
str(al)
l = len(al)
alphabet = []
i = 0
while(i!=l):
    alphabet.append(al[i])
    i += 1

df = pd.DataFrame(0,
                columns=['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
                         '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32'],
                index=['Y_0', 'Y_1', 'Y_2', 'Y_3', 'Y_4', 'Y_5', 'Y_6', 'Y_7', 'Y_8', 'Y_9', 'Y_10', 'Y_11', 'Y_12', 'Y_13',
                       'Y_14', 'Y_15', 'Y_16', 'Y_17', 'Y_18', 'Y_19', 'Y_20', 'Y_21', 'Y_22', 'Y_23', 'Y_24', 'Y_25',
                       'Y_26', 'Y_27', 'Y_28', 'Y_29', 'Y_30', 'Y_31'])

def encrypt(k_len):
    a = open('1.txt', 'r')
    a = a.read()
    a = str(a)
    key = []
    i = 0
    while i < k_len:
        key.append(random.randint(0, 32))
        i += 1
    print(key, ' --  key')
    encrypted = []
    i = 0
    while i < len(a):
        j = 0
        while j < len(alphabet):
            if a[i] == alphabet[j]:
                var = (j + key[i % k_len]) % 33
                encrypted.append(alphabet[var])
                break
            j += 1
        i += 1
    a = str(encrypted)
    a = a.replace('[', '')
    a = a.replace(']', '')
    a = a.replace(',', '')
    a = a.replace("'", '')
    a = a.replace(' ', '')
    var = open('encr-text-30.txt', 'w')
    var.write(a)

def task2(a):
    a = open(a, 'r')
    a = a.read()
    a = str(a)
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

def lengthsearch1(a):
    a = open(a, 'r')
    a = a.read()
    a = str(a)
    print(a)
    r = 2
    average = []
    while r <= 32:
        i = 0
        summY_i = 0
        counterY_i = 0
        while i < r:
            Y_i = []
            k = 0
            while k*r+i < len(a):
                Y_i.append(a[k*r+i])
                k += 1
            Y_i = str(Y_i)
            Y_i = Y_i.replace('[', '')
            Y_i = Y_i.replace(']', '')
            Y_i = Y_i.replace(',', '')
            Y_i = Y_i.replace("'", '')
            Y_i = Y_i.replace(' ', '')
            counterlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0]
            i1 = 0
            while i1 < len(Y_i):
                j = 0
                while j < len(alphabet):
                    if Y_i[i1] == alphabet[j]:
                        counterlist[j] += 1
                        break
                    j += 1
                i1 += 1
            I = 0
            i1 = 0
            while i1 < len(counterlist):
                I += counterlist[i1] * (counterlist[i1] - 1)
                i1 += 1
            I = I / (len(Y_i) * (len(Y_i) - 1))
            summY_i += I
            counterY_i += 1
            df.iat[i, r - 2] = I
            print('r =', r, 'i =', i, Y_i)
            i += 1
        print('')
        r += 1
        average.append(summY_i / counterY_i)
    df.to_excel("indexes1.xlsx", sheet_name='1.xlsx')
    print(df)
    print(average, 'average')
    print(max(average), 'max(average)')
    var = open('average.txt', 'w')
    var.write(str(average))
#lengthsearch('var1.txt')


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

#lengthsearch2('var1.txt')


def keysymbols1(a):
    a = open(a, 'r')
    a = a.read()
    a = str(a)
    r = 15
    i = 0
    mostcommon = []
    while i < r:
        Y_i = []
        k = 0
        while k * r + i < len(a):
            Y_i.append(a[k * r + i])
            k += 1
        Y_i = str(Y_i)
        Y_i = Y_i.replace('[', '')
        Y_i = Y_i.replace(']', '')
        Y_i = Y_i.replace(',', '')
        Y_i = Y_i.replace("'", '')
        Y_i = Y_i.replace(' ', '')
        counterlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        i1 = 0
        while i1 < len(Y_i):
            j = 0
            while j < len(alphabet):
                if Y_i[i1] == alphabet[j]:
                    counterlist[j] += 1
                    break
                j += 1
            i1 += 1
        i1 = 0
        while i1 < len(counterlist):
            if counterlist[i1] == max(counterlist):
                mostcommon.append(i1)
                break
            i1 += 1
        if i == 1:
            print(counterlist, 'counterlist')
        i += 1
    print(mostcommon, 'mostcommon')
    mostcommon1 = []
    i = 0
    while i < len(mostcommon):
        mostcommon1.append(mostcommon[i])
        i += 1
    i = 0
    while i < len(mostcommon1):
        if mostcommon1[i] - 14 >= 0:
            mostcommon1[i] = mostcommon1[i] - 14
        else:
            mostcommon1[i] = 32 + (mostcommon1[i] - 14)
        i += 1
    print(mostcommon1)
    key = []
    i = 0
    while i < len(mostcommon1):
        j = 0
        while j < len(alphabet):
            if mostcommon1[i] == j:
                key.append(alphabet[j])
                break
            j += 1
        i += 1
    print(key, ' --  key')
    print(mostcommon, 'with len =', len(mostcommon))
#keysymbols1('var1.txt')

def keysymbols2(a):
    a = open(a, 'r')
    a = a.read()
    a = str(a)
    r = 15
    df1 = pd.DataFrame(0,
                      columns=['Y_0', 'Y_1', 'Y_2', 'Y_3', 'Y_4', 'Y_5', 'Y_6', 'Y_7', 'Y_8', 'Y_9', 'Y_10', 'Y_11',
                             'Y_12', 'Y_13', 'Y_14'],
                      index=['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
                          'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'])
    i = 0
    K= []
    while i < r:
        Y_i = []
        k = 0
        while k * r + i < len(a):
            Y_i.append(a[k * r + i])
            k += 1
        Y_i = str(Y_i)
        Y_i = Y_i.replace('[', '')
        Y_i = Y_i.replace(']', '')
        Y_i = Y_i.replace(',', '')
        Y_i = Y_i.replace("'", '')
        Y_i = Y_i.replace(' ', '')
        counterlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        i1 = 0
        while i1 < len(Y_i):
            j = 0
            while j < len(alphabet):
                if Y_i[i1] == alphabet[j]:
                    counterlist[j] += 1
                    break
                j += 1
            i1 += 1
        M_ig = []
        g = 0
        probability = count('1.txt')
        while g < len(alphabet):
            summ = 0
            t = 0
            while t < len(alphabet):
                summ += probability[t] * counterlist[(t+g) % len(alphabet)]
                t += 1
            M_ig.append(summ)
            df1.iat[g, i] = summ
            g += 1
        g = 0
        while g < len(M_ig):
            if M_ig[g] == max(M_ig):
                K.append(g)
                break
            g += 1
        i += 1
    df1.to_excel("Mi(g).xlsx", sheet_name='1.xlsx')
    print(K)


def count(a):
    a = open(a, 'r')
    a = a.read()
    a = str(a)
    counterlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    while i < len(a):
        j = 0
        while j < len(alphabet):
            if a[i] == alphabet[j]:
                counterlist[j] += 1
            j += 1
        i += 1
    i = 0
    while i < len(counterlist):
        counterlist[i] = counterlist[i]/len(a)
        i += 1
    return counterlist

#count('1.txt')
keysymbols2('var1.txt')

def decrypt(a):
    a = open(a, 'r')
    a = a.read()
    a = str(a)
    print(len(a))
    i = 0
    key = ['а', 'р', 'у', 'д', 'а', 'з', 'е', 'в', 'а', 'р', 'х', 'и', 'м', 'а', 'г']
    while i < len(key):
        j = 0
        while j < len(alphabet):
            if key[i] == alphabet[j]:
                if i == 0:
                    print('hell yeah!')
                key[i] = j
                break
            j += 1
        i += 1
    i = 0
    print(key)
    #[10, 4, 0, 25, 7, 20, 2, 16, 21, 26, 31, 0, 3, 0, 20]
    decrypted = []
    while i < len(a):
        j = 0
        while j < len(alphabet):
            if a[i] == alphabet[j]:
                break
            j += 1
        if j - key[i % len(key)] >= 0:
            decrypted.append(j - key[i % len(key)])
        else:
            decrypted.append(32 + j - key[i % len(key)])
        i += 1
    i = 0
    while i < len(decrypted):
        j = 0
        while j < len(alphabet):
            if decrypted[i] == j:
                decrypted[i] = alphabet[j]
                break
            j += 1
        i += 1
    decrypted = str(decrypted)
    decrypted = decrypted.replace('[', '')
    decrypted = decrypted.replace(']', '')
    decrypted = decrypted.replace(',', '')
    decrypted = decrypted.replace("'", '')
    decrypted = decrypted.replace(' ', '')
    var = open('decrypted text -- var1-1.txt', 'w')
    var.write(decrypted)
    print(decrypted)
#decrypt('var1-1.txt')
