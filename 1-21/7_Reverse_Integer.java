public class Solution {
    public int reverse(int x) {
        // if(x>=Integer.MAX_VALUE||x<=Integer.MIN_VALUE) return 0;
		long number = x ;
		long result = 0;
		if(x<0){
			number = -1*number;
		}
		while(number>=10){
			result += number%10;
			result *= 10;
			number = number / 10;
		}
		result += number;
		if (result>=Integer.MAX_VALUE) return 0;
		
		if(x<0){
			result = -1 * result;
		}
		return (int)result;
    }
}