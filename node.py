
class Node:
    def __init__(self, value):
        self.value = value
        self.color = "RED"
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
        if self.left_child == None and self.right_child == None:
            return [self.value, self.color, self.left_child, self.right_child]

        elif self.left_child == None:
            return [self.value, self.color, self.left_child, self.right_child.get_value()]

        elif self.right_child == None: 
            return [self.value, self.color, self.left_child.get_value(), self.right_child]

        else:
            return [self.value, self.color, self.left_child.get_value(), self.right_child.get_value()]

    def is_right_child(self):
        if self == self.get_parent().get_right_child():
            return True
        return False

