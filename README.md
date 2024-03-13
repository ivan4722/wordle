# wordle
Is wordle word selection truly random or is it biased?
![graph](https://i.imgur.com/h1HDE3A.png)

# 1. Are any letters used more in the wordle words than across all words in the English dictionary?
Per this source: https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
We can see the percentage of all letters for each letter respective is as follows:
```
A 8.4966%
B 2.0720%
C 4.5388%
D 3.3844%
E 11.1607%
F 1.8121%
G 2.4705%
H 3.0034%
I 7.5448%
J 0.1965%
K 1.1016%
L 5.4893%
M 3.0129%
N 6.6544%
O 7.1635%
P 3.1671%
Q 0.1962%
R 7.5809%
S 5.7351%
T 6.9509%
U 3.6308%
V 1.0074%
W 1.2899%
X 0.2902%
Y 1.7779%
Z 0.2722%
```
We can count the freuqency of each letter in each of the past 997 wordle words (as of 3/12/24).
```
A 8.9869%
B 2.3671%
C 4.2528%
D 3.1294%
E 10.7924%
F 1.8656%
G 2.8686%
H 3.7312%
I 5.5767%
J 0.2006%
K 1.9458%
L 6.0983%
M 2.6480%
N 4.8546%
O 6.8405%
P 3.1093%
Q 0.2808%
R 7.9639%
S 5.2156%
T 6.8004%
U 3.7914%
V 1.1434%
W 1.5446%
X 0.3811%
Y 3.2297%
Z 0.3811%
```

We can see the numbers are relatively similar by examination, but lets see how similar they are by calculating the pearson correlation coefficient. Because we have two continuous variables, we can examine the statistical significance by measuring the association between the two variables. We can also calculate the p-value to further support the statistical significance.
```
Pearson Correlation Coefficient: 0.9733621073220139
P-value: 7.35520736230258e-17
```
As we can see by the very high Pearson correlation coefficient of >0.5 denoting positive relationship, and 0.97... denotes a very strong positive relationship. (with frequency of letters of all words on y axis and frequency of letters of wordle words on x axis).

**Based on the strong correlation, what does that tell us in terms of how wordle selects their words?**\
Based on the Pearson correlation coefficient of 0.9733621073220139 and P-value of 7.35520736230258e-17, we can deduce that the correlation is not due to random chance. Based on the statistical analysis, I believe the wordle word selection is not biased and systemically similar to that of the total English language. More generally, Wordle's word selection is relatively representative of the letter distribution across the total English language. 
