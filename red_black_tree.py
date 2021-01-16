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
        return


    def search(self,value):
        if self.head == None:
            return False
        return self.__searching(value, self.head)


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
            return True
            




if __name__ == "__main__":
    tree = RedBlackTree()
    tree.insert(10)
    print(tree.bfs())
    tree.insert(18)
    print(tree.bfs())
    tree.insert(7)
    print(tree.bfs())
    tree.insert(15)
    print(tree.bfs())
    tree.insert(16)
    print(tree.bfs())
    tree.insert(30)
    print(tree.bfs())
    tree.insert(25)
    print(tree.bfs())
    tree.insert(40)
    print(tree.bfs())
    tree.insert(60)
    print(tree.bfs())
    tree.insert(2)
    print(tree.bfs())
    tree.insert(1)
    print(tree.bfs())
    tree.insert(70)
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