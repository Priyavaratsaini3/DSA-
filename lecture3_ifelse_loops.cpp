#include<iostream>
using namespace std;
 
 int main (){
    // int n =  -45;

    // if (n >= 0){
    //     cout<< "n is positive\n";
    // } else {
    //     cout << "n is negative\n";
    // }
    
    // int age ;
    // cout <<"Enter the age:";
    // cin >>age;

    // if(age >= 18){
    //     cout<< "You can vote\n";
    // } else {
    //     cout << "You can't vote\n";
    // }

    // int n ;
    // cout <<"Enter the number:";
    // cin >>n;

    // if(n % 2 == 0){
    //     cout<< "Even\n";
    // } else {
    //     cout << "Odd\n";
    // }

    // int marks ;
    // cout <<"Enter the marks:";
    // cin >>marks;

    // if(marks >= 90){
    //     cout<< "A\n";
    // } else if(marks >= 80 && marks <= 90) {
    //     cout << "B\n";
    // } else {
    //     cout << "C\n"; 
    // }
     
    // char ch;
    // cout <<"enter char: ";
    // cin>> ch;

    // if (ch >= 'a' && ch <= 'z'){
    //     cout  << "lowercase\n";
    // } else {
    //     cout << "uppercase\n";
    // }

// ASCII VALUE 
    // if (ch >= 97 && ch <= 122  ){
    //     cout  << "lowercase\n";
    // } else {
    //     cout << "uppercase\n";
    // }
// ternary 
    // int n = 35;

    // cout<< (n >= 0 ? "positive" : "negative") << endl;

// Loops 

   // int count = 1;

    // while (count <= 5)
    // {
    //     /* code */
    //     cout<< count << " ";
    //     count++;
    // }

   // int n = 15;

    // for (int  i = 1; i <= n; i++)
    // {
    //     /* code */
    //     cout << i << " ";
    // }

    // int sum = 0;

    // for (int i = 1; i <= n; i++)
    // {
    //     /* code */
    //     sum += i;
    //     if (i == 5)
    //     {
    //         break; // keywords
    //     }
        
    // }

    // int oddSum = 0;

    // for (int i = 1; i <= n; i++)
    // {
    //     if (i%2 != 0)
    //     {
    //         oddSum += i;
    //     }
        
    // }
    
    // cout<<"odd sum = "<< oddSum << endl;

 // do while loop

//  do
//  {
//     cout << "Hello world!\n";
//  } while (3 > 5 );
 
    // int n = 10;
    // int i = 1;

    // do{
    //     cout << i << " ";
    //     i++;
    // } while (i <= n);

// prime number find

//int n = 7;
bool isPrime = true ;

// for (int i = 2 ; i <= n - 1; i++){
//     if(n % i == 0){
//         isPrime = false;
//         break;
//     }
// }

// for (int i = 2 ; i*i <= n; i++){
//     if(n % i == 0){
//         isPrime = false;
//         break;
//     }
// }

// if (isPrime == true)
// {
//     cout<< "prime number\n";
// } else {
//     cout << "non prime number\n";
// }

//nested loops
int n = 10;
for (int i = 1; i <= n ; i++)
{
int x = 10;
for(int j = 1; j <= x; j++){
    cout << "*";
}
    cout << "*****\n";
}

cout << endl;
    return 0;
 } 
