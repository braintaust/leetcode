public class Solution {
    public List<String> letterCombinations(String digits) {
         
        char[] adigs  = digits.toCharArray();
		List<String> index = new ArrayList<String>();
		List<String> result = new ArrayList<String>();
		if(digits.length()<1) return result;
		for(int i=0;i<digits.length();i++){
			switch(adigs[i]){
			case '0':index.add(" ");continue;
			case '1':index.add(" ");continue;
			case '2':index.add("abc");continue;
			case '3':index.add("def");continue;
			case '4':index.add("ghi");continue;
			case '5':index.add("jkl");continue;
			case '6':index.add("mno");continue;
			case '7':index.add("qprs");continue;
			case '8':index.add("tuv");continue;
			case '9':index.add("wxyz");continue;
			}
		}
		StringBuffer temp = new StringBuffer();
		combination(0,0,adigs,index,temp,result); 
    	return result;
    }
    private void combination(int iofd,int iofc,char[] adigs,
			List<String> charList,StringBuffer temp,List<String> result) {
		if(iofd >= charList.size()) {
			result.add(temp.toString());
			return;
			}
		String s = charList.get(iofd);
		if(iofc > s.length()-1) return;
		temp.append(s.charAt(iofc));
		combination(iofd+1,0,adigs,charList,temp,result);
		temp.delete(iofd, iofd+1);
		combination(iofd,iofc+1,adigs,charList,temp,result);	
	}
}