public class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        int[] sortnums = nums;
		Arrays.sort(sortnums);
		List<List<Integer>> result = new ArrayList<List<Integer>>();	
		for(int i=0;i<nums.length-3;i++){
			int a=sortnums[i];
			if(i!=0&&sortnums[i-1]==a) continue;
			int target2 = target-a;
			for(int z=i+1;z<nums.length-2;z++){
				int j=z+1,k=nums.length-1;
				int b=sortnums[z];
				
				int target3 = target2-b;
				while(j<k){
					List<Integer> alist = new ArrayList<Integer>();
					if(sortnums[j]+sortnums[k]>target3) k--;
					else if(sortnums[j]+sortnums[k]<target3) j++;
					else if(sortnums[j]+sortnums[k]==target3){
						alist.add(sortnums[j]);alist.add(sortnums[k]);
						alist.add(b);alist.add(a);result.add(alist);
						j++;k--;
						while(j < k &&sortnums[j]==sortnums[j-1]){
							j++;
						}	
						while(j < k &&sortnums[k]==sortnums[k+1]){
							k--;
						}
					}	
				
				}
			while(z<nums.length-2&&sortnums[z+1]==b){ z++;}	
			}
		}
		return result;
    }
}