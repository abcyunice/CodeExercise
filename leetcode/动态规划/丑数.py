class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1]
        index = [0 for i in primes]
        for i in range(1, n):
            min_ = 2 ** 32
            for j in range(len(primes)):
                if min_ > primes[j] * dp[index[j]]:
                    min_ = primes[j] * dp[index[j]]
            dp.append(min_)
            for j in range(len(primes)):
                if min_ == primes[j] * dp[index[j]]:
                    index[j] += 1

        return dp[-1]