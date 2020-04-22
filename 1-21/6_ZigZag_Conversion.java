public class Solution {
    public String convert(String s, int numRows) {
        int row = numRows;
		char[] a,b=new char[s.length()];
		int index=0;
		a = s.toCharArray();
		if(row ==1){
			return s;
		}
		for(int i = 0; i<row ;i++){
			for(int j = i; j<a.length; j+=2*(row-1)){
				b[index++] = a[j];
				//System.out.print(a[j]);
				if(i<row-1&&i>0&&a.length>j+2*(row-1-i)){
					b[index++] = a[j+2*(row-1-i)];
					//System.out.print(a[j+2*(row-1-i)]);
				}
				
			}
		}
		return String.valueOf(b); 
    }
}