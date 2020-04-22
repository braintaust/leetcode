/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode p1 = head;  
	     ListNode p2 = head;  
	     ListNode removeNode = head;  
	     int i = 0;  
	     while(p1!=null){  
	         p1 = p1.next;  
	         i++;  
	         if(i > n){  
	             p2 = removeNode;  
	             removeNode = removeNode.next;  
	         }  
	     }
	     if(removeNode == head){  
	         head = head.next;  
	     }else{  
	         p2.next = removeNode.next;  
	     }  
	        return head;  
    }
}