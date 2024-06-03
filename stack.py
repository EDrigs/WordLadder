import copy
class Stack:
    """
    Class Stack implements a conceptual stack and its associated methods
    """
    def __init__(self):
        """
        Constructor function for stack
        :param: None
        :returns: None
        """
        self.data = []

    def push(self,item):
        """
        Item is appended or "pushed" to the list of data that will be used as a stack
        :param item: The item to be appended
        :return: None
        """
        self.data.append(item)

    def pop(self):
        """
        The most recent data appended to the stack is retrieved
        :param: None
        :return: The most recently appended data from the list
        """
        return self.data.pop()

    def __str__(self):
        """
        String override function for Stack
        :param: None
        :return: A string representation of the data in the stack
        """
        return str(self.data)

    def __repr__(self):
        """
        Creates string representation of the stack object
        :param: None
        :return: String representation of stack object
        """
        return str(self)

    def size(self):
        """
        Indicates the size of the stack data/list length
        :param: None
        :return: The length of the data list in Stack
        """
        return len(self.data)

    def is_empty(self):
        """
        Affirms whether the list for Stack is empty or not
        :param: None
        :return: Boolean value for an empty list or not
        """
        return self.data == []

    def peek(self):
        """
        Allows one to see the most recent value in the stack
        :param: None
        :return: The most recently appended item in the list for Stack
        """
        return self.data[-1]

    #return a deep copy of this Stack
    def clone(self):
        """
        Creates another Stack object completely independent of the original object
        :param: None
        :return: A new object with the identical data from the original Stack
        """
        s = Stack()
        s.data = copy.deepcopy(self.data)
        return s