#include <iostream>
using namespace std;
int main()
{   //  Square Numbers Patterns
    // int n = 4;

    // for (int i = 1; i <= n; i++)
    // { // outer loop

    //     for (int j = 1; j <= n; j++)
    //     { // inner loop
    //         cout << j << " ";
    //     }
    // cout << endl;
    // }

    // Stars Patterns
    // int n = 5 ;

    // for (int i = 0; i < n; i++){
    //     for(int j = 0; j < n; j++){
    //         cout <<"* ";
    //     }
    //     cout << endl;
    // }

    // Character pattern 
    // int n = 4;

    // for(int i = 0; i < n; i++){
    //     char ch = 'A';
    //     for(int j = 0; j < n; j++){
    //         cout << ch ;
    //         ch = ch + 1;
    //     }
    //     cout  << endl;
    // }

    // Pattern for non repeating number 
    // int n = 3; 
    
    // int num = 1;

    // for(int i = 0; i < n; i++){
    //     for(int j = 0; j < n; j++){
    //         cout << num <<" ";
    //         num++;
    //     }
    //     cout << endl;
    // }


    // Character for non repeating pattern
    // A B C
    // D E F
    // F G H

    int n = 3; 

    char ch = 'A';

    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cout << ch;
            ch++;
        }
        cout << endl;
    }

    return 0;
}