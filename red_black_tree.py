class RedBlackTree:
    def __init__(self):
        pass

    def insert(self,value):
        return

    def remove(self,value):
        return

    def search(self,value):
        return bool

    def path(self,value):
        return

    def min(self):
        return

    def max(self):
        return

    def bfs(self):
        return

    def __rotate(self):
        None

class Node:
    def __init__(self):
        self.value = None
        self.color = None
        self.left_child = None
        self.right_child = None
        self.parent = None

    def get_value(self):
        return self.value

    def get_color(self):
        return self.color

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def get_parent(self):
        return self.parent

    def get_sibling(self):
        if self == self.get_parent().get_left_child():
            return self.get_parent().get_right_child()
        else:
            return self.get_parent().get_left_child()

    def set_color(self, color):
        self.color = color

    def set_value(self, value):
        self.value = value

    def set_right_child(self, right_child):
        self.right_child = right_child

    def set_left_child(self, left_child):
        self.left_child = left_child

    def set_parent(self, parent):
        self.parent = parent




    def list_convert(self):
        return [self.value, self.color, self.left_child, self.right_child]