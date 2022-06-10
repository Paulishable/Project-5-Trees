"""This is the Binary Search Tree Class (including Node Class"""


class Node:
    """defines the Node of the BST"""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def add_left_child(self, node):
        """add a left child for completeness"""
        self.left = node

    def add_right_child(self, node):
        """add a right child for completeness"""
        self.right = node

    def __repr__(self):
        lines = []
        if self.right:
            found = False
            for line in repr(self.right).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " ┌─" + line
                elif found:
                    line = " | " + line
                else:
                    line = "   " + line
                lines.append(line)
        lines.append(str(self.key))
        if self.left:
            found = False
            for line in repr(self.left).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " └─" + line
                elif found:
                    line = "   " + line
                else:
                    line = " | " + line
                lines.append(line)
        return "\n".join(lines)


class BST:
    """class definition for the BST"""

    def __init__(self):
        self.root = None

    def __repr__(self):
        return repr(self.root)

    def size(self):
        """calculate the BST size"""
        the_count = 0
        #        inorder_list = []

        if self.root is None:
            return the_count

        a_list = self.inorder()
        the_count = len(a_list)
        return the_count

    def is_empty(self):
        """return true if the tree is empty"""
        if self.root is None:
            return True
        return False

    def height(self):
        """calculate the total height of the tree"""
        # height for this project is node based, not edge based
        # function 'height_subtree' calculates 'edge based' height
        # add 1 for node based
        node_based_height = True
        node = self.root
        height = self.height_subtree(node)
        if node_based_height:
            height += 1
        return height

    def height_subtree(self, node):
        """calculate the height of a subtree"""
        # calculates height based on edges
        if node is None:
            return -1
        left_height = self.height_subtree(node.left)
        right_height = self.height_subtree(node.right)
        return 1 + max(left_height, right_height)

    def add(self, a_pair):
        """create a node from an item of the 'Pair' class and add it to the BST"""
        node = Node(a_pair)
        # check to see if it is in the tree already
        this_node_in_tree = self.find_this_node_in_tree(node)
        if this_node_in_tree is not None:
            this_node_in_tree.key.count += 1
            return self
        # Check if the tree is empty
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None:
                if node.key < current_node.key:
                    # If there is no left child, add the new
                    # node here; otherwise repeat from the
                    # left child.
                    if current_node.left is None:
                        current_node.left = node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    # If there is no right child, add the new
                    # node here; otherwise repeat from the
                    # right child.
                    if current_node.right is None:
                        current_node.right = node
                        current_node = None
                    else:
                        current_node = current_node.right
        return self

    def remove(self, key):
        """remove a node from the BST using the key which is a Pair class item"""
        parent = None
        current_node = self.root

        # Search for the node.
        while current_node is not None:

            # Check if current_node has a matching key.
            if current_node.key == key:
                if current_node.left is None and current_node.right is None:  # Case 1
                    if parent is None:  # Node is root
                        self.root = None
                    elif parent.left is current_node:
                        parent.left = None
                    else:
                        parent.right = None
                    return  # Node found and removed

                if current_node.left is not None and current_node.right is None:  # Case 2
                    if parent is None:  # Node is root
                        self.root = current_node.left
                    elif parent.left is current_node:
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
                    return  # Node found and removed

                if current_node.left is None and current_node.right is not None:  # Case 2
                    if parent is None:  # Node is root
                        self.root = current_node.right
                    elif parent.left is current_node:
                        parent.left = current_node.right
                    else:
                        parent.right = current_node.right
                    return  # Node found and removed

                # Case 3
                # Find successor (leftmost child of right subtree)
                successor = current_node.right
                while successor.left is not None:
                    successor = successor.left
                current_node.key = successor.key  # Copy successor to current node
                parent = current_node
                current_node = current_node.right  # Remove successor from right subtree
                key = parent.key  # Loop continues with new key

            elif current_node.key < key:  # Search right
                parent = current_node
                current_node = current_node.right
            else:  # Search left
                parent = current_node
                current_node = current_node.left

        return  # Node not found

    def find(self, desired_key):
        """find the node related to a key in the BST"""
        if self.is_empty():
            raise ValueError("ValueError exception thrown")

        current_item = self.root
        while current_item is not None:
            # Return the node if the key matches.
            if current_item.key == desired_key:
                return current_item.key

            # Navigate to the left if the search key is
            # less than the node's key.
            if desired_key < current_item.key:
                current_item = current_item.left

            # Navigate to the right if the search key is
            # greater than the node's key.
            else:
                current_item = current_item.right

        # The key was not found in the tree.
        raise ValueError("ValueError exception thrown")

    def find_this_node_in_tree(self, desired_node):
        """see if the desired_node is already in the tree"""
        if self.is_empty():
            return None
        desired_key = desired_node.key
        current_item = self.root
        while current_item is not None:
            # Return the node if the key matches.
            if current_item.key == desired_key:
                return current_item

            # Navigate to the left if the search key is
            # less than the node's key.
            if desired_key < current_item.key:
                current_item = current_item.left

            # Navigate to the right if the search key is
            # greater than the node's key.
            else:
                current_item = current_item.right

        # The key was not found in the tree.
        # raise ValueError("ValueError exception thrown")

        return None

    def inorder(self):
        """initiate inorder pass (needs function inorder2)"""
        inorder_list = []
        return self.inorder2(self.root, inorder_list)

    def inorder2(self, item, inorder_list):
        """perform inorder (needs function 'inorder')"""
        if item is None:
            return inorder_list

        self.inorder2(item.left, inorder_list)
        inorder_list.append(item.key)
        self.inorder2(item.right, inorder_list)
        return inorder_list

    def preorder(self):
        """perform preorder on BST (needs preorder2)"""
        preorder_list = []
        self.preorder2(self.root, preorder_list)
        return preorder_list

    def preorder2(self, node, preorder_list):
        """execute preorder from function (preorder)"""
        if node is None:
            return preorder_list
        # print the current node
        # print(node.key, end=" ,")
        preorder_list.append(node.key)
        # print("pre from preorder ", pre_list)
        # traverse left subtree
        self.preorder2(node.left, preorder_list)

        # traverse right subtree
        self.preorder2(node.right, preorder_list)

        return preorder_list

    def postorder(self):
        """perform postorder and return a list to calling function (needs postorder2)"""
        node = self.root
        postorder_list = []
        self.postorder2(node, postorder_list)
        return postorder_list

    def postorder2(self, node, postorder_list):
        """perform postorder and return a list to calling function (postorder)"""
        # if root is None return
        if node is None:
            return None
        # traverse left subtree
        self.postorder2(node.left, postorder_list)
        # traverse right subtree
        self.postorder2(node.right, postorder_list)
        # traverse root
        # print(node.key)
        postorder_list.append(node.key)
        return postorder_list

    def check_balance(self):
        """return True if the BST is balanced"""
        return self.check_balance_helper(self.root)

    def check_balance_helper(self, node):
        """Helper to check the balance of a BST (driven by the function 'check_balance'"""
        # if tree is empty,return True
        if node is None:
            return True
        # check height of left subtree
        l_height = self.height_subtree(node.left)
        r_height = self.height_subtree(node.right)

        # if difference in height is greater than 1, return False
        if abs(l_height - r_height) > 1:
            return False
        # check if left subtree is balanced
        l_check = self.check_balance_helper(node.left)
        # check if right subtree is balanced
        r_check = self.check_balance_helper(node.right)

        # if both subtree are balanced, return True
        return bool(l_check and r_check)

    def rebalance(self):
        """rebuild a BST with a sorted array or list"""
        lyst = self.inorder()
        self.__init__()
        self.rebalance_helper(lyst)
        return self

    def rebalance_helper(self, lyst):
        """Convert a sortd array or list to a BST"""
        if not lyst:
            return None

        center_index = (len(lyst)) // 2

        root = Node(lyst[center_index])
        self.add_node(root)

        left_list = lyst[:center_index]
        right_list = lyst[center_index + 1:]

        root.left = self.rebalance_helper(left_list)
        root.right = self.rebalance_helper(right_list)

        return root

    def add_node(self, node):
        """given a ---'node'---, add it to the BST"""
        # check to see if it is in the tree already
        this_node_in_tree = self.find_this_node_in_tree(node)
        if this_node_in_tree is not None:
            this_node_in_tree.key.count += 1
            return self
        # Check if the tree is empty
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while current_node is not None:
                if node.key < current_node.key:

                    # If there is no left child, add the new
                    # node here; otherwise repeat from the
                    # left child.
                    if current_node.left is None:
                        current_node.left = node
                        current_node = None
                    else:
                        current_node = current_node.left
                else:
                    # If there is no right child, add the new
                    # node here; otherwise repeat from the
                    # right child.
                    if current_node.right is None:
                        current_node.right = node
                        current_node = None
                    else:
                        current_node = current_node.right
        return self
