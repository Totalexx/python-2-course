from binarytree import tree, Node

my_tree = tree(7)
right_list = [my_tree.left.left.value, my_tree.left.left.right.value,
              my_tree.left.left.right.left.value,my_tree.left.left.right.left.right.value]
wrong_list = [1, 8, 16, 100]


def tryFind(tree: Node, list):
    if len(list) == 0:
        return True

    startNode = findListStart(tree, list[0])

    if startNode is None:
        return False

    if len(list) == 1:
        return True

    return tryFindNext(list, 1, startNode.right) or tryFindNext(list, 1, startNode.left)


def tryFindNext(list, index, node):
    if node is None:
        return False

    if node.value != list[index]:
        return False

    next_index = index + 1
    if len(list) == next_index:
        return True

    return tryFindNext(list, next_index, node.right) or tryFindNext(list, next_index, node.left)


def findListStart(tree: Node, start: int):
    if tree.value == start:
        return tree

    findInLeft = None
    if tree.left is not None:
        findInLeft = findListStart(tree.left, start)

    if findInLeft is not None:
        return findInLeft

    findInRight = None

    if tree.right is not None:
        findInRight = findListStart(tree.right, start)

    if findInRight is not None:
        return findInRight

    return None


print(my_tree)
print(tryFind(my_tree, right_list))
print(tryFind(my_tree, wrong_list))
