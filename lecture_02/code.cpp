#include <iostream>
using namespace std;

int main()
{
    // cout << "hello world" << endl;
    // cout << "priyavart \n saini" << "\n";
    // int age = 25;
    char grade = 's';

    int value = grade;
    cout << value << endl;
    float PI = 3.14f;

    bool isSafe = true;
    double price = 200.44;

    cout << sizeof(grade) << grade << endl;
    cout << isSafe << endl; // true -> 1 & false -> 0

    int newPrice = (int)price;
    cout << newPrice << endl;

    int age;
    // cout << "Enter the age:" << endl;
    // cin >> age;

    // cout << "your age is :" << age << endl;

    // int a = 10, b = 5; // assingment

    // cout << "sum =" << (a + b) << endl;
    // cout << "difference =" << (a - b) << endl;
    // cout << "product =" << (a * b) << endl;
    // cout << "division =" << (a / b) << endl;
    // cout << "modulo =" << (a % b) << endl;
    // int ans = (5 / (double)3);
    // cout << ans << endl;
    // cout << (4 / (double)3) << endl;
    // cout << (3 < 5) << endl;
    // cout << (3 > 5) << endl;
    // cout << (3 >= 3) << endl;
    // cout << (3 == 3) << endl;
    // cout << (3 == 5) << endl;
    // cout << (3 != 5) << endl;
    // cout << (3 != 3) << endl;
    // cout << !(3 < 1) << endl;
    // cout << ((3 < 1) || (4 > 3)) << endl;

    // int a, b;
    cout << "enter a:";
    // cin >> a;
    cout << "enter b:";
    // cin >> b;

    // int sum = a + b;
    // cout << "sum " << sum << endl;
    int a = 10;
    int b = ++a;

    cout << "b = " << b << endl;
    cout << "a = " << a << endl;
    return 0;
}
// Boilerplate code - comment
