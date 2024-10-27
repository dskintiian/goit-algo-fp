class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __gt__(self, other):
        return self.data > other.data

    def __ge__(self, other):
        return self.data >= other.data

    def __lt__(self, other):
        return self.data < other.data

    def __le__(self, other):
        return self.data <= other.data

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return self.data != other.data

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        llist = []
        current = self.head
        while current:
            llist.append(current.data)
            # print(current.data)
            current = current.next

        print(llist)

def reverse(linked_list: LinkedList):
    reverse_nodes(linked_list.head, linked_list.head.next, linked_list)

def reverse_nodes(node1: Node, node2: Node, linked_list, i = 0):
    if node2.next is None:
        node2.next = node1
        linked_list.head = node2
        return

    reverse_nodes(node2, node2.next, linked_list, i+1)
    node2.next = node1
    if i == 0:
        node1.next = None

def insertion_sort(data: LinkedList):
    prev_node = data.head # before current
    current_node = data.head.next
    next_node = current_node.next # after current
    next_prev_node = prev_node.next # after prev

    while current_node:
        compare_node = data.head
        prev_compare_node = None # before compare
        print(f'current node: {current_node.data}')
        while current_node != compare_node:
            print(f'compare node: {compare_node.data}')
            if current_node < compare_node:
                print(f'current node is smaller than compare node: {current_node.data} < {compare_node.data}')
                prev_node.next = current_node.next
                next_prev_node = prev_node
                current_node.next = compare_node
                if prev_compare_node:
                    prev_compare_node.next = current_node
                else:
                    data.head = current_node

                print(data.head.data, data.head.next.data, data.head.next.next.data, data.head.next.next.next.data, data.head.next.next.next.next.data, data.head.next.next.next.next.next.data, data.head.next.next.next.next.next.next.data)

                # data.print_list()
                break
            else:
                print(f'current node is bigger than compare node: {current_node.data} > {compare_node.data}')

            prev_compare_node, compare_node = compare_node, compare_node.next

        current_node, next_node, prev_node, next_prev_node = next_node, next_node.next if next_node else None, next_prev_node, next_prev_node.next


linked_list = LinkedList()
linked_list.insert_at_beginning(5)
linked_list.insert_at_beginning(1)
linked_list.insert_at_beginning(3)
linked_list.insert_at_end(10)
linked_list.insert_at_beginning(6)
linked_list.insert_at_beginning(2)
linked_list.insert_at_beginning(4)
linked_list.insert_at_end(8)
linked_list.insert_at_end(9)
linked_list.insert_at_end(12)
linked_list.insert_at_beginning(7)
linked_list.insert_at_end(13)
linked_list.insert_at_end(11)

print('List:')
linked_list.print_list()

print('Reversed list:')
reverse(linked_list)
linked_list.print_list()

print('Sorted list:')
insertion_sort(linked_list)
linked_list.print_list()