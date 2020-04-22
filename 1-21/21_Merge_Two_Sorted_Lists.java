/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode list = new ListNode(0);
        ListNode p = list;
        while(true){
            if(l1 == null|| l2 == null){
                if(l1 != null){
                    p.next = l1;
                }
                if(l2 != null){
                   p.next = l2;
                }
                break;
            }
            if(l1.val <= l2.val){
                ListNode temp = l1.next;
                p.next = l1;
                p = p.next;
                p.next = null;
                l1 = temp;
            }else{
                ListNode temp = l2.next;
                p.next = l2;
                p = p.next;
                p.next = null;
                l2 = temp;
            }
        }
        return list.next;
    }
}