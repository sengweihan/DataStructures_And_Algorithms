class BinarySearchTreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def add_child(self, data):

        if self.data < data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
        elif self.data > data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            #  if equal then dont need to add anything because binary search tree cannot have any duplicates element.
            return

    def inorder_traversal(self):
        element = []
        # visit left tree
        if self.left:
            element += self.left.inorder_traversal()

        # visit base node
        element.append(self.data)

        # visit right tree
        if self.right:
            element += self.right.inorder_traversal()

        return element

    def search(self, value):
        if self.data == value:
            return True

        elif self.data > value:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_max(self):
        # finds minimum element in entire binary tree
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def calculate_sum(self):
        sum = 0
        # visit left tree
        if self.left:
            sum += self.left.calculate_sum()

        # visit base node
        sum += self.data

        # visit right tree
        if self.right:
            sum += self.right.calculate_sum()

        return sum

    def post_order_traversal(self):
        element = []
        if self.left:
            element += self.left.post_order_traversal()

        if self.right:
            element += self.right.post_order_traversal()

        element.append(self.data)

        return element

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def delete_node(self, data):
        """
        THREE CASES FOR DELETION OF NODE IN A BINARY SEARCH TREE.
        CASE 1: IF THE NODE WE WANTED TO DELETE IS A LEAF, THEN WE CAN JUST SET PARENT REFERENCE TO NONE. (EASY)
        CASE 2: IF THE NODE WE WANT TO DELETE HAS ONE CHILD, THEN WE CAN JUST PROMOTE THE CHILD TO TAKE THE PLACE OF ITS PARENT. (EASY)
        CASE 3: IF THE NODE WE WANT TO DELETE HAS TWO CHILD, THEN WE CAN TAKE THE MIN OF THE NODE FROM THE RIGHT SUBTREE OF THE PARENT.
        """

        #  we need to first traverse down the tree.
        if data > self.data:
            if self.right:
                self.right = self.right.delete_node(data)
        elif data < self.data:
            if self.left:
                self.left = self.left.delete_node(data)
        else:
            # if we found the node we want to delete.
            if self.right == None and self.left == None:
                return None
            if self.left == None:
                return self.right
            if self.right == None:
                return self.left

            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete_node(min_value)

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [15, 12, 27, 7, 14, 20, 88, 23]

    root = build_tree(numbers)
    print(root.inorder_traversal())
    print(root.delete_node(15))
    print(root.inorder_traversal())
    # print(root.post_order_traversal())
