from node import Node

import sys

class RedBlackTree:
    def __init__(self):
        self.head = None

    def load(self, array):
        #return [self.value, self.color, self.left_child, self.right_child]
        nodes = {}
        for i in range(len(array) - 1, -1, -1):
            new_node = Node(array[i][0])
            new_node.set_color(array[i][1])
            if array[i][2] != None:
                new_node.set_left_child(nodes[array[i][2]])
                nodes[array[i][2]].set_parent(new_node)
            if array[i][3] != None:
                new_node.set_right_child(nodes[array[i][3]])
                nodes[array[i][3]].set_parent(new_node)
                
            
            nodes[array[i][0]] = new_node
            if i == 0:
                self.head = new_node

    def insert(self,value):
        if self.head == None:
            self.head = Node(value)
            self.head.set_color("BLACK")

        else:
            inserted_node = self.__insert(value, self.head)
            if inserted_node == None or inserted_node.get_parent() == None or inserted_node.get_parent().get_parent() == None:
                return
            
            self.__recolor_rotate(inserted_node)
        

    def remove(self,value):
        if self.search(value) == True:
            node = self.__searching(value, self.head)

            self.__remove(node)

    def __remove(self, node):
        
        if node.get_left_child() != None and node.get_right_child() != None:
            n = node.get_right_child()
            while n.get_left_child() != None:
                    n = n.get_left_child()
            node.set_value(n.get_value())
            self.__remove(n)
            
        elif node.get_left_child() != None:
            n = node.get_left_child()
            while n.get_right_child() != None:
                    n = n.get_right_child()
            node.set_value(n.get_value())
            self.__remove(n)

        elif node.get_right_child() != None:
            n = node.get_right_child()
            while n.get_left_child() != None:
                    n = n.get_left_child()
            node.set_value(n.get_value())
            self.__remove(n)
            
        else:
            if node == self.head:
                self.head = None
            elif node.get_color() == "BLACK":
                self.__double_black(node)

            if node.is_right_child() == True:
                node.get_parent().set_right_child(None)
            else:
                node.get_parent().set_left_child(None)


    def __double_black(self, node):
        sibling = node.get_sibling()
        if sibling == None:
            pass
        elif sibling.get_color() == "BLACK":
            if (sibling.get_left_child() == None or sibling.get_left_child().get_color() == "BLACK") and (sibling.get_right_child() == None or sibling.get_right_child().get_color() == "BLACK"):
                #Case 3
                sibling.set_color("RED")

                if node.get_parent().get_color() == "BLACK" and node.get_parent() != self.head:
                    #Case 3.2
                    self.__double_black(node.get_parent())
                else:
                    #Case 3.1
                    node.get_parent().set_color("BLACK")
            else:
                if node.is_right_child() == True:
                    far_child = sibling.get_left_child()
                    close_child = sibling.get_right_child()
                else:
                    far_child = sibling.get_right_child()
                    close_child = sibling.get_left_child()
                    
                if close_child != None and (far_child == None or far_child.get_color() == "BLACK"):
                    #Case 5
                    close_child.set_color("BLACK")
                    sibling.set_color("RED")
                    if sibling.is_right_child() == True:
                        self.__rotate(sibling, "RIGHT")
                    else:
                        self.__rotate(sibling, "LEFT")
                    
                    self.__double_black(node)
                elif far_child != None and far_child.get_color() == "RED":
                    #Case 6
                    c = node.get_parent().get_color()
                    node.get_parent().set_color(sibling.get_color())
                    sibling.set_color(c)
                    if node.is_right_child() == True:
                        self.__rotate(node.get_parent(), "RIGHT")
                    else:
                        self.__rotate(node.get_parent(), "LEFT")
                    
                    far_child.set_color("BLACK")

        else:
            #Case 4
            c = node.get_parent().get_color()
            node.get_parent().set_color(sibling.get_color())
            sibling.set_color(c)
            if node.is_right_child() == True:
                self.__rotate(node.get_parent(), "RIGHT")
                if sibling.get_left_child() == None or sibling.get_left_child().get_color() == "BLACK":
                    pass
            else:
                self.__rotate(node.get_parent(), "LEFT")
                if sibling.get_right_child() == None or sibling.get_right_child().get_color() == "BLACK":
                    pass
            self.__double_black(node)

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
        
    def __recolor_rotate(self, node):
        while node != self.head and node.get_parent().get_color() == "RED":
            parent = node.get_parent()
            uncle = parent.get_sibling()
            if uncle != None:
                if uncle.is_right_child() == False: 
                    if uncle.get_color() == "RED":
                        uncle.set_color("BLACK")
                        parent.set_color("BLACK")
                        parent.get_parent().set_color("RED")
                        node = parent.get_parent()
                    else:
                        if node.is_right_child() == False:
                            node = parent
                            self.__rotate(node, "RIGHT")
                        
                        node.get_parent().set_color("BLACK")
                        node.get_parent().get_parent().set_color("RED")
                        self.__rotate(node.get_parent().get_parent(), "LEFT")

                else:
                    if uncle.get_color() == "RED":
                        uncle.set_color("BLACK")
                        parent.set_color("BLACK")
                        parent.get_parent().set_color("RED")
                        node = parent.get_parent()
                    else:
                        if node.is_right_child() == True:
                            node = parent
                            self.__rotate(node, "LEFT")
                        
                        node.get_parent().set_color("BLACK")
                        node.get_parent().get_parent().set_color("RED")
                        self.__rotate(node.get_parent().get_parent(), "RIGHT")
            else:
                if parent.is_right_child() == True:
                    if node.is_right_child() == False:
                        node = parent
                        self.__rotate(node, "RIGHT")
                    
                    node.get_parent().set_color("BLACK")
                    node.get_parent().get_parent().set_color("RED")
                    self.__rotate(node.get_parent().get_parent(), "LEFT")
                else:
                    if node.is_right_child() == True:
                        node = parent
                        self.__rotate(node, "LEFT")
                     
                    node.get_parent().set_color("BLACK")
                    node.get_parent().get_parent().set_color("RED")
                    self.__rotate(node.get_parent().get_parent(), "RIGHT")
            
        self.head.set_color("BLACK")

    def __rotate(self, child,  left_or_right):
        if left_or_right == "LEFT":
            right_child = child.get_right_child()
            child.set_right_child(right_child.get_left_child())
            if right_child.get_left_child() != None:
                right_child.get_left_child().set_parent(child)
            
            right_child.set_parent(child.get_parent())

            if child.get_parent() == None:
                self.head = right_child
            elif child.is_right_child() == False:
                child.get_parent().set_left_child(right_child)
            else:
                child.get_parent().set_right_child(right_child)

            right_child.set_left_child(child)
            child.set_parent(right_child)

        elif left_or_right == "RIGHT":
            left_child = child.get_left_child()
            child.set_left_child(left_child.get_right_child())
            if left_child.get_right_child() != None:
                left_child.get_right_child().set_parent(child)
            
            left_child.set_parent(child.get_parent())
            if child.get_parent() == None:
                self.head = left_child
            elif child.is_right_child() == True:
                child.get_parent().set_right_child(left_child)
            else:
                child.get_parent().set_left_child(left_child)

            left_child.set_right_child(child)
            child.set_parent(left_child)

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
            

    def print(self):
        self.__print_helper(self.head, "", True)

    def __print_helper(self, node, indent, last):
        # print the tree structure on the screen
        if node != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            print(str(node.get_value()) + "(" + node.get_color() + ")")
            self.__print_helper(node.get_left_child(), indent, False)
            self.__print_helper(node.get_right_child(), indent, True)

def jennys_tree(tree):
    nodes = [[10, "BLACK", 3, 30], [3, "BLACK", 1, 7], [30, "BLACK", 25, 40], [1, "BLACK", None, None], [7, "BLACK", None, None], [25, "RED", 20, 28], [40, "BLACK", None, None], [20, "BLACK", None, None], [28, "BLACK", None, None]]
    
    tree.load(nodes)
    tree.print()
    print(tree.bfs())

    tree.remove(1)
    tree.print()
    print(tree.bfs())

def jennys_tree2(tree):
    nodes = [[50, "BLACK", 30, 65], [30, "BLACK", 15, 35], [65, "BLACK", 55, 70], [15, "BLACK", None, None], [35, "BLACK", None, None], [55, "BLACK", None, None], [70, "RED", 68, 80], [68, "BLACK", None, None], [80, "BLACK", None, 90], [90, "RED", None, None]]

    tree.load(nodes)
    tree.print()
    print(tree.bfs())

    tree.remove(55)
    tree.print()
    print(tree.bfs())

    tree.remove(30)
    tree.print()
    print(tree.bfs())

    tree.remove(90)
    tree.print()
    print(tree.bfs())
    
    tree.remove(80)
    tree.print()
    print(tree.bfs())
    
    tree.remove(50)
    tree.print()
    print(tree.bfs())
    
    tree.remove(35)
    tree.print()
    print(tree.bfs())
    
    tree.remove(15)
    tree.print()
    print(tree.bfs())
    
    tree.remove(65)
    tree.print()
    print(tree.bfs())

    tree.remove(68)
    tree.print()
    print(tree.bfs())
    
    

if __name__ == "__main__":
    tree = RedBlackTree()
    
    jennys_tree2(tree)

    """
    tree.insert(10)
    tree.insert(7)
    tree.insert(20)
    tree.insert(30)
    tree.insert(25)
    tree.insert(2)
    tree.insert(12)
    tree.insert(11)
    #print(tree.bfs())
    tree.print()
    
    tree.remove(20)
    #print(tree.bfs())
    tree.print()

    tree.remove(7)
    tree.print()
    
    tree.remove(2)
    tree.print()
    """
    """
    print(tree.search(45))
    print(tree.search(27))
    print(tree.path(45))
    print(tree.path(40))
    print(tree.min())
    print(tree.max())
    print(tree.bfs())
    """