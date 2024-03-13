# wordle
Is wordle word selection truly random or is it biased?
![graph](https://i.imgur.com/h1HDE3A.png)

# 1. Are any letters used more in the wordle words than across all 5 words in the English dictionary?
Per this source: https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
We can see the percentage of all letters for each letter respective is as follows:
```
E  11.1607%  M  3.0129%
A  8.4966%   H  3.0034%
R  7.5809%   G  2.4705%
I  7.5448%   B  2.0720%
O  7.1635%   F  1.8121%
T  6.9509%   Y  1.7779%
N  6.6544%   W  1.2899%
S  5.7351%   K  1.1016%
L  5.4893%   V  1.0074%
C  4.5388%   X  0.2902%
U  3.6308%   Z  0.2722%
D  3.3844%   J  0.1965%
P  3.1671%   Q  0.1962%
```
We can count the freuqency of each letter in each of the past 997 wordle words (as of 3/12/24).
```
A 8.986960882647944%
B 2.3671013039117352%
C 4.252758274824473%
K 1.945837512537613%
S 5.2156469408224675%
E 10.792377131394183%
T 6.800401203610833%
Y 3.2296890672016048%
O 6.8405215646940825%
U 3.791374122367101%
V 1.1434302908726177%
R 7.963891675025075%
I 5.576730190571715%
D 3.1293881644934802%
P 3.1093279839518555%
M 2.6479438314944836%
L 6.098294884653962%
F 1.8655967903711133%
G 2.868605817452357%
N 4.85456369107322%
W 1.5446339017051154%
H 3.7311935807422265%
X 0.3811434302908726%
Z 0.3811434302908726%
J 0.20060180541624875%
Q 0.28084252758274825%
```
