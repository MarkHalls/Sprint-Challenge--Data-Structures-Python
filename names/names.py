import time

start_time = time.time()

f = open("names_1.txt", "r")
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open("names_2.txt", "r")
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        def find_insert(current_node, value):
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BinarySearchTree(value)
                    return
                else:
                    return find_insert(current_node.left, value)
            else:
                if current_node.right is None:
                    current_node.right = BinarySearchTree(value)
                    return
                else:
                    return find_insert(current_node.right, value)

        find_insert(self, value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        def search(current_node, target):
            if current_node.value == target:
                return True
            if target < current_node.value:
                if current_node.left is not None:
                    return search(current_node.left, target)
            if target >= current_node.value:
                if current_node.right is not None:
                    return search(current_node.right, target)

            return False

        return search(self, target)


bst = BinarySearchTree("")

for name_2 in names_2:
    bst.insert(name_2)


for name_1 in names_1:
    if bst.contains(name_1):
        duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
