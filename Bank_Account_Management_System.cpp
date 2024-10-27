#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <ctime>
#include <limits>
#include <algorithm>

using namespace std;

// Forward declarations
class Account;
class Transaction;
class Bank;

// Transaction class to store transaction history
class Transaction {
private:
    string type;
    double amount;
    double balanceAfter;
    string timestamp;

public:
    Transaction(string type, double amount, double balanceAfter)
        : type(type), amount(amount), balanceAfter(balanceAfter) {
        time_t now = time(0);
        timestamp = ctime(&now);
        timestamp.pop_back(); // Remove newline character
    }

    // Getter methods
    string getType() const { return type; }
    double getAmount() const { return amount; }
    double getBalanceAfter() const { return balanceAfter; }
    string getTimestamp() const { return timestamp; }
};

// Account class to manage individual accounts
class Account {
private:
    static int nextAccountNumber;
    int accountNumber;
    string accountHolder;
    double balance;
    string pin;
    vector<Transaction> transactions;

public:
    Account(string holder, string pin)
        : accountHolder(holder), balance(0.0), pin(pin) {
        accountNumber = nextAccountNumber++;
    }

    // Getter methods
    int getAccountNumber() const { return accountNumber; }
    string getAccountHolder() const { return accountHolder; }
    double getBalance() const { return balance; }

    bool verifyPin(const string& inputPin) const {
        return pin == inputPin;
    }

    bool deposit(double amount) {
        if (amount <= 0) return false;
        
        balance += amount;
        transactions.push_back(Transaction("Deposit", amount, balance));
        return true;
    }

    bool withdraw(double amount) {
        if (amount <= 0 || amount > balance) return false;
        
        balance -= amount;
        transactions.push_back(Transaction("Withdrawal", amount, balance));
        return true;
    }

    void displayTransactionHistory() const {
        cout << "\nTransaction History for Account #" << accountNumber << endl;
        cout << string(60, '-') << endl;
        cout << left << setw(20) << "Date/Time"
             << left << setw(12) << "Type"
             << right << setw(12) << "Amount"
             << right << setw(16) << "Balance" << endl;
        cout << string(60, '-') << endl;

        for (const auto& transaction : transactions) {
            cout << left << setw(20) << transaction.getTimestamp()
                 << left << setw(12) << transaction.getType()
                 << right << setw(12) << fixed << setprecision(2) << transaction.getAmount()
                 << right << setw(16) << transaction.getBalanceAfter() << endl;
        }
        cout << string(60, '-') << endl;
    }
};

// Static member initialization
int Account::nextAccountNumber = 1001;

// Bank class to manage all accounts
class Bank {
private:
    vector<Account> accounts;

    void clearScreen() {
        #ifdef _WIN32
            system("cls");
        #else
            system("clear");
        #endif
    }

    void waitForEnter() {
        cout << "\nPress Enter to continue...";
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

public:
    void createAccount() {
        clearScreen();
        cout << "\n=== Create New Account ===" << endl;
        
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        
        string name, pin;
        cout << "Enter account holder name: ";
        getline(cin, name);

        while (true) {
            cout << "Enter 4-digit PIN: ";
            getline(cin, pin);
            
            if (pin.length() == 4 && all_of(pin.begin(), pin.end(), ::isdigit)) {
                break;
            }
            cout << "Invalid PIN. Please enter exactly 4 digits." << endl;
        }

        Account account(name, pin);
        accounts.push_back(account);

        cout << "\nAccount created successfully!" << endl;
        cout << "Your account number is: " << account.getAccountNumber() << endl;
        waitForEnter();
    }

    Account* findAccount(int accountNumber) {
        for (auto& account : accounts) {
            if (account.getAccountNumber() == accountNumber) {
                return &account;
            }
        }
        return nullptr;
    }

    void performTransaction(bool isDeposit) {
        clearScreen();
        cout << "\n=== " << (isDeposit ? "Deposit" : "Withdrawal") << " ===" << endl;

        int accountNumber;
        string pin;
        double amount;

        cout << "Enter account number: ";
        cin >> accountNumber;

        Account* account = findAccount(accountNumber);
        if (!account) {
            cout << "Account not found!" << endl;
            waitForEnter();
            return;
        }

        cout << "Enter PIN: ";
        cin >> pin;

        if (!account->verifyPin(pin)) {
            cout << "Incorrect PIN!" << endl;
            waitForEnter();
            return;
        }

        cout << "Enter amount: $";
        cin >> amount;

        bool success;
        if (isDeposit) {
            success = account->deposit(amount);
        } else {
            success = account->withdraw(amount);
        }

        if (success) {
            cout << "\nTransaction successful!" << endl;
            cout << "New balance: $" << fixed << setprecision(2) << account->getBalance() << endl;
        } else {
            cout << "\nTransaction failed!" << endl;
            if (!isDeposit) {
                cout << "Insufficient funds or invalid amount." << endl;
            } else {
                cout << "Invalid amount." << endl;
            }
        }
        waitForEnter();
    }

    void checkBalance() {
        clearScreen();
        cout << "\n=== Check Balance ===" << endl;

        int accountNumber;
        string pin;

        cout << "Enter account number: ";
        cin >> accountNumber;

        Account* account = findAccount(accountNumber);
        if (!account) {
            cout << "Account not found!" << endl;
            waitForEnter();
            return;
        }

        cout << "Enter PIN: ";
        cin >> pin;

        if (!account->verifyPin(pin)) {
            cout << "Incorrect PIN!" << endl;
            waitForEnter();
            return;
        }

        cout << "\nAccount Holder: " << account->getAccountHolder() << endl;
        cout << "Current Balance: $" << fixed << setprecision(2) << account->getBalance() << endl;
        
        account->displayTransactionHistory();
        waitForEnter();
    }

    void displayMenu() {
        while (true) {
            clearScreen();
            cout << "\n=== Bank Account Management System ===" << endl;
            cout << "1. Create New Account" << endl;
            cout << "2. Deposit" << endl;
            cout << "3. Withdraw" << endl;
            cout << "4. Check Balance" << endl;
            cout << "5. Exit" << endl;
            cout << "\nEnter your choice (1-5): ";

            int choice;
            cin >> choice;

            if (cin.fail()) {
                cin.clear();
                cin.ignore(numeric_limits<streamsize>::max(), '\n');
                continue;
            }

            switch (choice) {
                case 1:
                    createAccount();
                    break;
                case 2:
                    performTransaction(true);  // deposit
                    break;
                case 3:
                    performTransaction(false); // withdraw
                    break;
                case 4:
                    checkBalance();
                    break;
                case 5:
                    cout << "\nThank you for using our banking system!" << endl;
                    return;
                default:
                    cout << "\nInvalid choice. Please try again." << endl;
                    waitForEnter();
            }
        }
    }
};

int main() {
    Bank bank;
    bank.displayMenu();
    return 0;
}