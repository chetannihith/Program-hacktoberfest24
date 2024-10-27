#include <iostream>
#include <fstream>
#include <vector>
#include <string>

struct Student {
    int id;
    std::string name;
    int age;
    double grade;
};

void addStudent();
void displayStudents();
void updateStudent();

const std::string filename = "students.txt";

// Helper functions
void saveStudent(const Student &student);
std::vector<Student> loadStudents();
void saveAllStudents(const std::vector<Student> &students);

int main() {
    int choice;
    do {
        std::cout << "\n--- Student Management System ---\n";
        std::cout << "1. Add Student\n";
        std::cout << "2. Display Students\n";
        std::cout << "3. Update Student\n";
        std::cout << "4. Exit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                addStudent();
                break;
            case 2:
                displayStudents();
                break;
            case 3:
                updateStudent();
                break;
            case 4:
                std::cout << "Exiting...\n";
                break;
            default:
                std::cout << "Invalid choice! Please try again.\n";
        }
    } while (choice != 4);

    return 0;
}

void addStudent() {
    Student student;
    std::cout << "\n--- Add Student ---\n";
    std::cout << "Enter Student ID: ";
    std::cin >> student.id;
    std::cout << "Enter Name: ";
    std::cin.ignore();
    std::getline(std::cin, student.name);
    std::cout << "Enter Age: ";
    std::cin >> student.age;
    std::cout << "Enter Grade: ";
    std::cin >> student.grade;

    saveStudent(student);
    std::cout << "Student added successfully!\n";
}

void displayStudents() {
    std::vector<Student> students = loadStudents();
    if (students.empty()) {
        std::cout << "No students found.\n";
        return;
    }

    std::cout << "\n--- Student List ---\n";
    for (const auto &student : students) {
        std::cout << "ID: " << student.id << ", Name: " << student.name
                  << ", Age: " << student.age << ", Grade: " << student.grade << "\n";
    }
}

void updateStudent() {
    int id;
    std::cout << "\n--- Update Student ---\n";
    std::cout << "Enter Student ID to update: ";
    std::cin >> id;

    std::vector<Student> students = loadStudents();
    bool found = false;

    for (auto &student : students) {
        if (student.id == id) {
            found = true;
            std::cout << "Enter new name: ";
            std::cin.ignore();
            std::getline(std::cin, student.name);
            std::cout << "Enter new age: ";
            std::cin >> student.age;
            std::cout << "Enter new grade: ";
            std::cin >> student.grade;
            break;
        }
    }

    if (found) {
        saveAllStudents(students);
        std::cout << "Student updated successfully!\n";
    } else {
        std::cout << "Student not found.\n";
    }
}

void saveStudent(const Student &student) {
    std::ofstream outFile(filename, std::ios::app);
    outFile << student.id << " " << student.name << " " << student.age << " " << student.grade << "\n";
    outFile.close();
}

std::vector<Student> loadStudents() {
    std::vector<Student> students;
    std::ifstream inFile(filename);

    Student student;
    while (inFile >> student.id) {
        inFile.ignore();
        std::getline(inFile, student.name);
        inFile >> student.age >> student.grade;
        students.push_back(student);
    }

    inFile.close();
    return students;
}

void saveAllStudents(const std::vector<Student> &students) {
    std::ofstream outFile(filename, std::ios::trunc);

    for (const auto &student : students) {
        outFile << student.id << " " << student.name << " " << student.age << " " << student.grade << "\n";
    }

    outFile.close();
}
