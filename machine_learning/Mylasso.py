import numpy as np
from sklearn.linear_model import Lasso
import datetime
import numba as nb


def coor_decent(X, y, w0, max_iter, alpha, max_e):
    w = w0
    nrows_w = X.shape[1]
    nrows_X = X.shape[0]

    for iter_num in range(max_iter):
        w_ori = w.copy()

        # j = 0
        y_mh = y[:, 0] - (X.dot(w[:, 0]) - w[0, 0] * X[:, 0])
        rho_j = y_mh.T.dot(X[:, 0])
        z_j = np.sum(X[:, 0] ** 2)

        rho_j = rho_j / nrows_X / 2
        z_j = z_j / nrows_X / 2
        w[0, 0] = rho_j / z_j

        # j = 1-N
        for j in range(1, nrows_w):
            y_mh = y[:, 0] - (X.dot(w[:, 0]) - w[j, 0] * X[:, j])
            rho_j = y_mh.T.dot(X[:, j])
            z_j = np.sum(X[:, j] ** 2)

            rho_j = rho_j / nrows_X / 2
            z_j = z_j / nrows_X / 2
            w[j, 0] = rho_j / z_j

            if rho_j < -1 / 2 * alpha:
                w[j, 0] = (rho_j + 1 / 2 * alpha) / z_j
            elif rho_j > 1 / 2 * alpha:
                w[j, 0] = (rho_j - 1 / 2 * alpha) / z_j
            else:
                w[j, 0] = 0.0

        w_delta_sum = np.sum((w - w_ori) ** 2)
        if w_delta_sum < max_e:
            break
    return w


class MyLasso():
    '''
            (1 / (2 * n_samples)) * ||y - Xw||^2_2 + alpha * ||w||_1
    '''

    def __init__(self, alpha=1.0, max_iter=10000, max_e=1e-10):
        self.alpha = alpha
        self.max_iter = max_iter
        self.max_e = max_e
        self._w = None

    def fit(self, X, y):
        X = np.hstack([np.ones([X.shape[0], 1]), X])
        w0 = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
        w = coor_decent(X, y, w0, self.max_iter, self.alpha, self.max_e)
        self._w = w

    def score(self, X, y):
        SST = np.sum((y - np.mean(y)) ** 2)
        y_pred = X.dot(self._w)
        SSR = np.sum((y - y_pred) ** 2)
        return 1 - SSR / SST

    def pred(self, X):
        return X.dot(self._w)

    @property
    def coef_(self):
        return self._w[1:].copy()

    @property
    def intercept_(self):
        return self._w[:1].copy()

    def loss_func(self, X, y):
        X = np.hstack([np.ones([X.shape[0], 1]), X])
        return np.sum((y - X.dot(self._w)) ** 2) / 2 / X.shape[0] + self.alpha * np.sum(np.abs(self._w))


def main():
    np.random.seed(1)

    X = np.random.normal(size=[10000, 100])
    y = X.dot(np.ones([100, 1])) + np.random.normal(size=[10000, 1])

    dt1 = datetime.datetime.now()
    mylasso = MyLasso(alpha=1)
    mylasso.fit(X, y)
    print(mylasso.intercept_)

    dt2 = datetime.datetime.now()
    mylasso2 = Lasso(alpha=1)
    mylasso2.fit(X, y)
    print(mylasso2.intercept_)

    dt3 = datetime.datetime.now()

    print(dt2 - dt1, dt3 - dt2)


if __name__ == "__main__":
    main()
