"""
Project:
Author:
Course:
Date:

Description:

Lessons Learned:

"""
import string
from pathlib import Path
from string import whitespace, punctuation
from bst import BST, Node


class Pair:
    """ Encapsulate letter,count pair as a single entity.

    Realtional methods make this object comparable
    using built-in operators.
    """

    def __init__(self, letter, count=1):
        self.letter = letter
        self.count = count

    def __eq__(self, other):
        return self.letter == other.letter

    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'

    def __str__(self):
        return f'({self.letter}, {self.count})'


def make_tree():
    """ A helper function to build the tree.

    The test code depends on this function being available from main.
    :param: None
    :returns: A binary search tree
    """

    # NOTE:  digits first, followed by upper case letters  followed by lower case letters

    """main driver function - reads file and does all for each line in the file"""

    the_tree = BST()

    with open("around-the-world-in-80-days-3.txt", "r", encoding="utf-8") as data_file:
        for line in data_file:
            any_punctuation = string.punctuation
            for char in line:
                if not char.isspace() and char not in any_punctuation:
                    this_char = Pair(char, 1)
                    the_tree.add_item(this_char)
    # print()
    #
    print(the_tree.inorder())
    # # #
    # print(str(the_tree))  # prints out a graphic of the tree
    # # print("the height of the tree is: ", the_tree.height())
    # print("Is the tree balanced?", the_tree.check_balance())
    # print("size is", the_tree.size())
    #
    # print()
    # print("the OLD tree height is: ", the_tree.height())
    # the_tree.rebalance()
    # print("Is the tree balanced?", n.check_balance())
    # print(the_tree.size())
    # print(str(the_tree))  # prints out a graphic of the tree
    # print("the NEW tree size is: ", the_tree.size())
    # print("the NEW tree height is: ", the_tree.height())
    # print("Is the NEW tree balanced?", the_tree.check_balance())



    # a_root = the_tree.sorted_array_to_tree(the_tree.inorder())

    # the_tree.rebalance()
    # # new_tree.add_item(a_root)a_root
    #
    # print(the_tree.size())
    # print(str(the_tree))  # prints out a graphic of the tree
    # print("the NEW tree size is: ", the_tree.size())
    # print("the NEW tree height is: ", the_tree.height())
    # print("Is the NEW tree balanced?", the_tree.check_balance())
    #
    data_file.close()
    return the_tree


def main():
    """ Program kicks off here."""
    make_tree()


if __name__ == "__main__":
    main()
