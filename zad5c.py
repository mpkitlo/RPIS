import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Rows: women, men
# Columns: PiS, PO, Kukiz, Nowoczesna, Lewica, PSL, Razem, KORWiN
data = np.array([[ 17508, 11642,  3308,  3131,  2911,  2205,  1852, 1235],
                [ 17672,  9318,  4865,  3259,  3029,  2479,  1606, 3259]])


def aggregate(procent, data):
    data2 = [[],[]]

    suma = np.sum(data)

    suma_women = 0
    suma_men = 0

    for i in range(len(data[0])):
        if(data[0][i] + data[1][i] < procent * suma):
            suma_women += data[0][i]
            suma_men += data[1][i]
        else:
            data2[0].append(data[0][i])
            data2[1].append(data[1][i])
    data2[0].append(suma_women)
    data2[1].append(suma_men)

    return data2




def chi_square_independence_test_pvalue(data):
    data = aggregate(0.05, data)
    
    degrees_of_freedom = (len(data) - 1) * (len(data[0]) - 1)

    total = np.sum(data)
    
    row_sum = np.sum(data, axis = 1)
    column_sum = np.sum(data, axis = 0)
    S = 0
    
    for i in range(len(data)):
        for j in range(len(data[0])):
            exp = row_sum[i] * column_sum[j] / total
            real = data[i][j]
            S += ((real - exp)**2) / exp
            
            
    return 1 - stats.chi2.cdf(S, degrees_of_freedom)


def attempt():
    # generate a similar dataset with 6 parties and two genders
    # this time the null hypothesis is true, i.e., gender has no effect on voting preferences

    data = np.zeros([2, 6])

    for k in range(10000):
      i = np.random.randint(2)
      j = int(np.sqrt(np.random.randint(36)))
      data[i][j] = data[i][j] + 1
    # replace np.random.random() with the p-value returned by your implementation of chi-square independence test
    # return chi_square_independence_test_pvalue(data)

    return chi_square_independence_test_pvalue(data)
    # return np.random.random()
    
pvalues = [attempt() for t in range(200)]
print(pvalues[:20])
# The values you get here should have (roughly) uniform distribution in [0,1].
# Note: this means that, in 20 attempts, we are likely to find one to rejecting the null hypothesis,
# even though the null hypothesis is true!
plt.hist(pvalues)

# to test whether the distribution of pvalue is indeed close to uniform distribution,
# we can use the Kolmogorov-Smirnov test:
stats.kstest(pvalues, "uniform")

# Examine the pvalue returned by kstest.
# Introduce a bug in your implementation (e.g. change the number of degrees of freedom) and see how the
# pvalue returned by kstest changes.
