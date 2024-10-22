from tree import Node 

# minimum
def find_min_value(root):
    # minimum value will be in left side
    current = root
    while current.left is not None:
        current = current.left
    return current.key

# insert
def insert(node, key):
    # if empty return instance
    if node is None:
        return Node(key)
    # else -> recursion
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

# Main
if __name__ == '__main__':
    try:
        root = None
        values = [20, 8, 22, 4, 12, 10, 14]
        for value in values:
            root = insert(root, value)
        root.display()
        min_value = find_min_value(root)
        print(f"The minimal value is : {min_value}")
    except (ValueError) as e:
        print(f'Something went wrong, {e}')
        sys.exit(0)

