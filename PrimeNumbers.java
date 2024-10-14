import java.util.Scanner;

public class PrimeNumbers {

    // Function to check if a number is prime
    public static boolean isPrime(int num) {
        if (num <= 1) return false; // 0 and 1 are not prime numbers
        for (int i = 2; i <= Math.sqrt(num); i++) { // Check for factors up to the square root of num
            if (num % i == 0) return false; // If divisible, it's not prime
        }
        return true; // If no factors found, it's prime
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the limit to find prime numbers: ");
        int limit = scanner.nextInt(); // Read the limit from user input

        System.out.println("Prime numbers up to " + limit + ":");
        for (int num = 2; num <= limit; num++) { // Iterate from 2 to the limit
            if (isPrime(num)) { // Check if num is prime
                System.out.print(num + " "); // Print the prime number
            }
        }
        System.out.println(); // Print a new line at the end
        scanner.close(); // Close the scanner
    }
}
