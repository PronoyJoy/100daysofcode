class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.parent[root_y] = root_x

# Test Cases
if __name__ == '__main__':
    uf = UnionFind(5)

    # Initial disjoint sets: {0}, {1}, {2}, {3}, {4}
    # User Ids 
    # Make Friends
    #  
    uf.union(0, 2) #using it as object 
    uf.union(4, 1)
    uf.union(3, 1)

    # After union operations: {0, 2}, {1, 3, 4}

    #now find friendship
    
    print(uf.find(0))  # Output: 2
    print(uf.find(4))  # Output: 2
    print(uf.find(3))  # Output: 2
    print(uf.find(1))  # Output: 2