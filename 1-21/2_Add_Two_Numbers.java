/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int jin=0;
    	ListNode res = null;
    	ListNode l3 = new ListNode(0);
    	while(l1!=null||l2!=null){
    		if(l1==null) l1 = new ListNode(0);
    		if(l2==null) l2 = new ListNode(0);
    		int sum = l1.val + l2.val + jin;
    		if (sum >= 10){
    			l3.next = new ListNode(sum - 10);
    			jin = 1;
    		}else{
    			l3.next = new ListNode(sum);
    			jin = 0;
    		}
    		if (res == null ){
    			res = l3;
    		}
    		l1=l1.next;
    		l2=l2.next;
    		l3=l3.next;
    	}
    	if(jin==1){
    		l3.next = new ListNode(1);
    	}
		return res.next;
        
    }
}