from topic6_AVL_tree import AVLTree, AVLNode
import random

class AVLTreeMinMax(AVLTree):
    @staticmethod
    def min_value_node(node: AVLNode):
        current = node
        while current.left is not None:
            current = current.left
        return current

    @staticmethod
    def max_value_node(node: AVLNode):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def get_min_value(self):
        return AVLTreeMinMax.min_value_node(self.root).key

    def get_max_value(self):
        return AVLTreeMinMax.max_value_node(self.root).key


values = random.sample(range(1, 51), 50)
tree = AVLTreeMinMax()
tree.add_all(values)

print("Min value:", tree.get_min_value())
print("Max value:", tree.get_max_value())

