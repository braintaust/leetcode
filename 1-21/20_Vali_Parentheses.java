public class Solution {
    public boolean isValid(String s) {
       //boolean result = true;
       Stack<Character> sk = new Stack<Character>();
       char[] schar = s.toCharArray();
       for(int i=0;i<schar.length;i++){
            if(schar[i]=='('||schar[i]=='['||schar[i]=='{'){
               sk.push(schar[i]); 
            }
            if(schar[i]==')'||schar[i]==']'||schar[i]=='}'){
                if(sk.empty()){
                    return false;
                }
                char temp = sk.pop();
                switch(temp){
                    case '(':temp=')';break;
                    case '[':temp=']';break;
                    case '{':temp='}';break;
                }
                if(schar[i]!=temp){
                    return false;
                }
            }
       }
       if(sk.empty()){
        return true;
       }else{
           return false;
       }
    }
}