"""This is the Binary Search Tree Class (including Node Class"""

# global inorder_list

inorder_list = []
preorder_list = []
postorder_list = []
middle_value = 0
list_left = []
list_right = []
new_root: int = 0


def find_mid_value_in_list(a_list):
    """find_mid_value_in_list"""
    return a_list[len(a_list) // 2]


def the_left_half_of(a_list):
    """find the_left_half_of a list"""

    mid = len(a_list) // 2
    return a_list[0: mid]


def the_right_half_of(a_list):
    """find the_right_half_of a list"""

    mid = len(a_list) // 2
    return a_list[mid + 1: len(a_list)]


class Node:
    """defines the Node of the BST"""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

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
        node = self.root
        return self.height_subtree(node)

    def height_subtree(self, node):
        """calculate the height of a subtree"""
        if node is None:
            return -1
        left_height = self.height_subtree(node.left)
        right_height = self.height_subtree(node.right)
        return 1 + max(left_height, right_height)

    def add_item(self, a_pair):
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
        """remove a node from the BST using the key"""
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
                elif current_node.left is not None and current_node.right is None:  # Case 2
                    if parent is None:  # Node is root
                        self.root = current_node.left
                    elif parent.left is current_node:
                        parent.left = current_node.left
                    else:
                        parent.right = current_node.left
                    return  # Node found and removed
                elif current_node.left is None and current_node.right is not None:  # Case 2
                    if parent is None:  # Node is root
                        self.root = current_node.right
                    elif parent.left is current_node:
                        parent.left = current_node.right
                    else:
                        parent.right = current_node.right
                    return  # Node found and removed
                else:  # Case 3
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
                return current_item

            # Navigate to the left if the search key is
            # less than the node's key.
            elif desired_key < current_item.key:
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
            elif desired_key < current_item.key:
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
        global inorder_list
        inorder_list = []
        return self.inorder2(self.root)

    def inorder2(self, item):
        """perform inorder (needs function 'inorder')"""
        global inorder_list
        if item is None:
            return inorder_list

        self.inorder2(item.left)
        inorder_list.append(item.key)
        self.inorder2(item.right)
        return inorder_list

    def preorder(self):
        """perform preorder on BST (needs preorder2)"""
        global preorder_list
        preorder_list = []
        self.preorder2(self.root)
        return preorder_list

    def preorder2(self, node):
        """execute preorder from function (preorder)"""
        # if node is None,return
        global preorder_list
        if node is None:

            return preorder_list
        # print the current node
        # print(node.key, end=" ,")
        preorder_list.append(node.key)
        # print("pre from preorder ", pre_list)
        # traverse left subtree
        self.preorder2(node.left)

        # traverse right subtree
        self.preorder2(node.right)

        return preorder_list

    def postorder(self):
        """perform postorder and return a list to calling function (needs postorder2)"""
        node = self.root
        self.postorder2(node)
        return postorder_list

    def postorder2(self, node):
        """perform postorder and return a list to calling function (postorder)"""
        # if root is None return
        if node is None:
            return None
        # traverse left subtree
        self.postorder2(node.left)
        # traverse right subtree
        self.postorder2(node.right)
        # traverse root
        # print(node.key)
        postorder_list.append(node.key)
        return postorder_list

    # def rebalance(self):
    #     global inorder_list, middle_value, list_right, list_left, new_root
    #
    #     inorder_list = []
    #     inorder_list = self.inorder()
    #     list_left = the_left_half_of(inorder_list)
    #     list_right = the_right_half_of(inorder_list)
    #     new_node = find_mid_value_in_list(inorder_list)
    #     self.__init__()
    #
    #     self.add_item(new_node)
    #     self.rebalance_self()

    # def rebalance_self(self):
    #     global inorder_list, middle_value, list_right, list_left
    #
    #     print("len(list_left)", len(list_left))
    #     print("len(list_right", len(list_right))
    #
    #     if len(list_left) <= 0 or len(list_right) <= 0:
    #         return
    #
    #     print("list_left", list_left)
    #     print("list_right", list_right)
    #     new_node = find_mid_value_in_list(list_left)
    #     self.add_item(new_node)
    #
    #     new_node = find_mid_value_in_list(list_right)
    #     self.add_item(new_node)
    #
    #     list_left = the_left_half_of(list_left)
    #     list_right = the_right_half_of(list_left)
    #
    #     print("list_left", list_left)
    #     print("list_right", list_right)
    #
    #     self.rebalance_self()

    def __repr__(self):
        return repr(self.root)

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
        rheight = self.height_subtree(node.right)

        # if difference in height is greater than 1, return False
        if abs(l_height - rheight) > 1:
            return False
        # check if left subtree is balanced
        l_check = self.check_balance_helper(node.left)
        # check if right subtree is balanced
        r_check = self.check_balance_helper(node.right)

        # if both subtree are balanced, return True
        return bool(l_check and r_check)

    def rebalance(self):
        """rebuild a BST with a sorted array or list"""
        an_arr = self.inorder()
        self.__init__()
        self.sorted_array_to_tree(an_arr)
        return self

    # function to convert sorted array to a
    # balanced BST
    # input : sorted array of integers
    # output: root node of balanced BST
    def sorted_array_to_tree(self, arr):
        """Convert a sortd array or list to a BST"""
        if not arr:
            return None

        # find middle
        mid = (len(arr)) // 2

        # make the middle element the root
        root = Node(arr[mid])
        self.add_node(root)

        # left subtree of root has all
        # values <arr[mid]
        root.left = self.sorted_array_to_tree(arr[:mid])

        # right subtree of root has all
        # values >arr[mid]
        root.right = self.sorted_array_to_tree(arr[mid + 1:])
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
