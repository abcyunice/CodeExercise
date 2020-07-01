import numpy as np


class Hicluster(object):
    def __init__(self):
        pass

    def helperDist(self, X):
        G = np.dot(X, X.T)
        DiagX = np.tile(np.diag(G), (X.shape[0], 1))
        return DiagX + DiagX.T - 2 * G

    def fit(self, X):
        X_copy = X.copy()
        result = []
        idx_list = [i for i in range(X.shape[0])]
        while X_copy.shape[0] > 1:
            dist = self.helperDist(X_copy)
            np.fill_diagonal(dist, np.max(dist) + 1)

            s = np.argmin(dist)
            s0 = s // X_copy.shape[0]
            s1 = s - X_copy.shape[0] * s0
            i, j = min(s0, s1), max(s0, s1)

            X_mean = (X_copy[[i], :] + X_copy[[j], :]) / 2
            X_copy = np.vstack([X_copy[:i, :], X_copy[i + 1:j, :], X_copy[j + 1:, :], X_mean])

            result.append([idx_list[i], idx_list[j]])
            idx_list = idx_list[:i] + idx_list[i + 1:j] + idx_list[j + 1:] + [idx_list[-1] + 1]

        self._result = result

    @property
    def result(self):
        return self._result


np.random.seed(1)
X = np.random.normal(size=(10, 1))
print(X)
hicluster = Hicluster()
hicluster.fit(X)
print(hicluster.result)