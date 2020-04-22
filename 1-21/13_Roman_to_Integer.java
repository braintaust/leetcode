public class Solution {
    public int romanToInt(String s) {
        char[] c= s.toCharArray();
		int index = 0;
		int result= 0;
		while(index<=s.length()-1){
			switch(c[index]){
			case 'M': result+=1000;index++; break;
			case 'D': result+=500;index++; break;
			case 'C':if(index+1>s.length()-1)
						result+=100;
			         else if(c[index+1]=='D'||c[index+1]=='M')
						result-=100; 
					 else result+=100;
					  index++;
					  break;
			case 'L': result+=50; index++;break;
			case 'X':if(index+1>s.length()-1)
						result+=10;
					 else if(c[index+1]=='L'||c[index+1]=='C')
						result-=10; 
					  else{result+=10;}
					  index++;
					  break;
			case 'V': result+=5;index++;break;
			case 'I':if(index+1>s.length()-1)
						result+=1;
					 else if(c[index+1]=='V'||c[index+1]=='X')
						result-=1; 
					  else result+=1;
			          index++;
			          break;
			}			
		}
		return result;
    }
}