public class Solution {
    public String intToRoman(int num) {
        Stack<String> s = new Stack<String>();
			StringBuffer sb =new StringBuffer();
			int index=0;
			int number = num;
			while(number>0){
				int n=number%10;
				switch(n){
				case (1):
					switch(index){
					case(0):s.push("I"); break;
					case(1):s.push("X"); break;
					case(2):s.push("C"); break;
					case(3):s.push("M"); break;
					} break;
				case (2): 
					switch(index){
					case(0):s.push("II"); break;
					case(1):s.push("XX"); break;
					case(2):s.push("CC"); break;
					case(3):s.push("MM"); break;
					} break;
				case (3): 
					switch(index){
					case(0):s.push("III"); break;
					case(1):s.push("XXX"); break;
					case(2):s.push("CCC"); break;
					case(3):s.push("MMM"); break;
					} break;
				case (4): 
					switch(index){
					case(0):s.push("IV"); break;
					case(1):s.push("XL"); break;
					case(2):s.push("CD"); break;
					} break;
				case (5): 
					switch(index){
					case(0):s.push("V"); break;
					case(1):s.push("L"); break;
					case(2):s.push("D"); break;
					} break;
				case (6): 
					switch(index){
					case(0):s.push("VI"); break;
					case(1):s.push("LX"); break;
					case(2):s.push("DC"); break;
					} break;
				case (7): 
					switch(index){
					case(0):s.push("VII"); break;
					case(1):s.push("LXX"); break;
					case(2):s.push("DCC"); break;
					} break;
				case (8): 
					switch(index){
					case(0):s.push("VIII"); break;
					case(1):s.push("LXXX"); break;
					case(2):s.push("DCCC"); break;
					} break;
				case (9): 
					switch(index){
					case(0):s.push("IX"); break;
					case(1):s.push("XC"); break;
					case(2):s.push("CM"); break;
					} break;
				default: s.push("");
				}
				number=number/10;
				index++;
			}
			while(s.size()>0){
				sb.append(s.pop());
			}
			return sb.toString();
    }
}