class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        parents = [-1 for i in range(N * 2 + 2)]
        def getRoot(a, parents):
            while parents[a] != -1:
                a = parents[a]
            return a

        for i, j in dislikes:
            rooti = getRoot(i, parents)
            rootj = getRoot(j, parents)

            if rooti == rootj:
                return False
            
            a = getRoot(i + N, parents)
            b = getRoot(j + N, parents)

            if a != rootj:
                parents[a] = rootj 
            if b != rooti:
                parents[b] = rooti 

        return True