import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import numpy as np
from scipy.stats import pearsonr

import pandas as pd

wordle_data = pd.read_csv('wordle.csv', header=None, names=['Word'])
words = wordle_data['Word'].tolist()
#print(words)
counta=0
counte=0
counti=0
countu=0
countae=0
countai=0
countau=0
countei=0
counteu=0
countiu=0
countaei=0
countaeu=0
countaiu=0
counteiu=0
countaeiu=0
print(len(words))
for i in words:
    if 'A' in i:
        counta+=1
        if 'E' in i:
            countae+=1
            if 'I' in i:
                countaei+=1
                if 'U' in i:
                    countaeiu+=1
            if 'U' in i:
                countaeu+=1
        if 'I' in i:
            countai+=1
            if 'U' in i:
                countaiu+=1
        if 'U' in i:
            countau+=1
    if 'E' in i:
        counte+=1
        if 'I' in i:
            countei+=1
            if 'U' in i:
                counteiu+=1
        if 'U' in i:
            counteu+=1
    if 'I' in i:
        counti+=1
        if 'U' in i:
            countiu+=1
    if 'U' in i:
        countu+=1
print('A:',counta/997)
print('E:',counte/997)
print('I:',counti/997)
print('U:',countu/997)
print('A ∩ E: ', countae/997)
print('A ∩ I: ', countai/997)
print('A ∩ U: ', countau/997)
print('E ∩ I: ', countei/997)
print('E ∩ U: ', counteu/997)
print('I ∩ U: ', countiu/997)
print('A ∩ E ∩ I: ', countaei/997)
print('A ∩ E ∩ U: ', countaeu/997)
print('A ∩ I ∩ U: ', countaiu/997)
print('E ∩ I ∩ U: ', counteiu/997)
print('A ∩ E ∩ I ∩ U: ', countaeiu/997)
'''
def count_letter_frequency_all(words):
    frequency_dict = {}
    for word in words:
        for letter in word:
            letter = letter.upper()  
            frequency_dict[letter] = frequency_dict.get(letter, 0) + 1
    return frequency_dict

letter_frequency_all = count_letter_frequency_all(wordle_data['Word'])

for key,val in letter_frequency_all.items():
    print(f"{key} {(val/(997*5))*100}%")

x = np.array([8.4966, 2.0720, 4.5388, 3.3844, 11.1607, 1.8121, 2.4705, 3.0034, 7.5448,
              0.1965, 1.1016, 5.4893, 3.0129, 6.6544, 7.1635, 3.1671, 0.1962, 7.5809,
              5.7351, 6.9509#, 3.6308, 1.0074, 1.2899, 0.2902, 1.7779, 0.2722])


y = np.array([8.9869, 2.3671, 4.2528, 3.1294, 10.7924, 1.8656, 2.8686, 3.7312, 5.5767,
              0.2006, 1.9458, 6.0983, 2.6480, 4.8546, 6.8405, 3.1093, 0.2808, 7.9639,
              5.2156, 6.8004, 3.7914, 1.1434, 1.5446, 0.3811, 3.2297, 0.3811])

correlation_coefficient, p_value = pearsonr(x, y)

print(f"Pearson Correlation Coefficient: {correlation_coefficient}")
print(f"P-value: {p_value}")
'''