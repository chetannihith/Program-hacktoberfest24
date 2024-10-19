#include <iostream>
using namespace std;

int main() {
    int limit;
    cout << "Enter the limit for the Fibonacci series: ";
    cin >> limit;

    int a = 0, b = 1; // Starting values
    cout << "Fibonacci Series up to " << limit << ": ";

    while (a <= limit) {
        cout << a << " ";
        int next = a + b; // Calculate the next Fibonacci number
        a = b; // Update a to the next number in the series
        b = next; // Update b to the next number in the series
    }
    cout << endl;

    return 0;
}

