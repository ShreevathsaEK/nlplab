public class EXP11 {
    public static int CBigram(String[] corpus, String w1, String w2) {
        int count = 0;
        for (String sentence : corpus) {
            String[] words = sentence.split(" ");
            for (int i = 0; i < words.length - 1; i++) {
                if (w1.equalsIgnoreCase(words[i]) && w2.equalsIgnoreCase(words[i + 1])) {
                    count++;
                }
            }
        }
        return count;
    }

    public static int Cuni(String[] corpus, String w1) {
        int count = 0;
        for (String sentence : corpus) {
            String[] words = sentence.split(" ");
            for (int i = 0; i < words.length; i++) {
                if (w1.equalsIgnoreCase(words[i])) {
                    count++;
                }
            }
        }
        return count;
    }

    public static void main(String[] args) {
        String[] corpus = {
            "There is a big garden",
            "Children play in a garden",
            "They play inside a beautiful garden"
        };
        String[] tw = "They play inside a big garden".split(" ");
        double prob = 1.0;
        int cz = 9;  // size of the vocabulary (number of unique words in the corpus)

        for (int i = 0; i < tw.length - 1; i++) {
            int bc = CBigram(corpus, tw[i], tw[i + 1]);
            int uc = Cuni(corpus, tw[i]);
            double sp= (double) (bc +1)/(uc+cz);
            System.out.printf(" BC of ('%s' and '%s') is %d %n", tw[i], tw[i + 1], bc);
            prob *= sp;
        }
        System.out.printf("Probability is %.8f %n", prob);
    }
}
