from topic6_AVL_tree import AVLTree, AVLNode
import random

class AVLTreeSum(AVLTree):
    @staticmethod
    def sum_node(node: AVLNode):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return node.key
        return node.key + AVLTreeSum.sum_node(node.left) + AVLTreeSum.sum_node(node.right)

    def get_sum(self):
        return AVLTreeSum.sum_node(self.root)


values = random.sample(range(1, 16), 15)
tree = AVLTreeSum()
tree.add_all(values)

print("Tree:", tree.root)
print("Sum value:", tree.get_sum())

