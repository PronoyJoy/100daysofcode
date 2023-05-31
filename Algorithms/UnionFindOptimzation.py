import tkinter as tk


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


def are_friends(user_id1, user_id2):
    # Assuming user IDs are integers
    n = max(user_id1, user_id2) + 1
    uf = UnionFind(n)

    # Here you would implement the logic to populate the disjoint sets based on the friendships
    # For demonstration purposes, let's assume a simple case where friends are directly connected
    friendships = [(1, 2), (2, 3), (4, 5)]

    for friend1, friend2 in friendships:
        uf.union(friend1, friend2)

    return uf.connected(user_id1, user_id2)


def check_friends():
    user1 = int(entry_user1.get())
    user2 = int(entry_user2.get())
    result = are_friends(user1, user2)
    label_result.config(text=f"Are user {user1} and user {user2} friends? {result}")


# Create the main window
window = tk.Tk()
window.title("Friendship Checker")

# Create the user input fields
label_user1 = tk.Label(window, text="User 1 ID:")
label_user1.pack()
entry_user1 = tk.Entry(window)
entry_user1.pack()

label_user2 = tk.Label(window, text="User 2 ID:")
label_user2.pack()
entry_user2 = tk.Entry(window)
entry_user2.pack()

# Create the button to check friendship
button_check = tk.Button(window, text="Check Friendship", command=check_friends)
button_check.pack()

# Create the label to display the result
label_result = tk.Label(window, text="")
label_result.pack()

# Start the main event loop
window.mainloop()
