class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def get_output(self):
        '''
        Print the output depending on the evaluated value.
        If the 0 <= value <= 999 the value is printed.
        If the value < 0, UNDERFLOW is printed.
        If the value > 999, OVERFLOW is printed.

        :return: None
        '''
        value = self.evaluate()
        if value > 999:
            print('OVERFLOW')
        elif value < 0:
            print('UNDERFLOW')
        else:
            print(value)


    def insert(self, data, bracketed):
        '''
        Insert operators and operands into the binary tree.

        :param data: Operator or operand as a tuple. E.g.: ('OPERAND', 34), ('OPERATOR', '+')
        :param bracketed: denote whether an operator is inside brackets or not. If the operator is inside brackets,
        we set bracketed as True.
        :return: self
        '''

        new_node = Node(data)

        if (data[0] == 'OPERATOR') :
            if (bracketed == True) :
                new_node.left = self.right
                self.right = new_node        
            elif (bracketed == False) :
                new_node.left = self
                self = new_node 
        elif (data[0] == 'OPERAND') :
            if (self.right == None) :
                self.right = new_node
            else :
                self.right.right = new_node 

        return self

    def evaluate(self):
        '''
        Process the expression stored in the binary tree and compute the final result.
        To do that, the function should be able to traverse the binary tree.

        Note that the evaluate function does not check for overflow or underflow.

        :return: the evaluated value
        '''

        if self.data[0] == 'OPERAND' :
            return self.data[1]
        elif self.data[0] == 'OPERATOR':
            left_value = self.left.evaluate()
            right_value = self.right.evaluate()
            operator = self.data[1]

            if operator == '+':
                return left_value + right_value
            elif operator == '-':
                return left_value - right_value            
            elif operator == '*':
                return left_value * right_value
            elif operator == '^':
                return left_value ** right_value
            

# 1+(2*3)+3^2          
root = Node(('OPERAND', 1))
root = root.insert(('OPERATOR', '+'), False)
root = root.insert(('OPERAND', 2), False)
root = root.insert(('OPERATOR', '*'), True)
root = root.insert(('OPERAND', 3), False)
root = root.insert(('OPERATOR', '+'), False)
root = root.insert(('OPERAND', 3), False)
root = root.insert(('OPERATOR', '^'), False)
root = root.insert(('OPERAND', 2), False)
root.get_output() 
# Should print 100


# 1+2*3+3^2
root = Node(('OPERAND', 1))
root = root.insert(('OPERATOR', '+'), False)
root = root.insert(('OPERAND', 2), False)
root = root.insert(('OPERATOR', '*'), False)
root = root.insert(('OPERAND', 3), False)
root = root.insert(('OPERATOR', '+'), False)
root = root.insert(('OPERAND', 3), False)
root = root.insert(('OPERATOR', '^'), False)
root = root.insert(('OPERAND', 2), False)
root.get_output()
# Should print 144


# -15-(99*10)
root = Node(('OPERAND',-15))
root = root.insert(('OPERATOR','-'),False)
root = root.insert(('OPERAND',99),False)
root = root.insert(('OPERATOR','*'),True)
root = root.insert(('OPERAND',10),False)
root.get_output()
# Should print UNDERFLOW