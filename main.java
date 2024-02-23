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
            }
        }
    }

    public static void main1(String[] args) {
        double[][] m = { { 0, 1, 0, 0, 0, 0 }, { 0.2, 0, 0.8, 0, 0, 0, }, { 0, 0.4, 0, 0.6, 0, 0 },
                { 0, 0, 0.6, 0, 0.4, 0 }, { 0, 0, 0, 0.8, 0, 0.2 }, { 0, 0, 0, 0, 1, 0 } };

        int k = 0;
        double m1[] = new double[6];
        int sum = 0;
        for (int i = 0; i < 20; i++) {
            for (int l = 0; l < 6; l++)
                for (int j = 0; j < 6; j++) {
                    if (j == k)
                        m1[l] = m[l][j];
                }

            // for (int w = 0; w < 6; w++) {
            double z = new Random().nextDouble();
            if ((z < m1[0]) && (z > 0))
                sum += 0;
            if ((z > m1[0]) && (z < m1[0] + m1[1]))
                sum += 1;
            if ((z > m1[0] + m1[1]) && (z < m1[0] + m1[1] + m1[2]))
                sum += 2;
            if ((z > m1[0] + m1[1] + m1[2]) && (z < m1[0] + m1[1] + m1[2] + m1[3]))
                sum += 3;
            if ((z > m1[0] + m1[1] + m1[2] + m1[3]) && (z < m1[0] + m1[1] + m1[2] + m1[3] + m1[4]))
                sum += 4;
            if ((z > m1[0] + m1[1] + m1[2] + m1[3] + m1[4])
                    && (z < m1[0] + m1[1] + m1[2] + m1[3] + m1[4] + m1[5]))
                sum += 5;
            if ((z > m1[0] + m1[1] + m1[2] + m1[3] + m1[4] + m1[5]) && (z < 1))
                sum += 6;

            System.out.println("Sum: " + sum);
            k = sum;
            sum = 0;
            // }
        }
    }

    public static void main2(String[] args) {
        double[][] m = { { 0, 0.5, 0.5 }, { 0.25, 0.5, 0.25 }, { 0.25, 0.25, 0.5 } };

        int k = 0;
        double m1[] = new double[3];
        int sum = 0;
        for (int i = 0; i < 20; i++) {
            for (int l = 0; l < 3; l++)
                for (int j = 0; j < 3; j++) {
                    if (j == k)
                        m1[l] = m[l][j];
                }

            // for (int w = 0; w < 3; w++) {
            double z = new Random().nextDouble();
            if ((z < m1[0]) && (z > 0))
                sum += 0;
            if ((z > m1[0]) && (z < m1[0] + m1[1]))
                sum += 1;
            if ((z > m1[0] + m1[1]) && (z < m1[0] + m1[1] + m1[2]))
                sum += 2;
            if ((z > m1[0] + m1[1] + m1[2]) && (z < 1))
                sum += 3;

            System.out.println("Sum: " + sum);
            k = sum;
            sum = 0;
            // }
        }
    }

    public static void main3(String[] args) {
        double[][] m = { { 1, 0, 0, 0 }, { 0.25, 0.35, 0.4, 0 }, { 0.25, 0, 0.35, 0.4 }, { 0, 0.25, 0, 0.75 } };

        int k = 3;
        double bankr = 0;
        double m1[] = new double[4];
        int sum = 0;
        for (int i = 0; i < 5; i++) {
            for (int l = 0; l < 4; l++)
                for (int j = 0; j < 4; j++) {
                    if (j == k)
                        m1[l] = m[l][j];
                }

            // for (int w = 0; w < 4; w++) {
            double z = new Random().nextDouble();
            if ((z < m1[0]) && (z > 0))
                sum += 0;
            if ((z > m1[0]) && (z < m1[0] + m1[1]))
                sum += 1;
            if ((z > m1[0] + m1[1]) && (z < m1[0] + m1[1] + m1[2]))
                sum += 2;
            if ((z > m1[0] + m1[1] + m1[2]) && (z < m1[0] + m1[1] + m1[2] + m1[3]))
                sum += 3;
            if ((z > m1[0] + m1[1] + m1[2] + m1[3]) && (z < 1))
                sum += 3;

            System.out.println("Sum: " + sum);
            k = sum;
            if (sum == 0)
                bankr++;
            sum = 0;
            // }
        }
        System.out.println("Bankr: " + bankr / 5); // 20

    }

}
