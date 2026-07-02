# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #Listnode() creates a blank placeholder node
        #dummy never moves and job is to remember where the start of new list is
            #dummy helps figure out which list node is smaller and to put first
            #at the end, you return the correct start
            #so you can start with a pretend node and attach nodes to it from there
        #node is active pointer, start at dummy node, as I add elements you advance it forward
        dummy = node = ListNode()

        #iterating through a linked list is different from array, loop through the nodes with while loop
        #iterates as long as the loop's node is not "none", meaning there is nothing
        while list1 and list2: #this works because an object like ListNode evaluates to True it it exists, and None evaluates to False
            if list1.val <= list2.val:
                node.next = list1 #add node to new list    
                list1 = list1.next #move the lsit1 pointer forward after that
            else:
                node.next = list2
                list2 = list2.next
            #now, move the node after adding one so you can change the next node
            node = node.next
        
        #after reaching the end of one list, the OR operator evaluates from left to right and returns the first truth val it finds
        #it automatically picks the none empty one!
        node.next = list1 or list2

        #returns dummy not node bc node has reached end tail - you are returning last node
        #dummy here is the superficial one before the first node, and you are returning the node after dummy, the actual first item
        return dummy.next
         
