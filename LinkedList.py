# |========================================================|
# |    Title:      Linked List.py                          |
# |    Author:     Drake G. Cummings                       |
# |    Purpose:    Creating a Linked List                  |
# |    Date:       February 19th, 2021                     |
# |========================================================|

class LinkedList:
    # Members
    head = None
    count = 1

    # Constructor
    def __init__(self, nodeValue):
        self.head = Node(nodeValue)

    # Class Utilites
    def __str__(self):
        printout = ""
        node = self.head
        while node is not None:

            # Add to printout string depending on if it's the first
            if printout == "":
                printout += f"{node.value}"
            else:
                printout += f" -> {node.value}"

            # Change node to next in line
            node = node.next
        return printout

    # Methods
    def append_left(self, value):
        # Create new node
        newHead = Node(value)
        # Assign new node's next to head
        newHead.next = self.head
        # Set new node as head
        self.head = newHead
        self.count = self.count + 1

    def append_right(self, value):
        tail = self.get_tail()
        # Set tail's next to new node
        tail.next = Node(value)
        self.count = self.count + 1

    def pop_left(self):
        self.head = self.head.next
        self.count = self.count - 1

    def pop_right(self):
        # Get length of linked list
        count = 1
        node = self.head
        while node.next is not None:
            node = node.next
            count += 1

        # Get second-to-last node
        node = self.head
        for x in range(0, count - 2):
            node = node.next

        # Nullify node's next
        node.next = None
        self.count = self.count - 1

    def contains(self, value):
        # Check head
        node = self.head
        if node.value == value:
            return True

        # Check the rest
        while node.next is not None:
            node = node.next
            if node.value == value:
                return True

        return False

    def get_tail(self):
        # Search for node without a next node
        node = self.head
        while node.next is not None:
            node = node.next

        return node

    def reverse(self):
        """
        Method to reverse a link list. Takes no parameters.
        """
        nodes = []
        # Reference first node and add it to list
        head = self.head
        node = head
        nodes.append(node)
        # Cycle through other nodes and add them
        while node.next is not None:
            node = node.next
            nodes.append(node)
        # Reverse list
        nodes = nodes[::-1]

        # Reset all "next" members
        for i in range(len(nodes)):
            if i != self.count-1:
                nodes[i].next = nodes[i+1]
            else:
                nodes[i].next = None

        # Set new head value
        self.head = nodes[0]

        # Uncomment to see new next values of nodes
        # for i in nodes:
        #     print(f"{i}'s next value is {i.next}")
    """
    This method takes the tail node and sets its next to the head node
    """
    def make_circular(self):
        tail = self.get_tail()
        tail.next = self.head

    """
    This GENIUS algorithm detects patterns in a linked list. Truly incredible.
    """
    def tortoise_and_hare(self):
        count = 1
        tortiose = self.head
        hare = self.head

        # Start both tortiose and hare at index 0
        while hare is not None:
            # Increase tortiose by one
            tortiose = tortiose.next
            # Increase hare by two
            if hare.next is not None and hare.next.next is not None:
                hare = hare.next.next
            else:
                return print("No pattern found")

            # Print values
            print(f"tortiose: {tortiose.value} hare: {hare.value}")

            # Check if values are the same
            if tortiose.value == hare.value:
                print("values match!")
                # If so, reset tortiose to head node
                tortiose = self.head

                # Make sure hare doesn't equal None
                while hare.next is not None:
                    print(f"tortiose: {tortiose.value} hare: {hare.value}")
                    # If values are same, the first repetition is found
                    if tortiose.value == hare.value:
                        print("First repetition found!")

                        # Send Hare to tortiose next to find pattern length
                        hare = tortiose.next
                        space = 0
                        while hare.value != tortiose.value:
                            hare = hare.next
                            space += 1
                        # Print start and spacing
                        summary = f"First repetition starts at index {count} "
                        summary += (f"and is {space} long")
                        return print(summary)

                    # Otherwise increment
                    else:
                        tortiose = tortiose.next
                        hare = hare.next

                # If none are found, return
                return

            # If tortiose does not equal hare, continue through the linekd list
            else:
                count += 1

        return print("No patterns found")

    """
    This method tests to see if the linked list eventually points back to
    the head node
    """
    def is_circular(self):
        node = self.head.next
        for x in range(0, self.count):
            if node is self.head:
                return print("Linked list is circular!")
            else:
                if node.next is not None:
                    node = node.next
                else:
                    return print("Linked list is not circular")

    """
    This method tests if the linked list is circular at every node, seeing if a
    cycle exists among them.
    """
    def is_lollipop(self):
        # Set to main node
        firstNode = self.head

        # Test for circles starting at every node
        for x in range(1, self.count):
            # Set node to current starting position
            for y in range(0, x):
                if firstNode.next is not None:
                    firstNode = firstNode.next
                else:
                    return print("Linked list is linear")

            # Set test node to after first node
            node = firstNode.next
            for j in range(0, self.count-x):
                if node is firstNode:
                    return print("Linked list is a lollipop!")
                else:
                    if node.next is not None:
                        node = node.next
        return print("Linked list is not a lollipop")


class Node:
    # Members
    value = None
    next = None

    # Methods
    def __init__(self, _nodeValue):
        self.value = _nodeValue
        self.next = None

    def __repr__(self):
        return f"Value: {self.value}"
