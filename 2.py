# Obtain the digits of the linked list as strs to avoid 0 padding
# Add them as ints
# Create a new linked list with the sum


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l3 = ListNode(0, None)
        l1_str = ""
        l2_str = ""

        while True:
            l1_str = str(l1.val) + l1_str
            if l1.next is None:
                break
            l1 = l1.next

        while True:
            l2_str = str(l2.val) + l2_str
            if l2.next is None:
                break
            l2 = l2.next

        l3_value = int(l1_str) + int(l2_str)
        l3.val = l3_value % 10
        curr = l3
        while l3_value // 10 != 0:
            l3_value = l3_value // 10
            curr.next = ListNode(l3_value % 10)
            curr = curr.next

        return l3
