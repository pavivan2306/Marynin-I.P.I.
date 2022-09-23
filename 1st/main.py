import pandas as pd
from math import log2
a = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
str(a)
l = len(a)
alphabet1 = []
k = 0
while(k!=l):
    alphabet1.append(a[k])
    k = k + 1
a = ' абвгдежзийклмнопрстуфхцчшщъыьэюя'
str(a)
l = len(a)
alphabet2 = []
k = 0
while(k!=l):
    alphabet2.append(a[k])
    k = k + 1
a = open('TEXT.txt', 'r')
с = a.read()
counterlist1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
counterlist2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
b = []
while i < len(b):
    j = 0
    if b[i] == ' ' and b[i - 1] == ' ':
        pass
    else:
        while j < len(alphabet1):
            if b[i] == alphabet1[j]:
                b.append(b[i])
            j += 1
    i += 1
def frequency_letters2():
    i = 0
    while (i < len(b)):
        j = 0
        while (j < len(alphabet2)):
            if (b[i] == alphabet2[j]):
                counterlist2[j] += 1
                break
            j += 1
        i += 1
    print(counterlist2)
    print(len(b))
    l = 0
    while (l<len(counterlist2)):
        counterlist2[l] = counterlist2[l]/len(b)
        l += 1
    df = pd.DataFrame(0,
                      columns=['Частота'],
                      index=[' ', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
                             'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'])
    i = 0
    while i < len(counterlist2):
        df.at[alphabet1[i], 'Частота'] = counterlist2[i]
        i += 1
    df.to_excel("букви з пробілом.xlsx", sheet_name='1.xlsx')
def frequency_bigrams():
    df = pd.DataFrame(0,
                      columns=[' ', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
                               'с', 'т', 'у', 'ф', 'х', 'ц',
                               'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'],
                      index=[' ', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
                             'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'])
    i = 0
    bigram_counter = 0
    while (i < len(b) - 1):
        if (b[i] == '\n' or b[i + 1] == '\n'):
            i = i + 1
        j = 0
        while (j < len(alphabet2)):
            if (b[i] == alphabet2[j]):
                k = 0
                while (k < len(alphabet2)):
                    if (b[i + 1] == alphabet2[k]):
                        df.at[alphabet2[j], alphabet2[k]] += 1
                        bigram_counter += 1
                    k += 1
            j += 1
        i += 1
    df.to_excel("with_a_cross.xlsx", sheet_name='1.xlsx')
    i = 0
    while(i < len(alphabet2)):
        j = 0
        while(j < len(alphabet2)):
            df.at[alphabet2[i], alphabet2[j]] = df.at[alphabet2[i], alphabet2[j]] / bigram_counter
            j += 1
        i += 1
    df1 = pd.DataFrame(0,
                    columns=['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
                            'т', 'у', 'ф', 'х', 'ц',
                            'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'],
                    index=['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
                          'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'])
    df = pd.DataFrame(0,
                    columns=[' ', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
                           'с', 'т', 'у', 'ф', 'х', 'ц',
                           'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'],
                    index=[' ', 'а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
                         'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'])
    i = 0
    bigram_counter = 0
    while (i < len(b) - 1):
        if (b[i] == '\n' or b[i + 1] == '\n'):
            i = i + 1
        j = 0
        while (j < len(alphabet2)):
            if (b[i] == alphabet2[j]):
                k = 0
                while (k < len(alphabet2)):
                    if (b[i + 1] == alphabet2[k]):
                        df.at[alphabet2[j], alphabet2[k]] += 1
                        bigram_counter += 1
                    k += 1
            j += 1
        i += 2
    df.to_excel("without_a_cross.xlsx", sheet_name='1.xlsx')
    i = 0
    while(i < len(alphabet2)):
        j = 0
        while(j < len(alphabet2)):
            df.at[alphabet2[i], alphabet2[j]] = df.at[alphabet2[i], alphabet2[j]] / bigram_counter
            j += 1
        i += 1
def GetEntropy1():
    i = 0
    H_1 = 0
    while (i < len(alphabet2)):
        if counterlist2[i] != 0:
            H_1 += counterlist2[i] * log2(counterlist2[i])
        i += 1
    print('Ентропія Н_1:')
    print(-H_1)
def GetEntropy2():
    i = 0
    H_2 = 0
    while (i < len(alphabet2)):
        j = 0
        while (j < len(alphabet2)):
            if df.at[alphabet2[i], alphabet2[j]] != 0:
                H_2 += df.at[alphabet2[i], alphabet2[j]] * log2(df.at[alphabet2[i], alphabet2[j]])
            j += 1
        i += 1
    print('Ентропія Н_2:')
    print(-H_2)
