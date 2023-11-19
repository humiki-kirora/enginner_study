#include <bits/stdc++.h>

using namespace std;
int main(){
    unsigned long long N,K;
    cin >> N >> K;

    vector<unsigned long long> A(N + 1,0);
    vector<unsigned long long> R(N + 1,0);

    for(int i = 0; i < N; i ++) cin >> A[i];

    for(int i = 0; i < N - 1; i ++){
        //初期位置の確認
        if(i == 0) R[i] = 0;
        else R[i] = R[i-1];

        //現在の位置を基準に限界まで伸ばす
        while(R[i] < N - 1 && A[R[i] + 1] - A[i] <= K){
            R[i] ++;
        }
    }

    long long ans = 0;

    for(int i = 0; i < N - 1; i ++) ans += R[i] - i;
    cout << ans << endl;
    return 0;
}