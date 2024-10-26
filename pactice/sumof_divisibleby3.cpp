#include<iostream>
using namespace std;
int main (){
    int n;
    cout<< "the number is :"<<endl;
    cin>>n;
    int sum = 0;
    for(int i = 1; i <=n ; i++){
        if(i % 3 == 0){
            sum += i;
        }
    }
    cout<< "the sum of divisible by 3 is:"<<sum<<endl;
    return 0;
}