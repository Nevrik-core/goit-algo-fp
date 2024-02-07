class LinkedList:
    def __init__(self):
        self.head = None


    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self, h):
        if h is None or h.next is None:
            return h
        middle = self.get_middle(h)
        next_to_middle = middle.next
        middle.next = None
        left = self.merge_sort(h)
        right = self.merge_sort(next_to_middle)
        sorted_list = self.merge(left, right)
        return sorted_list

    def get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, a, b):
        result = None
        if a is None:
            return b
        if b is None:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.merge(a.next, b)
        else:
            result = b
            result.next = self.merge(a, b.next)
        return result

    def start_merge_sort(self):
        self.head = self.merge_sort(self.head)

    def merge_sorted_lists(self, llist):
        self.head = self.merge(self.head, llist.head)

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
