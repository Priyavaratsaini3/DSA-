#include<iostream>
using namespace std;
int main (){
    int n;
    cin>>n;
    int sumofeven_no = 0;
    for(int i = 0; i <=n ; i++){
        if (i % 2 == 0){
        sumofeven_no += i;    
        }
    }
    cout<<"the sum of even number is :"<< sumofeven_no<<endl;
    return 0;
}