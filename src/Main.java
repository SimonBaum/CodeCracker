// program to solve a vignere chiffre with a known password length
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        int passwordLength;
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter password length:");
        passwordLength = Integer.parseInt(sc.nextLine());

        System.out.println("Enter encrypted text:");
        String encText = sc.nextLine().toUpperCase() ;
        encText = encText.replaceAll("[^a-zA-Z]", "").trim();

        System.out.println(encText);

        sc.close();
    }


}