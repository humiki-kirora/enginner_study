#include <bits/stdc++.h>

ulong N,K;
using namespace std;
int main(){
    cin >> N >> K;

    vector<ulong> A(N,0);
    for(ulong i = 0; i < N; i ++) cin >> A[i];


    // step1:calc Afront sum & Aback sum
    ulong element_size = N / 2;
    vector<ulong> AFsum(1 << element_size,0);
    ulong pattern = (1 << element_size);

    for(ulong i = 0; i < pattern; i ++){
        ulong ans = 0;

        for(ulong j = 0; j < element_size; j ++){
            ulong div = (i / (1 << j));
            if(div % 2 == 1) ans += A[j];
        }
        AFsum[i] = ans;
    }

    vector<ulong> ABsum(1 << (N - element_size),0);
    pattern = (1 << (N - element_size));

    for(ulong i = 0; i < pattern; i ++){
        ulong ans = 0;

        for(ulong j = element_size; j < N; j ++){
            ulong div = ((i << element_size) / (1 << j));
            if(div % 2 == 1) ans += A[j];
        }
        ABsum[i] = ans;
    }

    sort(ABsum.begin(),ABsum.end());

    // step2 片方の要素を引いた値を2分探索
    for(ulong i = 0; i < (1 << element_size); i ++){
        ulong ans = K - AFsum[i];
        if(binary_search(ABsum.begin(),ABsum.end(),ans)){
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
    return 0;
}