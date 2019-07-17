#!/usr/bin/env python
# @author:sq
# @time:2019/07/17

from TreeTest import BinaryTree
from TreeTest import Node
# %%


def main():
    root = Node(5)
    layer1_1 = Node(3)
    layer1_2 = Node(7)
    layer2_1 = Node(2)
    layer2_2 = Node(4)
    layer2_3 = Node(6)
    layer2_4 = Node(8)
    layer1_1.left_node = layer2_1
    layer1_1.right_node = layer2_2
    layer1_2.left_node = layer2_3
    layer1_2.right_node = layer2_4
    root.left_node = layer1_1
    root.right_node = layer1_2
    binary_tree = BinaryTree(root)
    binary_tree.pre_order_traversal()
    binary_tree.in_order_traversal()
    binary_tree.last_order_traversal()


if __name__ == "__main__":
    main()
