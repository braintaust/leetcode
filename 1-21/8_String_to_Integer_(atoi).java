public class Solution {
    public int myAtoi(String str) {
    	int length = str.length();
		char[] a = str.toCharArray();
		int index = 0;
		boolean sign = true;
		long result = 0;
		if(length<=0){
			return 0;
		}
		while(index<length&&a[index] == ' '){
			index++;
		}
		if (index<length&&a[index] == '+'){
			index++;
		}
		else if(index<length&&a[index] == '-'){
			sign = false;
			index++;
		}
		for(int j=index ; j<length; j++){
			if(a[j]>='0'&&a[j]<='9'){
				result = result * 10 + (a[j]-'0');
			    if(result > Integer.MAX_VALUE){
				    result = sign?Integer.MAX_VALUE:Integer.MIN_VALUE;
				    break;
			    }
			}else{
				// result = 0;
				break;
			}	
		}
		result = sign?result:result*(-1);
		return (int)result;         
    }
}