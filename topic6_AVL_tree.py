class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, prefix="Root: ", indent=""):
        ret = prefix + str(self.key) + "\n"
        children = []
        if self.left:
            children.append(("L: ", self.left))
        if self.right:
            children.append(("R: ", self.right))
        for i, (label, child) in enumerate(children):
            is_last = (i == len(children) - 1)
            connector = "└── " if is_last else "├── "
            extension = "    " if is_last else "│   "
            ret += child.__str__(indent + connector + label, indent + extension)
        return ret

class AVLTree:
    @staticmethod
    def get_balance(node: AVLNode):
        if not node:
            return 0
        return AVLTree.get_height(node.left) - AVLTree.get_height(node.right)

    @staticmethod
    def get_height(node):
        if not node:
            return 0
        return node.height

    @staticmethod
    def left_rotate(z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(AVLTree.get_height(z.left), AVLTree.get_height(z.right))
        y.height = 1 + max(AVLTree.get_height(y.left), AVLTree.get_height(y.right))

        return y

    @staticmethod
    def right_rotate(y):
        x = y.left
        T3 = x.right

        x.right = y
        y.left = T3

        y.height = 1 + max(AVLTree.get_height(y.left), AVLTree.get_height(y.right))
        x.height = 1 + max(AVLTree.get_height(x.left), AVLTree.get_height(x.right))

        return x

    @staticmethod
    def insert(root, key):
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = AVLTree.insert(root.left, key)
        elif key > root.key:
            root.right = AVLTree.insert(root.right, key)
        else:
            return root

        root.height = 1 + max(AVLTree.get_height(root.left), AVLTree.get_height(root.right))

        balance = AVLTree.get_balance(root)

        if balance > 1:
            if key < root.left.key:
                return AVLTree.right_rotate(root)
            else:
                root.left = AVLTree.left_rotate(root.left)
                return AVLTree.right_rotate(root)

        if balance < -1:
            if key > root.right.key:
                return AVLTree.left_rotate(root)
            else:
                root.right = AVLTree.right_rotate(root.right)
                return AVLTree.left_rotate(root)

        return root

    def __init__(self):
        self.root: AVLNode or None = None

    def add(self, key):
        self.root = AVLTree.insert(self.root, key)

    def add_all(self, keys):
        for key in keys:
            self.add(key)

