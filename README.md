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
As we can see by the very high Pearson correlation coefficient of $>0.5$ denoting positive relationship, and $0.97...$ denotes a very strong positive relationship. (with frequency of letters of all words on y axis and frequency of letters of wordle words on x axis). Additionally the p-value of $7.35520736230258e-17 < 0.05$ allows us to reject the null hypothesis, denoting statistical significance.

**Based on the strong correlation, what does that tell us in terms of how wordle selects their words?**\
Based on the Pearson correlation coefficient of $0.9733621073220139$ and P-value of $7.35520736230258e-17$, we can deduce that the correlation is not due to random chance. Based on the statistical analysis, I believe the wordle word selection is not biased and systemically similar to that of the total English language. More generally, Wordle's word selection is relatively representative of the letter distribution across the total English language. 

# 2. Game Theory Optimal (GTO) Wordle: Why is "adieu" the best choice?
All words contain one vowel. According to the Wordle analysis bot, the optimal guess is "adieu" to guess $4/5$ of the vowels. \
Lets see why that is. \
What is the probability with the guess "adieu" that we hit at least one vowel?\
First, lets consider that the probability that a word has the letter $\alpha_1$ is not mutually exclusive to $\alpha_2$, $\alpha_i$ denoting any letter.\
$P(\text{at least one vowel guessed by "adieu"}) = P (A ∪ E ∪ I ∪ U)$ \
$= P(A) + P(E) + P(I) +P(U) - P(A ∩ E) - P(A ∩ I) - P(A ∩ U)- P(E ∩ I) $\
$ - P(E ∩ U) - P(I ∩ U) + P(A ∩ E ∩ I) + P(A ∩ E ∩ U) + P(A ∩ I ∩ U) + P(E ∩ I ∩ U) - P(A ∩ E ∩ I ∩ U) $\
There are some words that have no vowels and have a "y" in place (ex: cysts), but they are a small subset of the total words so for simplicity we will ignore them.\
Below is the count of each word that has the following letters:
```
A: 413
E: 474
I: 270
O: 308
U: 185
A ∩ E:  173
A ∩ I:  64
A ∩ U:  37
E ∩ I:  107
E ∩ U:  53
I ∩ U:  24
A ∩ E ∩ I:  11
A ∩ E ∩ U:  10
A ∩ I ∩ U:  2
E ∩ I ∩ U:  6
A ∩ E ∩ I ∩ U:  0
```
We can then calculate the probability by dividing by the total amount of words (997).
```
A: 0.41424272818455365
E: 0.4754262788365095
I: 0.2708124373119358
U: 0.1855566700100301
A ∩ E:  0.17352056168505517
A ∩ I:  0.0641925777331996
A ∩ U:  0.037111334002006016
E ∩ I:  0.10732196589769308
E ∩ U:  0.05315947843530592
I ∩ U:  0.024072216649949848
A ∩ E ∩ I:  0.011033099297893681
A ∩ E ∩ U:  0.010030090270812437
A ∩ I ∩ U:  0.0020060180541624875
E ∩ I ∩ U:  0.006018054162487462
A ∩ E ∩ I ∩ U:  0.0
```
Then, we can now compute the probability: \
$P(\text{at least one vowel guessed by "adieu"}) = P (A ∪ E ∪ I ∪ U)$ \
$= P(A) + P(E) + P(I) +P(U) - P(A ∩ E) - P(A ∩ I) - P(A ∩ U)- P(E ∩ I)$\
$- P(E ∩ U) - P(I ∩ U) + P(A ∩ E ∩ I) + P(A ∩ E ∩ U) + P(A ∩ I ∩ U) + P(E ∩ I ∩ U) - P(A ∩ E ∩ I ∩ U)$\
$=0.41424272818455365+0.4754262788365095+0.2708124373119358+0.1855566700100301-0.17352056168505517-0.0641925777331996-0.037111334002006016$\
$-0.10732196589769308-0.05315947843530592-0.024072216649949848+0.011033099297893681+0.010030090270812437+0.0020060180541624875+0.006018054162487462-0$\
This evaluates to $0.91574724172$.\
**What does this tell us?** \
Well, this data does not tell us anything regarding the green and yellow squares (denoting correct index of the letter). \
However, it does tell us that with $\approx91.57$%, any word in the experimental 997 past words will have the letters a e i or u. As a result, the guess "adieu" will have a "hit" with $91.57$% of words. (realistically it is higher if you consider the "d" letter, but for the sake of the argument we used only the vowels.)\

**How does this compare to random guessing?**\
There are $26^5$ total 5 letter "words". There are not actually this many 5 letter words, but there are $26^5$ permutations of letter arrangements of length 5. That means for each letter, there is a $1/26$ chance that it is guessed correctly.\
Lets compute the probability that we guess at least 1 letter correct. \
$P(\text{at least one correct}) = 1 - P(\text{none correct})=1-(25\div26)^5=0.17807289324\approx 17.81$%.\
We can see the probability of getting at least one letter of "randomly guessing" is only around 17.81%, compared to guessing "adieu" with a probability of 91.57%. 
We can deduce from this data that "adieu" is a better-than-random guess, as supported by wordle's analysis bot as well. 

