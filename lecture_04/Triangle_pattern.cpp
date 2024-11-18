#include<iostream>
using namespace std;
int main (){
    // Stars patterns
    // int n = 4;
    // for(int i = 0; i < n; i++){
    //     for(int j = 0; j < i+1; j++){
    //         cout << "* ";
    //     }
    //     cout << endl;
    // }

    // Numbers Patterns

    // int n = 4;

    // for(int i = 0; i < n; i++){
    //     for(int j = 0; j < i + 1; j++){
    //         cout << (i + 1) << " ";
    //     }
    //     cout << endl;
    // }

    // Character Patterns
   
    // int n = 5;

    // for(int i = 0; i < n; i++){
    // char ch = 'A';  
    //     ch = ch + i;
    //     for(int j = 0 ; j < i + 1; j++){
    //     cout << ch ;
    //     }
    //     cout << endl;
    // }

    // int n = 5;

    // for(int i = 0; i < n; i++){
    //     for(int j = 1; j <= i + 1; j++){
    //         cout << j << " ";
    //     }
    //     cout << endl;
    // }

    //     int n;
    //  cout<<"enter the value of n:";
    //  cin>>n;
    //     for(int i = 0; i < n; i++){
    //     for(int j = i+1; j > 0; j--){
    //         cout << j  << " ";
    //     }
    //     cout << endl;
    //     }

        int n = 4;
        
        for(int i = 0; i < n; i++){
            for(int j = i+1; j > 0; j--){
            char ch = 'A';
            ch = ch + j - 1;
            cout << ch << " ";
            }
        cout << endl;
        }
    return 0;
}