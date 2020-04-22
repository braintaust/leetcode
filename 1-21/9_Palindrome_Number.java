public class Solution {
    public boolean isPalindrome(int x) {
        if(x>=Integer.MAX_VALUE||x<=Integer.MIN_VALUE) return false;
        long number = x;
		long result = 0;
		if(x<0){
		    return false;
		}
		while(number>=10){
			result += number%10;
			result *= 10;
			number = number/10;
		}
		result += number;
		return (result == x)?true:false;  
    }
}