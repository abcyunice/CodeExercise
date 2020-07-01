import numpy as np


class Kmeans(object):
    def __init__(self, k):
        self.k = k

    def fit(self, X):
        result = np.random.randint(1, self.k, size=(X.shape[0],))
        dist_helper = np.ones(shape=(X.shape[0], self.k))
        while True:
            for resulti in result:
                mean_ = np.mean(X[result == resulti], axis=0)
                dist_helper[:, resulti] = np.sqrt(np.sum((X - mean_) ** 2, axis=1))

            result_tmp = np.argmin(dist_helper, axis=1)

            if np.sum(np.abs(result_tmp - result)) == 0:
                self.result = result_tmp
                return
            
            result = result_tmp

    @property
    def Ksort(self):
        return self.result


import matplotlib.pyplot as plt

np.random.seed(2)
X = np.random.normal(size=(100, 2))
mykmeans = Kmeans(3)
mykmeans.fit(X)

plt.figure()
for i, c in zip([0, 1, 2], ["r", "g", "b"]):
    plt.scatter(X[mykmeans.Ksort == i, 0], X[mykmeans.Ksort == i, 1], c=c)
plt.show()
