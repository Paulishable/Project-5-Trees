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
        #line_1 = data_file.readline().replace("\n", "")
        #print(line_1)
        for line in data_file:
            any_punctuation = string.punctuation
            for char in line:
                if not char.isspace() and char not in any_punctuation:
                    this_char = Pair(char, 1)
                    the_tree = the_tree.add_item(this_char)
            print()

            the_list = the_tree.inorder()
            print(the_list)

            print("h is", the_tree.height())
            print("size is ", the_tree.size())

    # for line in data_file:
    #     line = line.strip()
    #     for char in line:
    #         print("-----------------", f"char: {char}\n")
    #
    data_file.close()


def main():
    """ Program kicks off here."""
    make_tree()


if __name__ == "__main__":
    main()
