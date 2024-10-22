from tree import Node

# sum 
def sum_tree(root):
    # if empty return 0
    if root is None:
        return 0
    # current + left and right subtree
    return root.key + sum_tree(root.left) + sum_tree(root.right)

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
        # case
        root = None
        values = [20, 8, 22, 4, 12, 10, 14]
        for value in values:
            root = insert(root, value)
        root.display()
        total_sum = sum_tree(root)
        print(f"The sum of all values ​​in the tree: {total_sum}")
    except (ValueError) as e:
        print(f'Something went wrong, {e}')
        sys.exit(0)
