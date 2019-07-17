#!/usr/bin/env python
# @author:sq
# @time:2019/07/17

# %%


class BinaryTree(object):
    """ Binary Tree.
    Args:
        root: root node of the tree.

    """
    def __init__(self, root=None):
        self.root = root

    def pre_order_traversal(self):
        BinaryTree.__pre_order_traversal(self.root)
        print()

    @classmethod
    def __pre_order_traversal(cls, root):
        """ Pre order Traversal method.

        Args:
            root: root of the tree

        Returns: null

        """
        print(root.get_value(), end="  ")
        # handle the left child
        if root.left_node is not None:
            BinaryTree.__pre_order_traversal(root.left_node)
        # handle the right child
        if root.right_node is not None:
            BinaryTree.__pre_order_traversal(root.right_node)

    def in_order_traversal(self):
        BinaryTree.__in_order_traversal(self.root)
        print()

    @classmethod
    def __in_order_traversal(cls, root):
        """ In order traversal.

        Args:
            root: root of tree.

        Returns: null

        """
        # handle the left child
        if root.left_node is not None:
            BinaryTree.__in_order_traversal(root.left_node)
        print(root.get_value(), end="  ")

        # handle the right child
        if root.right_node is not None:
            BinaryTree.__in_order_traversal(root.right_node)

    def last_order_traversal(self):
        BinaryTree.__last_order_traversal(self.root)
        print()

    @classmethod
    def __last_order_traversal(cls, root):
        """ Last order traversal.

        Args:
            root: root of the tree.

        Returns:

        """
        # handle the left child
        if root.left_node is not None:
            cls.__last_order_traversal(root.left_node)
        # handle the right child
        if root.right_node is not None:
            cls.__last_order_traversal(root.right_node)
        print(root.get_value(), end="  ")
    
    def single_node(self):
        """
        
        """

# %%


class Node(object):
    """ Node class
    Args:
        value: value of node

    """
    def __init__(self, value=0):
        """ Construction method

        Args:
            value: value of node
        """
        self.value = value
        self.left_node = None
        self.right_node = None

    def get_value(self):
        """ Get method of value.

        Returns:
            value of node

        """
        return self.value

    def set_value(self, value):
        """ Set method.

        Args:
            value: value to set

        Returns: null

        """
        self.value = value
