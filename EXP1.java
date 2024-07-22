public class EXP1{
    public static int CBigram(String[] corpus, String w1, String w2){
        int count=0;
        for (String sentence : corpus){
            String[] words=sentence.split(" ");
            for(int i=0;i<(words.length-1);i++){
                if(w1.equalsIgnoreCase(words[i]) && w2.equalsIgnoreCase(words[i+1])){
                    count++;
                }
            }
        }
        return count;
    }
    public static int Cuni(String[] corpus, String w1){
        int count=0;
        for (String sentence : corpus){
            String[] words=sentence.split(" ");
            for(int i=0;i<words.length;i++){
                if(w1.equalsIgnoreCase(words[i])){
                    count++;
                }
            }
        }
        return count;
    }



    public static void main(String[] args){
        String[] corpus={
            "There is a big garden",
            "Children play in a garden",
            "They play inside a buetiful garden"
        };
        String[] tw="They play inside a big garden".split(" ");
        double prob=1;
        int cz=9;
        for(int i=0;i<tw.length-1;i++){
            int bc=CBigram(corpus, tw[i], tw[i+1]);
            int uc=Cuni(corpus, tw[i]);
            System.out.printf(" BC of ('%s and %s') is %d %n",tw[i],tw[i+1],bc);
            prob *= (double)bc/(uc+cz);

        }
        System.out.printf("Probability is %.8f %n",prob);
    }


}
