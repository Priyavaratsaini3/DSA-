#include<iostream>
using namespace std;
int main (){
    int n ;
    int factorial = 1;
    cin >> n;
    for (int i =1 ; i <= n ; i++){
        factorial *= i;
    }
    cout << "The factorial is :"<< factorial;
    cout<< endl;
    return 0;
}