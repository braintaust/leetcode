public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
		int[] sortnums = nums;
		Arrays.sort(sortnums);
		
		List<List<Integer>> result = new ArrayList<List<Integer>>();
		for(int i=0;i<nums.length-2;i++){
			int a=sortnums[i];
			if(i!=0&&sortnums[i-1]==a) continue;
			int j=i+1,k=nums.length-1;
			while(j<k){
				List<Integer> alist = new ArrayList<Integer>();
				if(sortnums[j]+sortnums[k]>-a) k--;
				else if(sortnums[j]+sortnums[k]<-a) j++;
				else if(sortnums[j]+sortnums[k]==-a){
					alist.add(sortnums[j]);alist.add(sortnums[k]);
					alist.add(a);result.add(alist);
					j++;k--;
					while(j < k &&sortnums[j]==sortnums[j-1]){
						j++;
					}
					while(j < k &&sortnums[k]==sortnums[k+1]){
						k--;
					}
				}
				
			}
		}
		return result;
    }
}