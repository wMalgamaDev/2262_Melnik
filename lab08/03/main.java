public class Main {
    public static void main(String[] args) {
        int[] zero = new int[2];
        int[][] vec2 = {
                { 1, 2, 3 },
                { 4, 0, 1 },
                { 2, 3, 4 }
        };
        flag: for (int i = 0; i < vec2.length; i++) {
            for (int j = 0; j < vec2[i].length; j++) {
                if (vec2[i][j] == 0) {
                    zero[0] = i;
                    zero[1] = j;
                    break flag;
                }
            }
        }
        System.out.println(zero[0] + " " + zero[1]);
    }
}
