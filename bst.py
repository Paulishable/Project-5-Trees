global inorder_list
inorder_list = []
preorder_list = []
postorder_list = []


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    def size(self):
        the_count = 0
        global inorder_list
        inorder_list = []

        if self.root is None:
            return the_count

        a_list = self.inorder()
        the_count = len(a_list)
        return the_count

    def is_empty(self):
        if self.root is None:
            return True
        return False

    def height (self):
        node = self.root
        return self.height2(node)

    def height2(self, node):
        if node is None:
            return -1
        leftHeight = self.height2(node.left)
        rightHeight = self.height2(node.right)
        return 1 + max(leftHeight, rightHeight)

    def add_item(self, a_pair):
        node = Node(a_pair)
        # check to see if it is in the tree already
        this_node_in_tree = self.find_this_node_in_tree(node)
        if this_node_in_tree is not None:
            this_node_in_tree.key.count += 1

            return self
        else:
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

    def remove(self, item):
        pass

    def find(self, desired_key):
        if self.is_empty():
            raise ValueError("ValueError exception thrown")
        else:
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

            return None

    def find_this_node_in_tree(self, desired_node):
        if self.is_empty():
            return None
        else:
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
        global inorder_list
        inorder_list = []
        return self.inorder2(self.root)

    def inorder2(self, item):
        global inorder_list
        if item is None:
            return

        self.inorder2(item.left)
        inorder_list.append(item.key)
        self.inorder2(item.right)
        return inorder_list

    def preorder(self):
        global preorder_list
        preorder_list = []
        self.preorder2(self.root)
        return preorder_list

    def preorder2(self, node):
        # if node is None,return
        global preorder_list
        if node is None:
            return
        # print the current node
       # print(node.key, end=" ,")
        preorder_list.append(node.key)
        #print("pre from preorder ", pre_list)
        # traverse left subtree
        self.preorder2(node.left)

        # traverse right subtree
        self.preorder2(node.right)

        return preorder_list


    def postorder(self):
        global postorder_list
        postorder_list = []
        node = self.root
        self.postorder2(node)
        return postorder_list


    def postorder2(self, node):
        # if root is None return
        if node is None:
            return
        # traverse left subtree
        self.postorder2(node.left)
        # traverse right subtree
        self.postorder2(node.right)
        # traverse root
        print(node.key)
        postorder_list.append(node.key)
        return postorder_list

    def rebalance(self):
        pass