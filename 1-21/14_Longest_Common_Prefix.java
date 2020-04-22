public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length<1) return "";
    	int row=0;
        int colunm;
        int minleng=Integer.MAX_VALUE;
        String temp ="";
        for(int i=0;i<strs.length;i++){
        	if(minleng>strs[i].length()){
        		minleng = strs[i].length();
        		row = i;
        	}
        }
        temp = strs[row];
                
        for(colunm=0;colunm<=minleng-1;colunm++){
        	boolean flag = true;
        	for(row=1;row<strs.length;row++){
	        	if(strs[row].charAt(colunm)!=strs[row-1].charAt(colunm)){
	        		flag = false;
	        		break;
	        	}
	        }
        	if(!flag){
        		temp = temp.substring(0, colunm);
        		break;
        	}
        }
        
    	return temp;
    }
}