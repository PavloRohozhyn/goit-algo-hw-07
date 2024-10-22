from tree import Node

# insert (for building)
def insert(node, key):
    # if tree is empty return 
    if node is None:
        return Node(key)
    # else -> recursion
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node



# max value
def find_max_value(root):
    # max value will be on the right side (node)
    current = root
    while current.right is not None:
        current = current.right
    return current.key

# Main
if __name__ == '__main__':
    try:
        # case
        root = None
        values = [20, 8, 22, 4, 12, 10, 14]
        for value in values:
            root = insert(root, value)
        root.display()
        max_value = find_max_value(root)
        print(f"The max value is : {max_value}")
    except (ValueError) as e:
        print(f'Something went wrong, {e}')
        sys.exit(0)
