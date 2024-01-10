#include <bits/stdc++.h>

long N,K;
using namespace std;
int main(){
    cin >> N >> K;

    long sub = K - (N - 1) * 2;

    if(sub < 0){
        cout << "No" << endl;
        return 0;
    }

    if(sub % 2 == 0){
        cout << "Yes" << endl; 
    }
    else cout << "No" << endl;

    return 0;
}