from node import Node

class RedBlackTree:
    def __init__(self):
        self.head = None

    def insert(self,value):
        if self.head == None:
            self.head = Node(value)
            self.head.set_color("BLACK")
            return

        else:
            inserted_node = self.__insert(value, self.head)
            if inserted_node == None:
                return
            #if inserted_node.get_parent().get_color() != "BLACK":
            node = self.__recolor_check(inserted_node)
            print(tree.bfs())
            if node != None:
            #else:
                if node.is_right_child() == True and node.get_parent().is_right_child() == False:
                    self.__rotate(node, "LEFT")
                    self.__rotate(node, "LEFTLEFT")
                elif node.is_right_child() == False and node.get_parent().is_right_child() == True:
                    self.__rotate(node, "RIGHT")
                    self.__rotate(node, "RIGHTRIGHT")
                elif node.is_right_child() == True and node.get_parent().is_right_child() == True:
                    self.__rotate(node, "RIGHTRIGHT")

                """

                
                elif inserted_node.is_right_child() == False and inserted_node.get_parent().is_right_child() == False:
                    self.__rotate(inserted_node, "LEFTLEFT")
                """
            return
        

    def remove(self,value):
        if self.search(value) == True:
            node = self.__searching(value, self.head)
        #If node to delete is red

            if node.get_color() == "RED":
                #if node is end node
                if node.get_left_child() == None and node.get_right_child() == None:
                    if node.is_right_child() == True:
                        node.get_parent().set_right_child(None)
                    else:
                        node.get_parent().set_left_child(None)

                #if node has children
                elif node.is_right_child() == True:
                    node.get_parent().set_right_child(node.get_right_child())
                    right_child = node.get_right_child()
                    right_child.set_parent(node.get_parent())
                    while right_child.get_left_child() != None:
                        right_child = right_child.get_left_child()
                    right_child.set_left_child(node.get_left_child())
                    node.get_left_child().set_parent(right_child)
                else:
                    node.get_parent().set_left_child(node.get_left_child())
                    left_child = node.get_left_child()
                    left_child.set_parent(node.get_parent())
                    while left_child.get_right_child() != None:
                        left_child = left_child.get_right_child()
                    left_child.set_right_child(node.get_right_child())
                    node.get_right_child().set_parent(left_child)


            else:
                """
                node_color_first = node.get_color()
                if z.left == self.TNULL:
                    x = z.right
                    self.__rb_transplant(z, z.right)
                elif (z.right == self.TNULL):
                    x = z.left
                    self.__rb_transplant(z, z.left)
                else:
                    y = self.minimum(z.right)
                    y_original_color = y.color
                    x = y.right
                    if y.parent == z:
                        x.parent = y
                    else:
                        self.__rb_transplant(y, y.right)
                        y.right = z.right
                        y.right.parent = y

                    self.__rb_transplant(z, y)
                    y.left = z.left
                    y.left.parent = y
                    y.color = z.color
                if y_original_color == 0:
                    self.__remove(x)
                """

    def __remove(self, node):
        while node != self.head and node.color == "RED":
            if node.is_right_child != True:
                sibling = node.get_sibling()
                if sibling.get_color() == "RED":
                    sibling.set_color("BLACK")
                    node.get_parent().set_color("RED")
                    self.__rotate(node.get_parent(), "LEFT")
                    sibling = node.get_sibling()

                if sibling.get_left_child().get_color() == "BLACK" and sibling.get_right_child().get_color() == "BLACK":
                    sibling.set_color("RED")
                    node = node.get_parent()
                else:
                    if sibling.get_right_child().get_color()=="BLACK":
                        sibling.get_left_child().set_color("BLACK")
                        sibling.set_color("RED")
                        self.__rotate(sibling, "RIGHT")
                        sibling = node.get_sibling()

                    sibling.set_color(node.get_parent().get_color())
                    node.get_parent().set_color("BLACK")
                    sibling.get_right_child().set_color("BLACK")
                    self.__rotate(node.get_parent(), "RIGHT")
                    node = self.head
            else:
                sibling = node.get_sibling()
                if sibling.get_color() == "RED":
                    sibling.set_color("BLACK")
                    node.get_parent().set_color("RED")
                    self.__rotate(node.get_parent(),"RIGHT")
                    sibling = node.get_sibling()

                if sibling.get_right_child().get_color() == "BLACK":
                    sibling.set_color("RED")
                    node = node.get_parent()
                else:
                    if sibling.get_left_child().get_color() == "BLACK":
                        sibling.get_right_child().set_color("BLACK")
                        sibling.set_color("RED")
                        self.__rotate(sibling, "LEFT")
                        sibling = node.get_sibling()

                    sibling.set_color(node.get_parent().get_color())
                    node.get_parent().set_color("BLACK")
                    sibling.get_left_child().set_color("BLACK")
                    self.__rotate(node.get_parent(), "RIGHT")
                    node = self.head
        node.set_color("BLACK")

    def __rb_transplant(self, u, v):
        if u.get_parent() == None:
            self.head = v
        elif u.is_right_child() == False:
            u.get_parent().set_left_child(v) 
        else:
            u.get_parent().set_right_child(v)
        v.set_parent(u.get_parent)





    def search(self,value):
        if self.head == None:
            return False
        elif self.__searching(value, self.head) != False:
            return True
        else:
            return False


    def path(self,value):
        path_list = []
        if self.search(value) == False:
            return None
        else:
            return self.__pathing(value, self.head, path_list)


    def min(self):
        if self.head == None:
            return None

        else:
            head = self.head
            while head.get_left_child() != None:
                head = head.get_left_child()
            return head.get_value()


    def max(self):
        if self.head == None:
            return None

        else:
            head = self.head
            while head.get_right_child() != None:
                head = head.get_right_child()
            return head.get_value()


    def bfs(self):
        closed_list = []
        open_list = [self.head]
        while len(open_list) != 0:
            if open_list[0].get_left_child() != None:
                open_list.append(open_list[0].get_left_child())
            if open_list[0].get_right_child() != None:
                open_list.append(open_list[0].get_right_child())

            closed_list.append(open_list[0].list_convert())
            open_list.pop(0)

        return closed_list
        
    def __recolor_check(self, node):
        if node.get_parent() != None and node.get_parent().get_color() == "RED":
            parent = node.get_parent()
            if parent.get_sibling() != None and parent.get_sibling().get_color() == "RED":
                # Recolor
                parent.set_color("BLACK")
                parent.get_sibling().set_color("BLACK")
                
                # Check if parent's parent is not root
                grandparent = parent.get_parent()
                if grandparent != self.head:
                    if grandparent.get_color() == "RED":
                        grandparent.set_color("BLACK")
                    else:
                        grandparent.set_color("RED")

                    if grandparent.get_parent() != self.head:
                        return self.__recolor_check(parent)
                    else:
                        return None
            else:
                return node
        return None

    def __rotate(self, child,  left_or_right):
        if left_or_right == "LEFT":
            parent = child.get_parent()
            parentparent = child.get_parent().get_parent()
            parent.set_right_child(None)
            child.set_left_child(parent)
            parentparent.set_left_child(child)
            child.set_parent(parentparent)
            parent.set_parent(child)

        elif left_or_right == "RIGHT":
            parent = child.get_parent()
            parentparent = child.get_parent().get_parent()
            parent.set_left_child(None)
            child.set_right_child(parent)
            parentparent.set_right_child(child)
            child.set_parent(parentparent)
            parent.set_parent(child)

        elif left_or_right == "RIGHTRIGHT":
            parent = child.get_parent()
            parentparent = parent.get_parent()

            child.set_color("BLACK")
            parent.set_color("RED")
            
            if parentparent != None:
                if parent.is_right_child() == True:
                    parentparent.set_right_child(child)
                else:
                    parentparent.set_left_child(child)
            child.set_parent(parentparent)
            
            parent.set_parent(child)
            child.set_left_child(parent)
            parent.set_right_child(None)
            """
            child.get_parent().set_left_child(child.get_parent().get_parent())
            child.get_parent().get_parent().set_right_child(None)
            if child.get_parent().get_parent().get_parent() != None:
                if child.get_parent().get_parent().is_right_child() == True:
                    child.get_parent().set_parent(child.get_parent().get_parent().get_parent())
                    child.get_parent().get_parent().get_parent().set_right_child(child.get_parent())
            else: 
                child.get_parent().set_parent(None)
                self.head = child.get_parent()
                self.head.set_color("BLACK")
            """

        elif left_or_right == "LEFTLEFT":
            parent = child.get_parent()
            parentparent = parent.get_parent()

            child.set_color("BLACK")
            parent.set_color("RED")
            
            if parentparent != None:
                if parent.is_right_child() == True:
                    parentparent.set_right_child(child)
                else:
                    parentparent.set_left_child(child)
            child.set_parent(parentparent)

            parent.set_parent(child)
            child.set_right_child(parent)
            parent.set_left_child(None)

    def __insert(self,value, head):
        if value > head.get_value():
            if head.get_right_child() != None:
                return self.__insert(value, head.get_right_child())
            else:
                new_node = Node(value)
                head.set_right_child(new_node)
                new_node.set_parent(head)
                return new_node


        elif value < head.get_value(): 
            if head.get_left_child() != None:
                return self.__insert(value, head.get_left_child())
            else:
                new_node = Node(value)
                head.set_left_child(new_node)
                new_node.set_parent(head)
                return new_node
        
        elif value == head.get_value():  
            return None

    def __pathing(self, value, head, path_list):
        if value > head.get_value():
            if head.get_right_child() != None:
                path_list.append(head)
                self.__pathing(value, head.get_right_child(), path_list)
            else:
                path_list.append(head.get_value())

        elif value < head.get_value(): 
            if head.get_left_child() != None:
                path_list.append(head)
                self.__pathing(value, head.get_left_child(), path_list)
            else:
                path_list.append(head)

        elif value == head.get_value():
            path_list.append(head)  
        
        return path_list

        
    def __searching(self, value, head):
        if value > head.get_value():
            if head.get_right_child() != None:
                return self.__searching(value, head.get_right_child())
            else:
                return False
    

        elif value < head.get_value():
            if head.get_left_child() != None:
                return self.__searching(value, head.get_left_child())
            else:
                return False


        elif value == head.get_value():
            return head
            




if __name__ == "__main__":
    tree = RedBlackTree()
    tree.insert(10)
    tree.insert(7)
    tree.insert(20)
    tree.insert(30)
    print(tree.bfs())
    
    tree.remove(30)
    print(tree.bfs())

    """
    print(tree.search(45))
    print(tree.search(27))
    print(tree.path(45))
    print(tree.path(40))
    print(tree.min())
    print(tree.max())
    print(tree.bfs())
    """