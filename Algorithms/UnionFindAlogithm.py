# Initialize the sets
def initialize(n):  # sourcery skip: inline-immediately-returned-variable
    parent = list(range(n)) #this line will create numbers
    return parent

parent = initialize(5)

print(parent)


def find(x):
    if parent[x] == x:
        return x
    else:
        return find(parent[x]) #recursive

def union(x,y):
    if find(x) != find(y):
        parent[find(x)] = parent[find(y)]



# Main program
n = 10  # Number of elements
parent = initialize(n)

# Perform union operations
union(1, 2)
union( 3, 4)
union( 5, 6)
union( 2, 8)

# Test the find operation
print(find(1))  # Output: 2
print(find(3))  # Output: 4
print(find(5))  # Output: 6
print(find(8))  # Output: 2

