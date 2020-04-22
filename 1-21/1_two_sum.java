import java.util.HashMap;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int component;
		int[] result = null;
		HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
		for(int i=0; i<nums.length;i++){
				component = target - nums[i];
				if (map.containsKey(component)){
					result = new int[]{i,map.get(component)}; 
					break;
				}
				map.put(nums[i],i);
		}
		return 	result;
    }
}