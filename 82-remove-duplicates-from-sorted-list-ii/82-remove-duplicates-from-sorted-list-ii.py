# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        prev_node = None
        new_head = None
        
        while curr_node is not None:
            curr_head = curr_node
            curr_val = curr_node.val
            cnt = 0
            
            while curr_node is not None and curr_node.val == curr_val:
                curr_node = curr_node.next
                cnt = cnt + 1
            if cnt > 1:
                if prev_node is not None:
                    prev_node.next = curr_node
            elif prev_node is None:
                    prev_node = curr_head
                    new_head = curr_head
            else:
                prev_node = prev_node.next
            
        return new_head
                