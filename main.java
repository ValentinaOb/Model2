import java.util.Scanner;
import java.util.Random;

public class main {

    public static void main(String[] args) {
        System.out.println("Ex: ");

        try (Scanner in = new Scanner(System.in)) {
            int a = in.nextInt();

            switch (a) {
                case 1:
                    main1(args);
                    break;
                case 2:
                    main2(args);
                    break;
                case 3:
                    main3(args);
                    break;
                case 4:
                    main4(args);
                    break;
            }
        }
    }

    public static int lan(double[] m, int n) {
        double p = 0;
        int stan = -1;
        double z = new Random().nextDouble();
        // System.out.println("Z: " + z);

        for (int i = 0; i < n; i++) {
            if (z >= p && z <= p + m[i]) {
                stan = i;
                break;
            }
            p += m[i];
            // System.out.println("P: " + p);
        }
        return stan;
    }

    public static void main1(String[] args) {
        double[][] m = { { 0, 1, 0, 0, 0, 0 }, { 0.2, 0, 0.8, 0, 0, 0, }, { 0, 0.4, 0, 0.6, 0, 0 },
                { 0, 0, 0.6, 0, 0.4, 0 }, { 0, 0, 0, 0.8, 0, 0.2 }, { 0, 0, 0, 0, 1, 0 } };

        int k = 1;
        double m1[] = new double[6];

        for (int i = 0; i < 20; i++) {

            for (int l = 0; l < 6; l++) {
                for (int j = 0; j < 6; j++) {
                    if (l == k) {
                        m1[j] = m[l][j];
                        // System.out.println(m1[j]);
                    }
                }
            }

            k = lan(m1, 6);
            System.out.println("Static: " + k);
        }
    }

    public static void main2(String[] args) {
        double[][] m = { { 0, 0.5, 0.5 }, { 0.25, 0.5, 0.25 }, { 0.25, 0.25, 0.5 } };

        int k = 0;
        double m1[] = new double[3];

        for (int i = 0; i < 20; i++) {

            for (int l = 0; l < 3; l++) {
                for (int j = 0; j < 3; j++) {
                    if (l == k) {
                        m1[j] = m[l][j];
                        // System.out.print(m[l][j] + " ");
                    }
                }
            }
            k = lan(m1, 3);
            System.out.println("Static: " + k);
        }
    }

    public static void main3(String[] args) {
        double[][] m = { { 1, 0, 0, 0 }, { 0.25, 0.35, 0.4, 0 }, { 0.25, 0, 0.35, 0.4 }, { 0, 0.25, 0, 0.75 } };

        int k = 1;
        double m1[] = new double[4];

        for (int i = 0; i < 10; i++) {

            for (int l = 0; l < 4; l++) {
                for (int j = 0; j < 4; j++) {
                    if (l == k) {
                        m1[j] = m[l][j];
                    }
                }
            }

            k = lan(m1, 4);
            System.out.println("Static: " + k);
        }

    }

    public static void main4(String[] args) {
        double[][] m = { { 1, 0, 0, 0 }, { 0.25, 0.35, 0.4, 0 }, { 0.25, 0, 0.35, 0.4 }, { 0, 0.25, 0, 0.75 } };

        int k = 3;
        double bankr = 0;
        double m1[] = new double[4];

        for (int j = 0; j < 25; j++) {
            for (int i = 0; i < 5; i++) {

                for (int l = 0; l < 4; l++) {
                    for (int p = 0; p < 4; p++) {
                        if (l == k) {
                            m1[p] = m[l][p];
                        }
                    }
                }

                k = lan(m1, 4);
                System.out.println("Static: " + k);
                if (k == 0)
                    bankr++;
            }
        }
        System.out.println("Bankr: " + bankr / 125);

    }

}
