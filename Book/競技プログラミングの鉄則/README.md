開始日 2023/05/08  
読了日 2023/ * / *  
著者 米田優峻 2022年9月16日初版

# 目次
- [目次](#目次)
- [序章 競技プログラミング入門](#序章-競技プログラミング入門)
  - [競技プログラミングとは](#競技プログラミングとは)
  - [コンテストの種類](#コンテストの種類)
  - [競技プログラミングで求められること](#競技プログラミングで求められること)
  - [本書の進め方](#本書の進め方)
- [1章 アルゴリズムと計算量](#1章-アルゴリズムと計算量)
  - [アルゴリズムとは](#アルゴリズムとは)
    - [具体例1 1+2+...+50を計算](#具体例1-1250を計算)
    - [具体例2 迷路の最短手数](#具体例2-迷路の最短手数)
  - [計算量](#計算量)
    - [計算量の例](#計算量の例)
    - [計算量の目安](#計算量の目安)
  - [第1章のゴール](#第1章のゴール)
  - [1.1 導入問題](#11-導入問題)
    - [A01 Thre First Problem ★1](#a01-thre-first-problem-1)
    - [B01 A+B Problem](#b01-ab-problem)
  - [1.2 全探索(1) ★1](#12-全探索1-1)
    - [A02 Linear Search](#a02-linear-search)
  - [1.3 全探索(2)](#13-全探索2)
    - [A03 Two Cards ★1](#a03-two-cards-1)
    - [B03 Supermarket 1](#b03-supermarket-1)
  - [1.4 2進法](#14-2進法)
    - [A04 Binary Representation 1 ★2](#a04-binary-representation-1-2)
    - [B04 Binary Representation 2](#b04-binary-representation-2)
    - [1.5 チャレンジ問題 ★2](#15-チャレンジ問題-2)
    - [ビット全探索](#ビット全探索)
- [2章 累積和](#2章-累積和)
  - [2.0 累積和とは](#20-累積和とは)
  - [2.1 一次元の累積和(1)](#21-一次元の累積和1)
    - [A06 How Many Guests? ★2](#a06-how-many-guests-2)
    - [B06 Lottery](#b06-lottery)
  - [2.2 一次元の累積和](#22-一次元の累積和)
    - [A07 Event Attendance ★3](#a07-event-attendance-3)
    - [B07 Convenience Store 2](#b07-convenience-store-2)
  - [2.3 二次元の累積和](#23-二次元の累積和)
    - [A08 Two DImensional Sum ★4](#a08-two-dimensional-sum-4)
    - [B08 Counting Points](#b08-counting-points)
  - [2.4 二次元の累積和(2)](#24-二次元の累積和2)
    - [A09 Winter in ALGO Kingdom ★4](#a09-winter-in-algo-kingdom-4)
    - [B09 Papers](#b09-papers)
  - [2.5 チャレンジ問題](#25-チャレンジ問題)
    - [A10 Resort Hotel ★4](#a10-resort-hotel-4)
- [3章 二分探索](#3章-二分探索)
  - [3.0 二分探索とは](#30-二分探索とは)
  - [3.1 配列の二分探索](#31-配列の二分探索)
    - [A11　Binary Search 1　★2](#a11binary-search-12)
    - [B11 Binary Search 2](#b11-binary-search-2)
  - [3.2 答えで二分探索](#32-答えで二分探索)
    - [A12 Printer ★3](#a12-printer-3)
    - [B12 Equation](#b12-equation)
    - [A13 Close Pairs ★4](#a13-close-pairs-4)
- [4章 動的計画](#4章-動的計画)
  - [4.0 動的計画法とは](#40-動的計画法とは)
  - [4.1 動的計画法の基本](#41-動的計画法の基本)
    - [A16 Dungeon1 ★2](#a16-dungeon1-2)
    - [B16 Frog 1](#b16-frog-1)
  - [4.2 動的計画法の復元](#42-動的計画法の復元)
    - [A17 Dungeon2 ★3](#a17-dungeon2-3)
    - [B17 Frog 1 with Restoration](#b17-frog-1-with-restoration)
  - [4.3 二次元のDP(1):部分和問題](#43-二次元のdp1部分和問題)
    - [A18 Subset Sum ★3](#a18-subset-sum-3)
    - [B18 Subset Sum with Restoration](#b18-subset-sum-with-restoration)
  - [4.4 二次元のDP(2):ナップザック問題](#44-二次元のdp2ナップザック問題)
    - [A19 Knapsack1 ★3](#a19-knapsack1-3)
    - [B19 knapsack2](#b19-knapsack2)
  - [4.5 二次元のDP(3):最長共通部分列問題](#45-二次元のdp3最長共通部分列問題)
    - [A20 LSC ★4](#a20-lsc-4)
    - [B20 Edit Distance](#b20-edit-distance)
  - [4.6 二次元のDP(4):区間DP](#46-二次元のdp4区間dp)
    - [A21 Block Game ★4](#a21-block-game-4)
    - [B21 Longest Subpalindrome](#b21-longest-subpalindrome)
- [5章 数学的問題](#5章-数学的問題)
  - [5.0 数学的問題について](#50-数学的問題について)
  - [5.1 素数判定](#51-素数判定)
    - [A26 Prime Check ★2](#a26-prime-check-2)
    - [B26 Output Prime Numbers](#b26-output-prime-numbers)
  - [5.2 最大公約数](#52-最大公約数)
    - [A27 Calculate GCD ★2](#a27-calculate-gcd-2)
    - [B26 Calculate LCM](#b26-calculate-lcm)
  - [5.3 余りの計算(1):基本](#53-余りの計算1基本)
    - [A28 Blackboards ★2](#a28-blackboards-2)
    - [B28 Fibonacci Easy (mod 1000000007)](#b28-fibonacci-easy-mod-1000000007)
  - [5.4 余りの計算(2)：累乗](#54-余りの計算2累乗)
    - [A29 Power ★3](#a29-power-3)
    - [B29 Power Hard](#b29-power-hard)
  - [5.5 余りの計算(3):割り算](#55-余りの計算3割り算)
    - [A30 Combination ★4](#a30-combination-4)
    - [B30 Combination2](#b30-combination2)
  - [5.6 包除原理](#56-包除原理)
    - [A31 Divisors ★2](#a31-divisors-2)
- [6章 考察テクニック](#6章-考察テクニック)
- [7章 ヒューリスティック](#7章-ヒューリスティック)
- [8章 データ構造とクエリ処理](#8章-データ構造とクエリ処理)
- [9章 グラフアルゴリズム](#9章-グラフアルゴリズム)
  - [9.0 グラフとは](#90-グラフとは)
  - [9.1 グラフの実装方法](#91-グラフの実装方法)
    - [A61 Adjacent Vertices](#a61-adjacent-vertices)
    - [B61 Influencer](#b61-influencer)
  - [9.2 深さ優先探索](#92-深さ優先探索)
    - [A62 Depth First Search ★3](#a62-depth-first-search-3)
    - [B62 Print a Path](#b62-print-a-path)
  - [9.3 幅優先探索](#93-幅優先探索)
    - [A63 Shortest Path 1 ★3](#a63-shortest-path-1-3)
      - [実装方法](#実装方法)
  - [B63 幅優先探索](#b63-幅優先探索)
  - [9.4 ダイクストラ法](#94-ダイクストラ法)
    - [A64 Shortest Path 2 ★4](#a64-shortest-path-2-4)
    - [B64 Print a Path](#b64-print-a-path)
  - [9.5 木に対する動的計画法](#95-木に対する動的計画法)
    - [A65 Road to Promotion ★4](#a65-road-to-promotion-4)
    - [B65 Road to Promotion Hard](#b65-road-to-promotion-hard)
  - [9.6 Union-Find 木](#96-union-find-木)
    - [Connect Query ★3](#connect-query-3)
    - [B66 Typhoon](#b66-typhoon)
  - [9.7 最小全域木問題](#97-最小全域木問題)
    - [A67 MST ★5](#a67-mst-5)
    - [B67 Max MST](#b67-max-mst)
  - [9.8 最大フロー問題](#98-最大フロー問題)
    - [A68 Maximum Flow ★6](#a68-maximum-flow-6)
- [10章 総合問題](#10章-総合問題)
- [終章 さらに上達するには](#終章-さらに上達するには)



# 序章 競技プログラミング入門

## 競技プログラミングとは
プログラミングの問題を解くことを競技にしたもので「競プロ」と言われるもの  
約15年程度前に本格的に始まった競技だが、現在国内だけで3万人程度のアクティブユーザがおり、中高生からプログラマまで幅広い層が参加しており、コーディングスキル向上や教育などの目的で利用されることも多い

## コンテストの種類
- AtCoder (https://atcoder.jp/?lang=ja)  
日本最大手のプログラミングコンテスト  毎週末21時からオンラインで開催  
コンテストの成績に応じたレーティングがつけられるという特徴があり、強さの照明になるという点で、技術系のアルバイトや就職活動に利用されることもある  

- 日本情報オリンピック(JOI)  
高校生以下を対象とするコンテスト  
毎年1500人程度が参加して4人まで絞り、日本代表として世界大会に出場できる  
自分には関係のないことなので省略

- 大学対抗プログラミングコンテスト(ICPC)  
ICPC Foundationが開催する大学生向けのコンテスト  
3人チームでの参加のため、AtCoderと違って戦略とチームワークが重要  
自分には関係のないことなので省略  

- Google Code Jam  
Google社が毎年開催している競技プログラミングの大会  
世界各地から毎年2万人程度が予選に参加  
2時間半で3~4問解く形式で行われて、3回の予選を勝ち抜いた上位25人は現地で行われる決勝戦に参加できる

- アルゴリズム実技検定(PAST)(https://past.atcoder.jp/)  
日本初のアルゴリズム構築能力を測る検定試験  
AtCoder社が主催しており、検定料は8800円と金がかかるが、基準点に達した場合は「アルゴリズムができる人材」の証明になるため、市場価値のアップに繋がる

この中ではAtCoder、Google Code Jam、アルゴリズム実技検定(PAST)が自分には関係ありそう  

## 競技プログラミングで求められること
- プログラミング能力  
プログラミングを書く必要があるので、どれかの一つの言語について必要な機能を利用して希望通りの機能を素早くコーディングする能力が求められる

- アルゴリズムの知識  
競技プログラミングでは処理時間の制約があり、正しい答えを出すだけでは不十分な場合がある  
そのため、より効率的に答えを導き出すための典型的なアルゴリズムを学ぶ必要がある

- 思考力・発想力  
競技プログラミングで出題される問題はアルゴリズムの知識だけで解けるとは限らない  
問題を上手く分解したり、規則性に着目したりなどの発想力やひらめきが要求されることもある  
また複雑な問題を整理して解き切るために必要な論理的思考力も重要

## 本書の進め方
- 読み方
全部で10章で構成されており、1章で競技プログラミングで戦う上での基礎となるアルゴリズムや計算量について概観する。  
2~9章以降は頻出の典型アルゴリズムや考察テクニックについて触れている  
それぞれ独立しているため、どこから始めても大丈夫

- 例題・応用問題・力試し問題  
★1~6の難易度の問題が用意されており、難易度が高いほど知識や応用力が必要になる

- 自動採点システム (https://atcoder.jp/contests/tessoku-book)  
本書の例題・応用問題・力試し問題を正しいか機械的に判定する自動採点システムがあるため利用可能

# 1章 アルゴリズムと計算量  

## アルゴリズムとは
アルゴリズムとは問題を解くための**計算の手順**のこと  
同じ問題を解くとしても複数のアルゴリズムが考えられ、効率の良し悪しが異なる場合がある

### 具体例1 1+2+...+50を計算
一番ナイーブな方法としては1から順に足し算を行う方法でこれでも正解の1275を求める事ができる  
ただし、足し算を49回行う必要があり、計算するのが大変である  

そこで、以下のように考える
```
 1 + 2 + 3 + ... + 50 = (1 + 50) + (2 + 49) + (3 + 48) + ... + (25 + 26) = 51 * 25 
```
このように51が25個存在しているという風に考えることで、一回の掛け算の計算で答えを得ることができ、効率的に計算が可能  

### 具体例2 迷路の最短手数
以下の迷路の最短経路を求めることを考える  
![迷路](images/1_maize.png)

一番ナイーブな方法としてはスタート地点から出発する全ての経路について調べることで**全探索**と呼ばれている方法  
ただし、この規模の迷路ですら経路数は15万通り以上の経路を調べる必要があり、コンピュータの力を借りなければ到底実現できない  

そこでより良い解放を考える  
まず、スタート地点を「0」として書き込み、その隣接している経路に「1」と書き込む  
その後、同様に隣接していてまだ数字が書かれていない経路に2,3,...と順に書き込む操作を行うと最終的に以下のような結果が得られる  

![](images/1_maze_algorithm.png)

このようにすることで、ゴールまでの最短手数20が計算されるので、ゴールから順に20⇒19⇒18と辿っていくことで全探索よりも少ない探索で最短経路を得ることができる  
このアルゴリズムは**幅優先探索**と呼ばれている(第9章で扱う)  

このように同じ問題を解くにしても複数のアルゴリズムがあり、効率が大きく異なる  

## 計算量
アルゴリズムによって効率が変化するのは分かったが、アルゴリズムの効率をどのように評価するべきか  
どこで用いられるのが**計算量**という概念

計算量はアルゴリズムの効率を評価する1つの指標であり、*O*記法を用いて*O(N)*,*O(N^2)*,*O(2^N)*等の形で表され次のような意味を持つ

|  計算量  |  意味  |
| ---- | ---- |
|  O(N)  |  計算回数が概ねNに比例する  |
|  O(N^2)  |  計算回数が概ねN^2に比例する  |
|  O(2^N)  |  計算化数が概ね2^Nに比例する  |

### 計算量の例
先ほどの[具体例1]()で説明した1ずつ足していく方法はN - 1回の足し算が必要なので計算量は*O(N)*
それに対し、工夫した解法の方は1回の掛け算で済むため、*O(1)*となる

このように*O*記法では大まかな計算回数を表している

### 計算量の目安
各計算量における計算回数とNの関係を以下の表に示す  
家庭用PCの計算速度は毎秒10億回程度であるため、10^9を超える部分は赤色になっている  
競技プログラミングにおいては、赤色で塗られた部分については正解となる可能性は低い
![](images/1_O_table.png)

## 第1章のゴール
次に全5問の例題を通して、アルゴリズムと計算量に関する理解と競技プログラミングの問題形式に慣れることを目指す  

## 1.1 導入問題
### A01 Thre First Problem ★1
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_a

特に何も難しいことはないのでそのまま解ける
```C++
#include <bits/stdc++.h>
using namespace std;
 
int main(){
  int N;
  cin >> N;
  cout << N * N << endl;
  return 0;
}
```


### B01 A+B Problem
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bz  

特に何も難しいことはないのでそのまま解ける
```C++
#include <bits/stdc++.h>
using namespace std;
 
int main(){
  int A,B;
  cin >> A >> B;
  cout << A + B << endl;
  return 0;
}
```

## 1.2 全探索(1) ★1
**全探索**は有り得る全てのパターンを調べ上げる方針で問題を解く方法  
Ex)4桁の暗証番号を0000~9999までのすべての番号を試す  
一番シンプルで確実に解けるが、時間的には効率が悪い
### A02 Linear Search
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_b  

set<>を使うと重複を避けられる
```C++
#include <bits/stdc++.h>
using namespace std;
 
int main(){
  int N,X;
  cin >> N >> X;

  set<int> A;
  for(int i = 0; i < N; i ++) {
    int tmp;
    cin >> tmp;
    A.insert(tmp);
  }

  if(find(A.begin(),A.end(),X) != A.end()){
    cout << "Yes" << endl;
  }
  else {
    cout<< "No" << endl;
  }

  return 0;
}
```

## 1.3 全探索(2)
### A03 Two Cards ★1
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_c  

P+Qのパターンを二重ループで全て試すと正解できる
```C++
#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int N,K;

    cin >> N >> K;
    vector<int> P(N),Q(N);

    for(int i = 0; i < N; i ++) cin >> P[i];
    for(int i = 0; i < N; i ++) cin >> Q[i];

    for(int i = 0; i < N; i ++){
        for(int j = 0; j < N; j ++){
            if(K == P[i] + Q[j]){
                cout << "Yes" << endl;
                return 0;
            }
        }
    }

    cout << "No" << endl;
    return 0;
}
```

### B03 Supermarket 1
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cb

3重ループで全パターンを試す
```C++
#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int N;
    cin >> N;

    vector<int> A(N);
    for(auto & a : A) cin >> a;

    for(int i = 0; i < N - 2; i ++){
        for(int j = i + 1; j < N - 1; j ++){
            for(int k = j + 1; k < N; k ++){
                if(A[i] + A[j] + A[k] == 1000){
                    cout << "Yes" << endl;
                    return 0;
                }
            }
        }
    }

    cout << "No" << endl;
    return 0;
}
```
## 1.4 2進法
### A04 Binary Representation 1 ★2
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_d

普通に10進数を2進数に変更する方法を試す
```C++
#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int N;
    cin >> N;

    vector<int> ans;
    int tmpN = N;
    while( (tmpN / 2) != 0){
        ans.push_back(tmpN % 2);
        tmpN = tmpN / 2;
    }
    ans.push_back(1);

    //0埋め
    for(int i = 0; i < 10 - ans.size(); i++) cout << 0;

    for(int i = ans.size() - 1; i >= 0; i --){
        cout << ans[i];
    }
    cout << endl;

    return 0;
}
```

**別解**  
対象の数字を2^n(n=0~9)までの数で割った余りを表示すれば簡単に解ける　　
```C++
#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int N;
    cin >> N;

    for(int i = 9; i >= 0; i --){
        int num = (1 << i);
        cout << (N / num) % 2;
    }
    cout << endl;

    return 0;
}
```

### B04 Binary Representation 2
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cc

2⇒10進数変換では10で割った余りを用いて、位に応じてシフトしたものの合計を計算すればよい
```C++
#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int N;
    cin >> N;

    int ans = 0;
    int count = 0;
    while(N > 0){
        ans += (( N % 10) << count);
        count ++;
        N /= 10;
    }

    cout << ans << endl;
    return 0;
}
```
### 1.5 チャレンジ問題 ★2
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_e

2枚のカードが決まれば3枚目は自動的に決まるので2重ループの探索で求まる
```C++
#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int N,K;
    cin >> N >> K;
    int ans = 0;

    for(int r = 1; r <= N; r ++){
        for(int b = 1; b <= N; b ++){
            if(K - (r + b) > N || K - (r + b) < 1) continue;
            ans ++;
        }
    }

    cout << ans << endl;
    return 0;
}
```

### ビット全探索
本格的な全探索問題として、以下の部分和問題を考える
> N枚のカードがあり、1からNまでの番号がつけられている。
> カードiには整数Aiが描かれており、カードの中からいくつか選び、書かれた整数の合計がSとなるような方法があるかを判定する

この問題では、N=20程度の小さい値であれば、全探索で解くことが可能だが、  
単純に実装すると、N重のfor文が必要になるため実装がめんどくさい  

2進数を用いることで、カードの選び方を0以上2^N - 1以下の整数値に対応させることが可能

![](images/1_bit%E5%85%A8%E6%8E%A2%E7%B4%A2.png)

これにより、部分和問題を解くプログラムを簡単に実装可能

```C++
#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int N,K;
    cin >> N >> K;
    
    vector<int> A(N);
    for(auto & a : A) cin >> a;

    int pattern = (1 << N);

    //0~2^N - 1の全パターンを探索
    for(int i = 0; i < pattern; i ++){
      int ans = 0;

      //iを2進数に変換して、1の箇所を足す
      for(int j = 0; j < N; j ++){
        int div = (i / (1 << j));
         if(div % 2 == 1) ans += A[j];
      }

      //一致すれば終了
      if(A[j] == K){
        cout << "Yes" << endl;
        return 0;
      }
    }

    cout << "No" << endl;
    return 0;
}
```

# 2章 累積和
## 2.0 累積和とは
最初に、以下の計算問題を考える
> ある遊園地では、1月前半の来場者数が以下の表のようになった。
> 4-13、3-10、2-15までの総来場者数を計算してください
 
![](images/2_%E7%B4%AF%E7%A9%8D%E5%92%8C%E4%BE%8B%E9%A1%8C1.png)

単純に考えるならば、1/4~1/13までの来場者数の総和をそのまま計算するだけで良いが、
これは面倒な上、他の期間の計算でも同じような計算が必要になり効率が悪い

そこで以下の表のように1月1日からの累積来場者数を前もって計算する

![](images/2_%E7%B4%AF%E7%A9%8D%E5%92%8C%E4%BE%8B%E9%A1%8C2.png)

この表を前もって計算しておくことで、以下の一回の引き算で期間の総来場者数を求めることができる
- 1/4~13の総来場者数　= 1/13時点の累積来場者数 - 1/3時点の累積来場者数
- 1/3~10の総来場者数　= 1/10時点の累積来場者数 - 1/2時点の累積来場者数
- 1/2~15の総来場者数　= 1/15時点の累積来場者数 - 1/1時点の累積来場者数

このように配列の先頭からの累積値を記録した累積和を前もって計算しておくと効率的に範囲の合計を計算できるようになる

## 2.1 一次元の累積和(1)
### A06 How Many Guests? ★2
問題文:https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_ai

そのままAの累積和を計算してから、引き算を行う  
累積和の日にちを0日目から計算することで、if文を使わずにスムーズに計算可能
```C++
#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int N,Q;
    cin >> N >> Q;

    vector<int> A(N);
    for(auto & a : A) cin >> a;

    vector<int> cumsum(N + 1,0);
    cumsum[0] = 0;
    for(int i = 1; i < N + 1; i ++){
        cumsum[i] = cumsum[i - 1] + A[i - 1];
    }

    vector<pair<int,int>> Question(Q);
    for(auto & q : Question) cin >> q.first >> q.second;

    for(int i = 0; i < Q; i ++){
        int l = Question[i].first;
        int r = Question[i].second;
        cout << cumsum[r] - cumsum[l - 1] << endl;
    }

    return 0;
}
```

### B06 Lottery
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ce

当たりの累積和を計算して、その区間の当たりの数を計算  
その後、その区間の日数と当たりの数を照らし合わせて判定すればよい
```C++
#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int N,Q;
    cin >> N;

    vector<int> A(N);
    for(auto & a : A) cin >> a;

    vector<int> cumsum(N+1);
    cumsum[0] = 0;
    for(int i = 1; i < N + 1; i ++){
        cumsum[i] = cumsum[i - 1] + A[i - 1]; 
    }

    cin >> Q;
    vector<pair<int,int>> question(Q);
    for(auto & q : question) cin >> q.first >> q.second;

    for(auto & q : question){
        int l = q.first;
        int r = q.second;
        int hit = cumsum[r] - cumsum[l - 1];
        int no_hit = (r - l + 1) - hit;
        if(hit == no_hit) cout << "draw" << endl;
        else if(hit > no_hit) cout << "win" << endl;
        else cout << "lose" << endl;
    }


    return 0;
}
```

## 2.2 一次元の累積和
### A07 Event Attendance ★3
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_g

普通にやると、各人の参加日程を調べて、その日程分プラスしていくという処理が必要になるが  
日程が多いとそれだけで処理時間がかなり増えてしまい時間切れになる  
例えば、D = 10^5日でN = 10^5人が全日参加した時、D * N　= 10^10回の加算処理が行われる  
<br>
そこで、前日比を考えて、**前日比の累積和**を取ることで効率的に解くことができる  
まず、参加者の最初の参加日をL日目、最終日をR日目として、
L日目に1人増えるので+1,R - 1日は1人減るので-1という風に記録していき、この処理を全ての参加者に対して行う事で前日比を算出できる
<br>  
前日比なので、0日目を0人として前日比の累積和を計算すると、各日の参加者の数を算出することができる

ここで先ほどのD=10^5 N=10^5の例との計算量を比較してみる  
前日比の累積和を使用したアルゴリズムでは以下の計算が行われる
- 1人に対して加算回数は2回だけなので、10^5 * 2
- 累積和を計算するのに、10^5回の加算処理

そのため、加算回数は```10^5 * 2 + 10^5 = 10^5 * 3 < 10^10```となり、より少ない計算回数で問題を解く事が可能となる

```C++
#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int D,N;
    cin >> D >> N;

    vector<pair<int,int>> person(N);
    for(auto & p : person) cin >> p.first >> p.second;

    vector<int> ratio(D + 2,0),cumsum(D + 2,0);
    for(auto & p : person){
        int l = p.first;
        int r = p.second;
        ratio[l] ++;
        ratio[r + 1] --;
    }

    cumsum[0] = 0;
    for(int i = 1; i < D + 1; i ++){
        cumsum[i] = ratio[i] + cumsum[i - 1];
    }

    for(int i = 1; i < D + 1; i ++){
        cout << cumsum[i] << endl;
    }
    
    return 0;
}
```

### B07 Convenience Store 2
問題文:https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_al  

A07と基本的には同じように解く  
今回は前日比の代わりに、先に時刻Tにおける人数の増減を記録することで、
累積和で時刻T~T+1の間に出勤している人数を求める事ができる

```C++
#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int T,N;
    cin >> T >> N;

    vector<pair<int,int>> person(N);
    for(auto &p : person) cin >> p.first >> p.second;

    vector<int> rate(T+2,0);

    for(int i = 0; i < person.size(); i ++){
        rate[person[i].first + 1] ++;
        rate[person[i].second + 1] --;
    }

    vector<int> cumsum(T+2,0);
    for(int i = 1; i < T + 2; i++){
        cumsum[i] = cumsum[i - 1] + rate[i];
    }

    for(int i = 1; i < T + 1; i ++){
        cout << cumsum[i] << endl;
    }

    return 0;
}
```

## 2.3 二次元の累積和
### A08 Two DImensional Sum ★4
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_h  

累積和は1次元だけでなく、2次元にも適用することが可能  
二次元の累積を取る場合は、先に行方向の累積和を計算し、その計算結果を元に列方向の累積和を計算することで、
座標(1,1)から座標(a,b)の矩形の全ての要素の和を座標(a,b)に計算することができる  
この累積和を元に任意の座標(a,b)と座標(c,d)内の累積和がを求める場合は以下のように求める事が可能

```
座標(c,d)の累積和 - (座標(c,b -1)の累積和 + 座標(a - 1,d)の累積和 - 座標(a-1 , b-1)の累積和)
```

具体的には以下のようなイメージの計算が行われる  
重複する部分があるため、その分を引きすぎないように注意が必要<br>
![](images/2_%E4%BA%8C%E6%AC%A1%E5%85%83%E7%B4%AF%E7%A9%8D%E5%92%8C.png)

```C++
#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int H,W;
    cin >> H >> W;
    vector<vector<int>> matrix(H,vector<int>(W,0));

    for(auto & row : matrix)
        for(auto & col : row) cin >> col;

    int Q;
    cin >> Q;
    vector<vector<int>> question(Q,vector<int>(4,0));

    for(auto & row : question)
        for(auto & col : row) cin >> col;
    
    vector<vector<int>> cumsum(H + 1,vector<int>(W + 1,0));
    for(int i = 1; i < H + 1 ; i ++){
        for(int j = 1; j < W + 1; j ++){
            cumsum[i][j] = cumsum[i][j - 1] + matrix[i - 1][j - 1];
        }
    }

    for(int i = 1; i < H + 1 ; i ++){
        for(int j = 1; j < W + 1; j ++){
            cumsum[i][j] = cumsum[i][j] + cumsum[i - 1][j];
        }
    }

    for(auto & q : question){
        cout << cumsum[q[2]][q[3]] - (cumsum[q[2]][q[1] - 1] + cumsum[q[0] - 1][q[3]] - cumsum[q[0] - 1][q[1] - 1]) << endl;
    }

    return 0;
}
```

### B08 Counting Points
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cg  

A08同様に二次元累積和を計算すれば計算可能
```C++
#include <bits/stdc++.h>
using namespace std;

//二次元行列デバッグ用関数
void print_2Dmatrix(vector<vector<int>> & matrix){
    for(int i = 0; i < matrix.size(); i ++){
        for(int j = 0; j < matrix[0].size(); j ++){
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}
 
int main(){
    int N;
    cin >> N;

    vector<int> cood_x(N);
    vector<int> cood_y(N);
    for(int i = 0; i < N; i ++) cin >> cood_x[i] >> cood_y[i];

    //行列の範囲を計算
    int max_x = *max_element(cood_x.begin(),cood_x.end());
    int max_y = *max_element(cood_y.begin(),cood_y.end());

    int Q;
    cin >> Q;
    vector<vector<int>> rect(Q,vector<int>(4,0));
    for(auto & r : rect) cin >> r[0] >> r[1] >> r[2] >> r[3];

    //二次元累積和の計算
    vector<vector<int>> matrix(max_y,vector<int>(max_x,0));
    vector<vector<int>> cumsum(max_y + 1,vector<int>(max_x + 1,0));

    for(int i = 0; i < N; i ++){
        matrix[cood_y[i] - 1][cood_x[i] - 1]++;
    }

    for(int h = 1; h < max_y + 1; h ++){
        for(int w = 1; w < max_x + 1; w ++){
            cumsum[h][w] = cumsum[h][w - 1] + matrix[h - 1][w - 1]; 
        }
    }

    for(int h = 1; h < max_y + 1; h ++){
        for(int w = 1; w < max_x + 1; w ++){
            cumsum[h][w] = cumsum[h][w] + cumsum[h - 1][w]; 
        }
    }

    //答えの出力
    for(auto & r : rect){
        int ans = cumsum[r[3]][r[2]] - (cumsum[r[3]][r[0] - 1] + cumsum[r[1] - 1][r[2]]) + cumsum[r[1] - 1][r[0] - 1];
        cout << ans << endl;
    }

    return 0;
}
```

## 2.4 二次元の累積和(2)
### A09 Winter in ALGO Kingdom ★4
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_i

前日比の累積和の応用で解くことが可能  
以下の画像を例に説明すると、(2,2) ~ (4,4)の範囲に雪が降ったとする<br>
その場合、(2,2)と(5,5)に+1,(2,5)と(5,2)に-1を加算すると、その二次元の累積和を計算すると、丁度(2,2) ~ (4,4)の範囲に雪が積持っていることを確認する事が計算できる。  

![](images/2_2%E6%AC%A1%E5%85%83%E7%B4%AF%E7%A9%8D%E5%92%8C%E3%81%AE%E6%AF%94.png)

二日目以降も同様に前日との差分を記録していくことで、累積和を取った時に現在の積雪量を復元することができるため、この方法で問題を解くことができる。

```C++
#include <bits/stdc++.h>
using namespace std;

void print_2Dmatrix(vector<vector<int>> & matrix){
    for(int i = 0; i < matrix.size(); i ++){
        for(int j = 0; j < matrix[0].size(); j ++){
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}
 
int main(){
    int N, H, W;
    cin >> H >> W >> N;

    vector<vector<int>> matrix(H + 1,vector<int>(W + 1,0));

    for(int i = 0; i < N; i++){
        int c[4];
        cin >> c[0] >> c[1] >> c[2] >> c[3];

        matrix[c[0] - 1][c[1] - 1] ++;
        matrix[c[0] - 1][c[3]] --;
        matrix[c[2]][c[1] - 1] --;
        matrix[c[2]][c[3]] ++;
    }

    vector<vector<int>> cumsum(H + 1,vector<int>(W + 1,0));

    for(int h = 1; h < H + 1; h ++){
        for(int w = 1; w < W + 1; w ++){
            cumsum[h][w] = cumsum[h][w - 1] + matrix[h - 1][w - 1];
        }
    }

    for(int h = 1; h < H + 1; h ++){
        for(int w = 1; w < W + 1; w ++){
            cumsum[h][w] = cumsum[h][w] + cumsum[h - 1][w];
        }
    }

    for(int i = 1; i < H + 1; i ++){
        for(int j = 1; j < W; j ++){
            cout << cumsum[i][j] << " ";
        }
        cout << cumsum[i][W] << endl;
    }

    return 0;
}
```
### B09 Papers
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ch

A09同様二次元配列の前回比を考えると解くことができる。  
座標の扱いで少し苦戦したので、実際に図に落として考えてみると整理しやすいかもしれない

```C++
#include <bits/stdc++.h>
using namespace std;
 
void print_2Dmatrix(vector<vector<int>> & matrix){
    for(int i = 0; i < matrix.size(); i ++){
        for(int j = 0; j < matrix[0].size(); j ++){
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
}
 
int main(){
    int N;
    cin >> N;
 
    vector<vector<int>> coods(N,vector<int>(4,0));
 
    int max_x = 0;
    int max_y = 0;
 
    for(auto & c : coods){
        cin >> c[0] >> c[1] >> c[2] >> c[3];
        max_x = max(max_x,c[2]);
        max_y = max(max_y,c[3]);
    }
 
    int H = max_y;
    int W = max_x;
 
    vector<vector<int>> matrix(H + 2,vector<int>(W + 2,0));
    vector<vector<int>> cumsum(H + 2,vector<int>(W + 2,0));
 
    for(auto &c : coods){
        matrix[c[1]][c[0]] ++;
        matrix[c[1]][c[2]] --;
        matrix[c[3]][c[0]] --;
        matrix[c[3]][c[2]] ++;   
    }
 
    for(int h = 1; h < H + 2; h ++){
        for(int w = 1; w < W + 2; w ++){
            cumsum[h][w] = cumsum[h][w - 1] + matrix[h - 1][w - 1];
        }
    }
 
    for(int h = 1; h < H + 2; h ++){
        for(int w = 1; w < W + 2; w ++){
            cumsum[h][w] = cumsum[h][w] + cumsum[h - 1][w];
        }
    }
 
    int ans = 0;
    for(int h = 1; h < H + 2; h ++){
        for(int w = 1; w < W + 2; w ++){
            if (cumsum[h][w] != 0) ans++;
        }
    }
 
    cout << ans << endl;
 
    return 0;
}
```

## 2.5 チャレンジ問題
### A10 Resort Hotel ★4
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_j<br>

累積和の応用で解くことが可能<br>
以下の図で説明すると、このように使用できない範囲が決まっている場合、この状況での最大値は、`max(1~2号室の最大値、6~7号室の最大値)`で求める事が可能<br>
その為、予め1~2号室、6~7号室の最大値が計算できていればO(1)で解くことが可能になる。<br>
![](images/2_challenge.png)

この場合、左から順にそれまでの範囲の最大値を計算した結果と、右側から順にそれまでの範囲の最大値を計算した結果を保持しておくことで、任意の範囲の最大値を即座に求める事ができる<br>
![](images/2_challenge_ans.png)

```C++
int main(){
    int N;
    cin >> N;

    vector<int> A(N);
    for(auto & a : A) cin >> a;

    int D;
    cin >> D;
    vector<int> L(D);
    vector<int> R(D);
    for(int i = 0; i < D; i ++){
        cin >> L[i] >> R[i];
    }

    vector<int> L_max(N,0);
    vector<int> R_max(N,0);

    L_max[0] = A[0];
    for(int i = 1; i < N; i ++){
        L_max[i] = max(A[i],L_max[i - 1]);
    }

    R_max[N - 1] = A[N - 1];
    for(int i = N - 2; i > 0; i --){
        R_max[i] = max(A[i],R_max[i + 1]);
    }

    for(int i = 0; i < D; i ++){
        cout << max(L_max[L[i] - 1 - 1],R_max[R[i]]) << endl;
    }


    return 0;
}
```

# 3章 二分探索
## 3.0 二分探索とは
>1以上64以下の整数を思い浮かべ、あなたはYes/Noで答えられる質問を6回まで行う事が可能。思い浮かべた数字を特定してください

このような問題がある時、素直に解くのであれば、1~64まで順に質問すればいつかはあてられるが、回数制限があるのでそれはできない

そこで、あらゆる候補の中で中央で区切る質問を繰り返すと、確実に6回で解くことが可能
1. 32以上か?⇒No 1~31
2. 16以上か?⇒Yes 16~31
3. 24以上か?⇒Yes 24~31
4. 28以上か?⇒No 24~27
5. 26以上か?⇒Yes 26~27
6. 27以上か?⇒No **26**

こういった中央に区切りながら探索範囲を半分ずつにしていくアルゴリズムを**二分探索法**という、この章ではこの二分探索法の実装について解説していく

## 3.1 配列の二分探索
### A11　Binary Search 1　★2
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_k

素直に二分探索で解ける
途中で同じ数を見つけた場合はそこで探索を止めた方が効率的ではある
```C++
#include <bits/stdc++.h>

using namespace std;

int main(){
    int N,X;
    cin >> N >> X;
    vector<int> A(N,0);
    for(int i = 0; i < N; i ++) cin >> A[i];

    int min_idx = 0;
    int max_idx = N - 1;

    while(max_idx -  min_idx > 1){
        int idx = min_idx + (max_idx - min_idx) / 2;
        if(A[idx] <= X){
            min_idx = idx;
        }
        else{
            max_idx = idx - 1;
        }
    }

    int ans = X == A[min_idx] ? min_idx + 1 : max_idx + 1;

    cout << ans << endl;

    return 0;
}

```

ちなみに今回二分探索を自力で実装しているが、C++には二分探索用のライブラリが既に用意されている。
```
lower_bound:任意の整数以下の整数の中で最大の数値のインデックスを返す
upper_bound:任意の整数以上の大きい整数の中で最小の数値のインデックスを返す
```

### B11 Binary Search 2
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cj

小さい順に並んでいるとは限らないという文がある。二分探索はソートされた配列にしか使用できないので、先に**sort()**してあげてから、**lower_bound()**で二分探索して、**distance**でインデックスの位置を把握してあげれば解ける

```C++
#include <bits/stdc++.h>

using namespace std;

int main(){
    int N,Q;
    cin >> N;
    vector<int> A(N,0);
    for(int i = 0; i < N; i ++) cin >> A[i];
    sort(A.begin(),A.end());

    cin >> Q;

    for(int i = 0; i < Q; i ++){
        int X;
        cin >> X;

        int ans = distance(A.begin(),lower_bound(A.begin(),A.end(),X));
        cout << ans << endl;
    }

    return 0;
}
```

## 3.2 答えで二分探索
### A12 Printer ★3
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_l

今回は配列自体に二分探索を行うのではなく、配列から計算できる値で二分探索することになる。つまり、任意のN秒の時に作られるチラシの枚数を数える関数を作成して、 $[1,10^9] $秒の範囲で二分探索を行ってあげればよい。
1.  $10^9 \div 2 $ 秒の時のチラシの枚数を数える
2. 大小を判定、範囲を更新
3. 更新した範囲の中央の値でチラシの枚数を数える
4. 2~3を範囲が一意に定まるまで、繰り返す

```C++
#include <bits/stdc++.h>

using namespace std;

unsigned long long count_nums(vector<unsigned long long>& A,unsigned long long sec){
    unsigned long long  count = 0;

    for(int i = 0; i < A.size(); i ++){
        count += sec / A[i];
    }

    return count;
}

int main(){
    unsigned long long N,K;
    cin >> N >> K;
    vector<unsigned long long> A(N,0);
    for(int i = 0; i < N; i ++) cin >> A[i];
    sort(A.begin(),A.end());

    unsigned long long  min_sec = 0;
    unsigned long long  max_sec = 1e9;
    unsigned long long  ans;
    while(max_sec - min_sec > 1){
        unsigned long long  sec = min_sec + (max_sec - min_sec) / 2;
        unsigned long long  nums = count_nums(A,sec);

        if(nums < K ) min_sec = sec + 1;
        else max_sec = sec;
    }

    ans = count_nums(A,min_sec) < K ? max_sec : min_sec;
    cout << ans << endl;  

    return 0;
}
```

### B12 Equation
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ck

今回は範囲が浮動小数点型であることに注意。
式より  $1 \leq x \leq 100 $ であることは自明なので、その範囲で二分探索してあげれば良い。
こういう単調増加関数に対しては二分探索は有効
```C++
#include <bits/stdc++.h>

using namespace std;

double calc_equation(double x){
    return pow(x,3) + x;
}

int main(){
    unsigned long long N,K;
    cin >> N;

    double min_idx = 1;
    double max_idx = 1e2;

    while(true){
        double idx = min_idx + (max_idx - min_idx) / 2;
        double ans = calc_equation(idx);
        if(abs(ans - N) < 1e-3){
            cout << idx << endl;
            return 0;
        }

        if(ans < N){
            min_idx = idx;
        }
        else{
            max_idx = idx;
        }
    }

    return 0;
}
```
### A13 Close Pairs ★4
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_m

こういったソートされている配列から2点を選び、条件に合う2点の取り方の組み合わせを求める問題は**しゃくとり法**を使う事で効率的に解くことができる。
```C++
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
```


# 4章 動的計画
## 4.0 動的計画法とは
**動的計画法**とはより小さい問題の結果を利用して問題を解く方法の総称であり、よくDP(Dynamic Programming)と略して呼ばれる事が多い<br>

例えば以下のような問題があるとする
> あるダンジョンには5つの部屋がある。このダンジョンでは、通路を介して、1つ先または二つ先の部屋に移動することが可能。
> 部屋1から部屋5まで移動するのに、最短何分かかるかを求めよ

![](images/4_DP.png)

この問題を解く最もシンプルな方法は、移動経路全てを全探索する事で今回は部屋の数が5つと少ないので、取りうる経路は以下の5通りしかなく、簡単に求める事ができる<br>
- 1⇒2⇒3⇒4⇒5
- 1⇒2⇒4⇒5
- 1⇒2⇒3⇒5
- 1⇒3⇒4⇒5
- 1⇒3⇒5

しかし、部屋の数が増えると移動経路の数が指数関数的に増加するため、
効率の良い探索方法とは言えない<br>

そこで、いきなり部屋1から5までの最短経路を出すのではなく、以下のような順序で問題を考えてみる事にする
- 部屋1から部屋1までの最短時間dp[1]
- 部屋1から部屋2までの最短時間dp[2]
- 部屋1から部屋3までの最短時間dp[3]
- 部屋1から部屋4までの最短時間dp[4]
- 部屋1から部屋5までの最短時間dp[5]

すると以下のような流れで解くことかできる
1. スタート地点が部屋1なのでdp[1]=0
2. 部屋2に進む経路は1からしかないので、dp[2]=2
3. 1からの経路と2から経路があり、以下の流れでdp[3]=5
   1. 1からの経路は5
   2. 2からの経路はdp[2]+4=6
4. 2からの経路と3からの経路があり、以下の流れでdp[4]=5
   1. 2からの経路はdp[2]+3=5
   2. 3からの経路はdp[3]+1=6
5. 3からの経路と4からの経路があり、以下の流れでdp[5]=8
   1. 3からの経路はdp[3]+7=12
   2. 4からの経路はdp[4]+3=8

このように、dp[1]やdp[2]のように小さい問題の結果を解きその結果を後の計算に利用して順に解いていく手法を**動的計画法**という

## 4.1 動的計画法の基本
### A16 Dungeon1 ★2
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_p

dp[1]=0、dp[2]=A[2]とした上で、dp[3]以降を以下の式で順に計算してあげれば解くことが可能<br>
```
dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i])
```

```C++
#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;

    vector<int> A(N + 1,0);
    for(int i = 2; i <= N; i++){
        cin >> A[i];
    }

    vector<int> B(N + 1,0);
    for(int i = 3; i <= N; i++){
        cin >> B[i];
    }

    vector<int> dp(N + 1,0);
    dp[1] = 0;
    dp[2] = A[2];

    for(int i = 3; i <= N; i ++){
        dp[i] = min(dp[i - 1] + A[i],dp[i - 2] + B[i]);
    }

    cout << dp[N] << endl;

    return 0;
}
```

### B16 Frog 1
問題文:https://atcoder.jp/contests/tessoku-book/tasks/dp_a

A16の問題とほぼ同じ。コストの部分を直せばそのまま解ける
```C++
#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int N;
    cin >> N;

    vector<int> h(N + 1,0);
    for(int i = 1; i <= N; i++){
        cin >> h[i];
    }

    vector<int> dp(N + 1,0);

    dp[1] = 0;
    dp[2] = abs(h[1] - h[2]);

    for(int i = 3; i <= N; i ++){
        dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]),dp[i - 2] + abs(h[i] - h[i - 2]));

    }

    cout << dp[N] << endl;
    return 0;
}
```

## 4.2 動的計画法の復元
### A17 Dungeon2 ★3
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_q

最短経路を求める場合は、DPを求めた後に後ろから順に計算結果が合う経路を辿って行ってあげることで少ない計算量で求める事が可能
```C++
#include <bits/stdc++.h>
using namespace std;
 

int main(){
    int N;
    cin >> N;

    vector<int> A(N + 1,0);
    for(int i = 2; i <= N; i++){
        cin >> A[i];
    }

    vector<int> B(N + 1,0);
    for(int i = 3; i <= N; i++){
        cin >> B[i];
    }

    vector<int> dp(N + 1,0);
    dp[1] = 0;
    dp[2] = A[2];

    for(int i = 3; i <= N; i ++){
        dp[i] = min(dp[i - 1] + A[i],dp[i - 2] + B[i]);
    }

    vector<int> p;
    p.push_back(N);

    int x = N;
    while(x != 1){
        if(dp[x] == dp[x - 1] + A[x]){
            p.push_back(x - 1);
            x = x - 1;
        }
        else{
            p.push_back(x - 2);
            x = x - 2;
        }
    }

    cout << p.size() << endl;
    for(int i = p.size() - 1; i > 0; i --){
        cout << p[i] << " ";
    }
    cout << p[0] << endl;
    
    return 0;
}
```

### B17 Frog 1 with Restoration
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cp

B16の問題をA17と同じ方法で最短経路を探索するだけ

```C++
#include <bits/stdc++.h>
using namespace std;
 

int main(){
    int N;
    cin >> N;

    vector<int> h(N + 1,0);
    for(int i = 1; i <= N; i++){
        cin >> h[i];
    }

    vector<int> dp(N + 1,0);
    dp[1] = 0;
    dp[2] = abs(h[1] - h[2]);

    for(int i = 3; i <= N; i ++){
        dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]),dp[i - 2] + abs(h[i] - h[i - 2]));
    }

    vector<int> p;
    p.push_back(N);

    int x = N;
    while(x != 1){
        if(dp[x] == dp[x - 1] + abs(h[x] - h[x - 1])){
            p.push_back(x - 1);
            x = x - 1;
        }
        else{
            p.push_back(x - 2);
            x = x - 2;
        }
    }

    cout << p.size() << endl;
    for(int i = p.size() - 1; i > 0; i --){
        cout << p[i] << " ";
    }
    cout << p[0] << endl;

    return 0;
}
```

## 4.3 二次元のDP(1):部分和問題
### A18 Subset Sum ★3
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_r

数字のかかれたN枚のカードを用いて合計Sになるようなカードの選択方法があるかを判定する問題
一番シンプルにやるのであればbit全探索ですべての通りを試すのだが、これだとO(2^N)となり、非常に計算量が膨大

そこで以下のように考える
1. カードが1枚の時は、そのカードを取るか取らないかの二択なので、０とカードに書かれている数字A1にチェック
2. カードが2枚の時、1枚の時の数字はそのまま引き継ぎ、その数字をベースに数字A2を足したところにチェック
3. カードが3枚の時、2枚の時の数字はそのまま引き継ぎ、その数字をベースに数字A3を足したところにチェック
4. カードがi枚の時、i-1枚の時の数字はそのまま引き継ぎ、その数字をベースに数字Aiを足したところにチェック

このように一つ前までに作れる数字はそのカードが無くても作れるので、その数字をベースにカードを取る場合だけを考えて上げればよい。<br>
これを繰り返すと、最終的にN枚のカードから作れる全ての数字を求める事ができる

イメージとしては以下のような感じ

![](images/4_2DDP1.png)
![](images/4_2DDP2.png)

```C++
#include <bits/stdc++.h>
using namespace std;
 

int main(){
    int N,S;
    cin >> N >> S;

    vector<int> A( N + 1, 0);
    for(int i = 1; i <= N; i ++) cin >> A[i];

    vector<vector<bool>> dp(N + 1,vector<bool>(S + 1,false));

    for(int i = 1; i <= N; i ++){
        if(A[i] <= S){
            dp[i][A[i]] = true;
        }
        
        for(int j = 1; j <= S; j ++){
            if(dp[i - 1][j]){
                dp[i][j] = true;
                if(j + A[i] <= S){
                    dp[i][j + A[i]] = true;
                }
            }
        }
    }

    if(dp[N][S]){
        cout << "Yes" << endl;
        return 0;
    }

    cout << "No" << endl;
    return 0;
}
```

### B18 Subset Sum with Restoration
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cq

基本的にはA17のようにdpでSとなる組合わせがあるかどうかを確認した後、その結果から順に取得するべきかを選択していく事で求めることができる<br>

具体的には、以下のような感じ
1. 現在の最大値Sに対して、以下の条件を満たすiを探す
   1. dp[i][S]が負
   2. dp[i][S - A[i+1]]が正
2. i+1を配列に格納
3. S = S - A[i+1]を代入
4. S = 0になるまで、1~3の操作を繰り返す

dp[i][S]が負かつ、dp[i][S - A[i+1]]の時、A[i+1]がSにするために必要な要素であることが分かる<br>
その後は現在の最大値SをS - A[i+1]に更新して、同様に繰り返す事で最終的にSにするために必要なカードの番号の組み合わせを算出することが可能となる


```C++
#include <bits/stdc++.h>
using namespace std;
 

int main(){
    int N,S;
    cin >> N >> S;

    vector<int> A( N + 1, 0);
    for(int i = 1; i <= N; i ++) cin >> A[i];

    vector<vector<bool>> dp(N + 1,vector<bool>(S + 1,false));
    dp[0][0] = true;
    for(int i = 1; i <= N; i ++){
        dp[i][0] = true;
        if(A[i] <= S){
            dp[i][A[i]] = true;
        }
        
        for(int j = 1; j <= S; j ++){
            if(dp[i - 1][j]){
                dp[i][j] = true;
                if(j + A[i] <= S){
                    dp[i][j + A[i]] = true;
                }
            }
        }
    }

    if(dp[N][S]){
        vector<int> ans;
        int current_max = S;
        for(int i = N - 1; i >= 0; i --){
            if((!dp[i][current_max] && dp[i][current_max - A[i + 1]])){
                ans.push_back(i + 1);
                current_max = current_max - A[i + 1];

                if(current_max == 0){
                    break;
                }
            }
        }

        cout << ans.size() << endl;
        for(int i = ans.size() - 1; i > 0; i --){
            cout << ans[i] << " ";
        }
        cout << ans[0] << endl;
    }
    else{
        cout << -1 << endl;
    }

    return 0;
}
```

## 4.4 二次元のDP(2):ナップザック問題
### A19 Knapsack1 ★3
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_s

いわゆる**ナップザック問題**とよばれるDPの代表的問題<br>
N個の物があり、それぞれの荷物の重さはwiで価値viが付けられている。ナップザックに入る重さは最大でWの時、
その中で価値が最大になるように物を選び、その価値の最大値を求めるというもの<br>

基本的な考え方はA18の応用で、チェックを付けていたのを数字に置き換えてあげれば良い
1. dp[0][0]に0を付けて、その他は×をつける(プログラム的には物の価値の最大値より大きい負の数字を入れると楽)
2. ```1 <= i```以降は```0 <= j <= w```の範囲で
   1. ```j < wi```の時は、荷物が入らないのでそのまま以前の結果を引き継ぐ
   2. ```wi <= j```の時は、```dp[i - 1][j]```と```dp[i - 1][j - weight] + vi```を比較し大きい方を記録する。
   (この時に最初に十分い大きい負の数字を設定した場合、その重さの組み合わせは取りえない場合にそのまま負の状態になるため管理が楽)

イメージとしては以下のような感じ

![](images/4_napsack1.png)
![](images/4_napsack2.png)
```C++
#include <bits/stdc++.h>
using namespace std;
 

int main(){
    int N,W;
    cin >> N >> W;
    vector<vector<long long>> napsacks(N + 1,vector<long long>(2,0));
    for(int i = 1; i <= N; i ++) cin >> napsacks[i][0] >> napsacks[i][1];

    vector<vector<long long>> dp(N + 1,vector<long long>(W + 1,10e-10));
    dp[0][0] = 0;

    for(int i = 1; i <= N; i++){
        long long  weight = napsacks[i][0];
        long long value = napsacks[i][1];
        for(int j = 0; j <= W; j ++){
            if(dp[i - 1][j] >= 0){
                if( j < weight) dp[i][j] = dp[i - 1][j];
                else {
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value);
                }
            }
        }
    }

    long long max = 0;
    for(int i = W; i >= 0; i --){
        if(dp[N][i] > max){
            max = dp[N][i];
        }
    }

    cout << max << endl;
    return 0;
}
```

### B19 knapsack2
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cr

A19と違い、今度はWの数が膨大になっている。<br>
この場合にA19と同様のDP配列を作ると、```N * 10^9```個の配列について考えなければいけないので、探索量が多くなってしまう。<br>
このような場合は、逆転して価値viについての最小となるWiの組み合わせを見つけあげることで解決が短時間で処理<br>
今回はWの最大値が```10^9```であるのに対して、価値の最大値は```1000 * N <= 10^5```であるため、Wに対するdp表を作るよりも短い探索回数で最適解を求める事ができる、

```C++
#include <bits/stdc++.h>
using namespace std;
 

int main(){
    int N,W;
    cin >> N >> W;
    vector<vector<long long>> napsacks(N + 1,vector<long long>(2,0));
    for(int i = 1; i <= N; i ++) cin >> napsacks[i][0] >> napsacks[i][1];

    vector<vector<long long>> dp(N + 1,vector<long long>(1000 * N + 1,LONG_LONG_MAX));
    dp[0][0] = 0;

    for(int i = 1; i <= N; i++){
        long long  weight = napsacks[i][0];
        long long value = napsacks[i][1];
        for(int j = 0; j <= 1000 * N; j ++){
            if(dp[i - 1][j] >= 0){
                if( j < value) dp[i][j] = dp[i - 1][j];
                else {
                    long long first = dp[i - 1][j] != LONG_LONG_MAX ? dp[i - 1][j] : LONG_LONG_MAX;
                    long long second = dp[i - 1][j - value] != LONG_LONG_MAX ? dp[i - 1][j - value] + weight : LONG_LONG_MAX;
                    dp[i][j] = min(first, second);
                }
            }
        }
    }

    long long max = 0;
    for(int i = 1000 * N; i >= 0; i --){
        if(dp[N][i] <= W){
            max = i;
            break;
        }
    }

    cout << max << endl;
    return 0;
}
```

## 4.5 二次元のDP(3):最長共通部分列問題
### A20 LSC ★4
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cr

配列の最長共通部分列を求める問題でもDPが使える。<br>

※ そもそも最長共通部分列とは?<br>
ある文字列から**順番を変えずに**一部の文字を取り出した物を**部分列**と呼ぶ<br>
```
例) mynavi ⇒　mnv,mna,yna,avi,mai...など
    monday ⇒  mny,mna,ond,day...など
```
最長共通部分列とは二つの文字列から部分列を生成した時、それが同じになるものを**共通部分列**と呼ぶ。上の例だと```mna```がそれにあたる<br>
その中で最も長い部分列を見つける問題である。<br>

この問題を解くには2段階の理解が必要<br>
- Step1 二つの文字列からなるマス目を考える<br>
文字列とマス目は全く関係内容に思えるが、以下のようなマス目を考えると一気に分かりやすくなる。<br>
![](images/4_LCS1.png)<br>
このように```tokyo```を行方向、```kyoto```を列方向に見立てたマス目を考える。矢印は各文字列おいて、進められる方向を示しており、二つの文字列の文字が一致する部分に限り、左上から赤い矢印方向に進む事ができる。<br>
この赤い矢印がついてる文字は二つの文字列の共通部分列になりうる文字を示しているので、(0,0)の座標から始まり、(5,5)の座標に至るまでに**一番多く赤い矢印を通るような経路**を選択することができれば、その矢印の数から最長共通部分列を求める事が可能となる。<br>
ちなみにこの例の場合は以下のような経路をが最長となる<br>
![](images/4_LSC2.png)

- STEP2 動的計画法を考える
赤い矢印を一番多く通る経路が最長になることは分かったので、次にどうやって一番多く通る経路を調べる事ができるかを考える。<br>
今回のDPは以下のように考える事ができる<br>
```
dp[i][j] ： マス(i,j)に到達するまでに通る、赤い矢印の本数の最大値
```
マス(i,j)に遷移するための移動方法は主に以下の3つ
|移動方法|通る赤い矢印の本数|
|---|---|
|マス(i - 1, j)から青矢印で移動|青矢印なので、数は増えないのでdp[i-1][j]の本数を引き継ぐ|
|マス(i, j - 1)から青矢印で移動|青矢印なので、数は増えないのでdp[i][j - 1]の本数を引き継ぐ|
|マス(i - 1, j - 1)から赤矢印で移動|赤矢印を通るため、1本足して、dp[i - 1][j - 1] + 1|

この移動方法の中で、最大の本数を選んで行くことで、dp[5][5]にたどり着く経路の中で最大の本数を調べることができる。<br>
赤矢印がある経路は文字が一致する場合だけなので、そこのチェックを忘れないように注意する事<br>
このような流れで、DPで解くと、以下のような結果になる<br>
![](images/4_LSC_ans.png)

```C++
#include <bits/stdc++.h>
using namespace std;
 
int main(){
    string S,T;
    cin >> S >> T;

    vector<vector<int>> dp(S.size() + 1,vector<int>(T.size() + 1,0));

    for(int i = 1; i <= S.size(); i ++){
        for(int j = 1; j <= T.size(); j ++){
            if(S[i - 1] == T[j - 1]){
                dp[i][j] = max({dp[i - 1][j],dp[i][j - 1],dp[i - 1][j - 1] + 1});
            }
            else {
                dp[i][j] = max({dp[i - 1][j],dp[i][j - 1]});
            }
        }
    }

    cout << dp[S.size()][T.size()] << endl;
    return 0;
}
```

### B20 Edit Distance
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cs

これは[編集距離(レーベンシュタイン距離)](https://mathwords.net/hensyukyori)を算出する問題。<br>
編集距離というのは二つの文字列がどれだけ似ているのかを示す距離で、0に近い程、二つの文字が似ている事を示している。<br>
具体的には以下の3つの操作のいずれかを実行して、片方の文字を編集していき、最低何回の編集回数で文字列を一致させる事ができるかを考える。<br>
- 一文字挿入
- 一文字削除
- 一文字置換

この問題についてもDPを適用して解くことが可能。<br>

- Step1 文字列をマス目として考える<br>
A20のLCSと同様にマス目のように考える。
今回も```tokyo```と```kyoto```の二つの文字列について考える<br>
![](images/4_%E7%B7%A8%E9%9B%86%E8%B7%9D%E9%9B%A21.png)

- Step2 1行目と1列目を埋める<br>
空白文字とのn文字の文字列の編集距離は```n```なので、1行目と1列目が埋まる<br>
![](images/4_%E7%B7%A8%E9%9B%86%E8%B7%9D%E9%9B%A22.png)

- Step3 左上から順にi行目とj列目の編集距離を計算する<br>
各マスには以下の条件の中で最小の数字を挿入していく
  - 上のマスの数字 + 1
  - 左のマスの数字 + 1
  - 左上のマスの数字 + c (このマスの縦と横の文字が同じ場合c=0 異なる場合c=1)<br>

例えば(1,1)のマス目について考えると、
- マス(0,1) + 1 = 2
- マス(1,0) + 1 = 2
- マス(0,0) + 1 = 1<br>

なので(1,1)には1を代入する。<br>
実際に```t```と```k```の編集距離は置換一回ですむので、編集距離は1である。同じ操作を順に実行していくと最終的に以下のようにマスを埋める事ができる<br>
![](images/4_%E7%B7%A8%E9%9B%86%E8%B7%9D%E9%9B%A23.png)

このようにすることで、最終的に```kyoto```と```tokyo```の編集距離が4であることを求める事ができる。計算量もO(NM)と十分に高速である<br>

```C++
#include <bits/stdc++.h>
using namespace std;
 

int main(){
    string S,T;
    cin >> S >> T;

    vector<vector<int>> dp(S.size() + 1,vector<int>(T.size() + 1,0));

    for(int i = 0; i <= S.size(); i ++){
        dp[i][0] = i;
    }

    for(int i = 1; i <= T.size(); i ++){
        dp[0][i] = i;
    }

    for(int i = 1; i <= S.size(); i ++){
        for(int j = 1; j <= T.size(); j ++){
            if(S[i - 1] == T[j - 1]){
                dp[i][j] = min({dp[i - 1][j] + 1,dp[i][j - 1] + 1,dp[i - 1][j - 1]});
            }
            else {
                dp[i][j] = min({dp[i - 1][j] + 1,dp[i][j - 1] + 1,dp[i - 1][j - 1] + 1});
            }
        }
    }

    cout << dp[S.size()][T.size()] << endl;
    return 0;
}
```

## 4.6 二次元のDP(4):区間DP
### A21 Block Game ★4
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_u

この問題ではどんな操作をしても、残るブロックは連続した番号になることに注目する(1,2,3と残ることは合っても,1,2,4の様に一つ抜けるような事はない)<br>
この時のDPの考え方は区間i(1 <= i <= N) ~ j (i <= j <= N)の区間における最大値dp[i][j]を計算する問題として考える<br>

1. 始めの状態では、dp[1][N]は何も削っていないので当然dp[1][N] = 0;
2. 次にi = 1を固定して、jをN-1から順にiまで減らしていきながら順にdp[1][j]を計算していく<br>
dp[i][j]になるには以下の二つのパターンの操作が考えられる
   - dp[i - 1][j]の状態からi - 1のブロックを削り、i <= P[i - 1] <= j の時、A[i - 1]を加算
   - dp[i][j + 1]の状態からj + 1のブロックを削り、i <= P[j + 1] <= j の時、A[j + 1]を加算<br>
この二つの操作の内スコアが高い方を選ぶことで、区間i~jに置けるスコアの最大値を計算することが可能
3. i = 2 ... Nについても同様に2の操作を繰り返していく

そうすると最終的に以下のようなイメージでスコアの取りうる最大値を求める事が可能<br>
![](images/4_range_DP.png)


```C++
#include <bits/stdc++.h>
using namespace std;
 

int main(){
    int N;
    cin >> N;

    vector<int> P(N + 2,0);
    vector<int> A(N + 2,0);

    for(int i = 1; i <= N; i ++) cin >> P[i] >> A[i];

    vector<vector<int>> dp(N + 1,vector<int>(N + 2,0));
    dp[1][N] = 0;

    for(int i = 1; i <= N; i ++){
        for(int j = N; j >= i; j --){
            int score_l = (i <= P[i - 1]) && (P[i - 1] <= j) ? A[i - 1] : 0;
            int score_r = (i <= P[j + 1]) && (P[j + 1] <= j) ? A[j + 1] : 0;
            dp[i][j] = max({dp[i - 1][j] + score_l, dp[i][j + 1] + score_r});
        }
    }

    int max = 0;
    for(int i = 1; i <= N; i ++){
        for(int j = 1; j <= N; j ++){
            if(max < dp[i][j]){
                max = dp[i][j];
            }
        }
    }

    cout << max << endl;
    return 0;
}
```

### B21 Longest Subpalindrome
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ct

今回は文字列Sからいくつかの文字を削って作れる最長の回文文字列を求める問題<br>
削る操作だけなので、区間S[l][r]の時に作れる最長の回文文字列を解くDP問題としてといて上げればよい<br>

- 手順<br>
1. 区間の長さが1の時はそのまま回文になるので```dp[i][i] = 1```
2. 区間の長さが2の時は二つの文字が同じであれば回文なので```dp[i][i+1]=2```、違うなら削って1になるので```dp[i][i+1] = 1```
3. 区間の長さが3以上の時、以下の遷移パターンを考える
   - ```S[l] == S[r]```の時は、```S[l + 1] ~ S[r - 1]```から作れる回文の最長文字長に+2
   - S[l]を削る場合は、```S[l + 1] ~ S[r]```から作れる最長文字長と同じになる
   - S[r]を削る場合は、```S[l] ~ S[r - 1]```から作れる最長文字列と同じになる<br>
4. 3の操作を区間の長さ3,4,5~と繰り返す事で区間0~Nの文字列から作れる回文の最長文字列長が求まる


```C++
#include <bits/stdc++.h>
using namespace std;
 

int main(){
    int N;
    cin >> N;

    string S;
    cin >> S;

    vector<vector<int>> dp(N,vector<int>(N));

    //1文字の時の初期化
    for(int i = 0; i < N; i ++) dp[i][i] = 1;

    //2文字の時の初期化
    for(int i = 0; i < N - 1; i ++){
        if(S[i] == S[i + 1]) dp[i][i + 1] = 2;
        else dp[i][i + 1] = 1;
    }

    //3文字以降は以下の条件で解くことができる
    //①　S[l] == S[r]の時、S[i + 1]~S[r - 1]の文字列から作れる回文の最長文字長+2
    //②  S[l] != S[r]の時、以下の二つの条件に分岐する
    //    - S[l]を削った場合、回文の最長文字長はS[l+1] ~ S[r]の最長文字長
    //    - S[r]を削った場合、回文の最長文字長はS[l] ~ S[r-1]の最長文字長
    //この条件の中で最大になるものを選択してあげればよい
    //この操作を3,4,5と長さを伸ばして実行することで以前の結果を利用して計算が行える

    for(int LEN = 2; LEN < N; LEN ++){
        for(int l = 0; l < N - LEN; l++){
            int r = l + LEN;
            if(S[l] == S[r]){
                dp[l][r] = max({dp[l + 1][r - 1] + 2,dp[l + 1][r], dp[l][r - 1]});
            }
            else{
                dp[l][r] = max({dp[l + 1][r], dp[l][r - 1]});
            }
        }
    }

    cout << dp[0][N -1] << endl;


    return 0;
}
```

# 5章 数学的問題
## 5.0 数学的問題について
 $2^8 $ の計算を高速に行うにはどうしたらよいか<br>
単純に解く場合、2×2×2×2×2×2×2×2を順に計算すれば解くこと自体はできるが、7回の掛け算が必要になる<br>
しかし,  $2^8=4^4=16^2 $ であることを利用すると、計算結果を流用することで2×2=4、4×4=16、16×16=256の3回の掛け算で答えを求める事が可能になる<br>
このように、数学的な見た目の問題にもアルゴリズムが役立つ。そのため競プロではこういった問題がたびたび出題される。この章ではそういった頻出の「数学的なテクニック」を10個の節に分けて説明する

## 5.1 素数判定
### A26 Prime Check ★2
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_z

素数判定を行う問題。素数を判定する場合、  $\sqrt{X} $ 以上の数は考慮しなくてよいのでそれを用いることでより効率的に計算可能<br>
```C++
#include <bits/stdc++.h>
using namespace std;
 
bool isPrime(int x){
    auto sx = sqrt(x);

    for(int i = 2; i <= sx; i ++){
        if(x % i == 0) {return false;}
    }

    return true;
}
 
int main(){
    int Q;
    cin >> Q;

    vector<int> X(Q);

    for(int i = 0; i < Q; i ++){
        cin >> X[i];
    }

    for(int i = 0; i < Q; i ++){
        if(isPrime(X[i])){
            cout << "Yes" << endl;
        }
        else{
            cout << "No" << endl;
        }
    }


    return 0;

}
```

### B26 Output Prime Numbers 
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cy

N以下の素数を全て求める問題。この問題は**エラストテネスのふるい**というアルゴリズムで効率的に解くことが可能<br>
手順
1. 2~Nまでの素数かどうかの結果を格納する配列を作成
2. 初期値i=2として2の倍数を全て消去
3. 配列を確認して、iの次に大きい消去されていない数をiに代入(この場合3)
4. 2と同様に3の倍数を全て消去
5. 以下3~4をi=Nになるまで繰り返す

このように素数の小さい順に倍数を予め消していく事で、効率的にN以下までの素数を求める事ができる<br>計算量は $O(N \log \log N) $である事が知られており、大体 $O(N) $程度の速さになる

![](images/5_%E3%82%A8%E3%83%A9%E3%82%B9%E3%83%881.png)
![](images/5_%E3%82%A8%E3%83%A9%E3%82%B9%E3%83%882.png)

```C++
#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int N;
    cin >> N;

    vector<bool> primes(N + 1,true);
    primes[0] = primes[1] = false;

    for(int i = 2; i <= N; i ++){
        if(!primes[i]) continue;
        cout << i << endl;
        for(int j = i * 2; j <= N; j += i){
            primes[j] = false;
        }
    }

    return 0;
}
```

## 5.2 最大公約数
### A27 Calculate GCD ★2
問題文:https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_o

二つの整数A,Bの最大公約数を求める問題。**ユークリッドの互除法**で解くことが可能。
1. 二つの数の大きい方に対して小さい方で割った余りを計算
2. 大きい方の数に余りの値を代入して、1を繰り返す
3. 余りが0になった時にもう片方の数が最大公約数であることが分かる

このアルゴリズムは小さい数から順に全ての数で割り切れるかどうかを調べるよりもはるかに高速であることが分かる<br>
![](images/5_%E3%83%A6%E3%83%BC%E3%82%AF%E3%83%AA%E3%83%83%E3%83%89.png)

```C++
#include <bits/stdc++.h>
using namespace std;

int gcd(int a,int b){
    int mod = a % b;
    if(mod == 0) return b;
    else return gcd(b,mod);
}
 
int main(){
    int A,B;
    cin >> A >> B;

    cout << gcd(A,B) << endl;
    return 0;
}
```

### B26 Calculate LCM
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cz

今度は最小公倍数( $LCM $)を求める問題。しかしこちらは最大公約数( $GCD $)の結果を使う事で簡単に解くことが可能<br>
二つの整数A,Bの最大公約数 $gcd $がある時、A,Bはそれぞれ以下のように表せる<br>

 $A = gcd \times A固有の素因数の積　B = gcd \times B固有の素因数の積 $<br>
 $LCM = gcd \times A固有の素因数の積 \times B固有の素因数の積 $<br>
したがって以上の関係性から、 $A\times B \div gcd $で最小公倍数 $LCM $を計算することが可能となる<br>

```C++
#include <bits/stdc++.h>
using namespace std;
#define ULLong unsigned long long
#define ULong unsigned long
#define LLong long long
#define Long long

ULLong gcd(ULLong a,ULLong b){
    int mod = a % b;
    if(mod == 0) return b;
    else return gcd(b,mod);
}

ULLong lcm(ULLong a,ULLong b){
    return a / gcd(a,b) * b;
} 
 
int main(){
    ULLong A,B;
    cin >> A >> B;

    cout << lcm(A,B) << endl;
    return 0;
}
```


## 5.3 余りの計算(1):基本
### A28 Blackboards ★2
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ab

各計算過程での10000で割った時の余りを求める問題<br>
そのまま馬鹿正直に計算すると途中でオーバーフローを起こしてしまうため、工夫する必要がある<br>
余りの性質として、**足し算、引き算、掛け算においては好きなタイミングで余りをとっても答えが変わらない**性質がある。
それを利用して各計算の後に今ある数を10000で割った余りを代入してあげることでオーバーフローを防ぐ事が可能<br>
ただし、引き算だけは負の値になってしまう可能性があるので、その場合には10000を加算することで、余りを変えずに正の値に戻して上げる必要がある

```C++
#include <bits/stdc++.h>
using namespace std;
#define ULLong unsigned long long
#define ULong unsigned long
#define LLong long long
#define Long long
 
int main(){
    ULLong N;
    cin >> N;;

    int ans = 0;
    for(int i = 0; i < N; i ++){
        char t;
        int a;
        cin >> t >> a;

        switch (t)
        {
        case '+':
            ans += a;
            break;
        case '-':
            ans -= a;
            if(ans < 0) ans += 10000;
            break;
        case '*':
            ans *= a;
            break;
        
        default:
            break;
        }
        ans = ans % 10000;
        cout << ans << endl;
    }

    return 0;
}
```

### B28 Fibonacci Easy (mod 1000000007)
問題文:https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_ap

基本的にはA28の問題と同様の性質を活用して計算する。<br>
フィボナッチ数列は二つ前と一つ前の数字を足した数の数列であるが、常に算出した値の余りを計算するようにして、その余り同士を足し合わせる事でオーバーフローを防げる。

```C++
#include <bits/stdc++.h>
using namespace std;
#define ULLong unsigned long long
#define ULong unsigned long
#define LLong long long
#define Long long

int main(){
    ULLong N;
    cin >> N;

    ULLong mod = 1e9 + 7;

    ULLong a1 = 1;
    ULLong a2 = 1;
    ULLong a3;
    for(int i = 3; i <= N; i ++){
        a3 = a1 + a2;
        a1 = a2;
        a2 = a3 % mod;
    } 

    cout << a2 << endl;

    return 0;
}
```

## 5.4 余りの計算(2)：累乗
### A29 Power ★3
問題文:https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_aq

そのままシンプルに解くことを考えると、bの数まで順にaをかけていけば良いが、これだと時間切れになる<br>
そこで,5.0節でやったような考え方で高速に計算することを考える。<br>
例えば  $a^{13} $ を計算することを考えると、通常13回の掛け算が必要だが、
-  $a^1 \times a^1 = a^2 $ を計算
-  $a^2 \times a^2 = a^4 $ を計算
-  $a^4 \times a^4 = a^8 $ を計算
-  $a^8 \times a^4 \times a^1 = a^13 $ を計算<br>
というように計5回の掛け算で計算することが可能

またオーバーフローについては前回の掛け算では好きなタイミングで余りをとっても答えは変わらない性質を用いて、適宜計算タイミングでmodを計算しておくことで防ぐ事ができる<br>

```C++
#include <bits/stdc++.h>
using namespace std;
#define ULLong unsigned long long
#define ULong unsigned long
#define LLong long long
#define Long long

/*b = 7 とすると、a^7 = a^4 * a^2 * a^1に分けて計算するイメージ*/
ULLong power(ULLong a, ULLong b,ULLong mod){
    ULLong p = a, answer = 1;
    for(int i = 0; i < 30; i ++){
        int wari = (1 << i);
        int tmp = (b/wari);
        if(tmp == 0) break;
        if(tmp % 2 == 1){
            answer = (answer * p) % mod;
        }
        p = (p * p) % mod; 
    }
    return answer;
}

 
int main(){
    ULLong a,b;
    cin >> a >> b;

    ULLong mod = 1e9 + 7;
    cout << power(a,b,mod) << endl;

    return 0;
}
```

### B29 Power Hard
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_db

基本的にはA29と同じだが、bの制約がかなり大きくなっている。A29の時はi=32で計算できる範囲だったが、これを更に拡張する必要がある。while文に変更して途中でbreakできるように実装することで、i=64まで対応可能にした。<br>
注意点としてはシフト演算子の型に気をつける必要がある。そのまま1としてしまうとint型になってしまうので、31以上の計算ができない。1ULLとしてunsigned long long型として定義してあげる必要があることを忘れないように

```C++
#include <bits/stdc++.h>
using namespace std;
#define ULLong unsigned long long
#define ULong unsigned long
#define LLong long long
#define Long long

/*b = 7 とすると、a^7 = a^4 * a^2 * a^1に分けて計算するイメージ*/
ULLong power(ULLong a, ULLong b,ULLong mod){
    ULLong p = a, answer = 1;
    int i = 0;
    while(true){
        ULLong wari = (1ULL << i);
        ULLong tmp = (b/wari);
        if(tmp == 0) break;
        if(tmp % 2 == 1){
            answer = (answer * p) % mod;
        }
        p = (p * p) % mod;
        i++;
    }
    return answer;
}

 
int main(){
    ULLong a,b;
    cin >> a >> b;

    ULLong mod = 1e9 + 7;
    cout << power(a,b,mod) << endl;

    return 0;
}
```

## 5.5 余りの計算(3):割り算
### A30 Combination ★4
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ad

足し算、引き算、掛け算については計算過程のどのタイミングでmodをとっても答えは変わらないが、割り算の場合はそうはいかない。<br>
割り算の場合は以下の性質があることの把握する必要がある
>Mを素数として、bをMで割り切れない整数であるとする。この時、Mで割った余りを求める問題では「  $\div b $ 」を「  $\times b^{M - 2} $ 」と変換しても答えは変わらない

この性質の証明は難しいので、詳しくは説明しないが、**フェルマーの小定理**が深く関連している。

実際にこの性質を使用して問題を解く場合以下のような流れで処理を行う.<br>
例)  $12 \div 3 $ を5で割った余りを求める
1. 分母分子を5で割った余りを求める  $2 \div 3 $
2.  $\div 3 $ を  $\times 3^{5-2} $ に変更　 $2 \times 3^{5-2} $
3. 直接計算 54
4. 実際に余りをとる 5

直接計算とあるが、「  $\times b^{M - 2} $ 」に変更した後は好きなタイミングで余りを取れるので、  $b^{M - 2} $ の余りを5.4節の累乗の余りの計算方法で先に計算してあげると楽に計算できる
```C++
#include <bits/stdc++.h>
using namespace std;
#define ULLong unsigned long long
#define ULong unsigned long
#define LLong long long
#define Long long

ULLong power(ULLong a, ULLong b,ULLong mod){
    ULLong p = a, answer = 1;
    int i = 0;
    while(true){
        ULLong wari = (1ULL << i);
        ULLong tmp = (b/wari);
        if(tmp == 0) break;
        if(tmp % 2 == 1){
            answer = (answer * p) % mod;
        }
        p = (p * p) % mod;
        i++;
    }
    return answer;
}
 
int main(){
    ULLong n,r;
    cin >> n >> r;

    ULLong mod = 1e9 + 7;

    ULLong a = 1;
    for(int i = 1; i <= n; i ++){
        a *= i;
        a = a % mod;
    }

    ULLong b = 1;
    for(int i = 1; i <= r; i ++){
        b *= i;
        b = b % mod;
    }

    for(int i = 1; i <= (n - r); i ++){
        b *= i;
        b = b % mod;
    }

    ULLong ans = (a * power(b,mod - 2,mod)) % mod;
    cout << ans << endl;

    return 0;
}
```

### B30 Combination2
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_dc

A30とほぼ同じ解法で解ける。ようは定式化ができるかどうかの問題<br>
(1,1)の座標から(H,W)まで行くのに、H方向への移動がH-1回、W方向への移動をW-1回の計W+H-2回の移動を行う。その中でどの順序で移動しても良いので、総移動回数H+W-2回の移動の中でHまたはW方向へ移動するタイミングの組み合わせを考えて上げれば良い<br>
つまり、  $_{H+W-2}C_{H - 1} $ か  $_{H+W-2}C_{W - 1} $ についてA30と同様の方法で解いて上げればよい<br>

```C++
#include <bits/stdc++.h>
using namespace std;
#define ULLong unsigned long long
#define ULong unsigned long
#define LLong long long
#define Long long

ULLong power(ULLong a, ULLong b,ULLong mod){
    ULLong p = a, answer = 1;
    int i = 0;
    while(true){
        ULLong wari = (1ULL << i);
        ULLong tmp = (b/wari);
        if(tmp == 0) break;
        if(tmp % 2 == 1){
            answer = (answer * p) % mod;
        }
        p = (p * p) % mod;
        i++;
    }
    return answer;
}
 
int main(){
    ULLong H,W;
    cin >> H >> W;
    ULLong mod = 1e9 + 7;

    ULLong a = 1;
    for(int i = 1; i <= (H + W - 2); i ++){
        a *= i;
        a = a % mod;
    }

    ULLong b = 1;
    for(int i = 1; i <= (H - 1); i ++){
        b *= i;
        b = b % mod;
    }

    for(int i = 1; i <= (W - 1); i ++){
        b *= i;
        b = b % mod;
    }

    ULLong ans = (a * power(b,mod - 2,mod)) % mod;
    cout << ans << endl;

    return 0;
}
```

## 5.6 包除原理
### A31 Divisors ★2
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ae

```C++
```

# 6章 考察テクニック

# 7章 ヒューリスティック

# 8章 データ構造とクエリ処理

# 9章 グラフアルゴリズム
## 9.0 グラフとは
多くの人は棒グラフや折れ線グラフなどの資料作成のツールを想像すると思うが、アルゴリズムの文脈ではモノとモノを結ぶネットワーク構造を**グラフ**という<br>
グラフは頂点と辺からできており、頂点はモノを表し、辺はつながりを表している<br>
![](images/9_%E3%82%B0%E3%83%A9%E3%83%95%E4%BE%8B.png)

**グラフの分類1 無向グラフ、有向グラフ**<br>
グラフの辺の向きの有無があるかどうかで変わる。<br>
**無向グラフ**には辺同士の方向がなく、両方の頂点を行き来できるが、**有向グラフ**は辺同士に方向の関係性があるため、一方通行となっている
|グラフの種類|使用例|
|---|---|
|無向グラフ|一般的な道路網、友人関係|
|有向グラフ|一方通行、流れ|

![](images/9_無向グラフと有向グラフ.png)

**グラフの分類2 重みなしグラフと重み付きグラフ**<br>
グラフには辺に重みや長さの情報がついているケースもある。<br>
**重みなしグラフ**には辺に重みが設定されていないが、**重み付きグラフ**には辺に重みがある<br>
|グラフの種類|使用例|
|---|---|
|重みなしグラフ|道路網や路線図|
|重み付きグラフ|道路網や路線図に所要時間、料金、移動距離などを設定|

グラフを日常的に使う例として以下のものがある

![](images/9_グラフの使用例.png)

その他覚えるべき用語集
|用語|説明|
|---|---|
|次数|ある頂点に接続している辺の本数。有向グラフの場合、出る本数を出次数、入る本数を入次数と呼ぶ|
|連結・隣接関係|グラフが連結であるということは頂点間が行き来可能であることを示す。隣接は二つの頂点が辺で結ばれている状態を示す|
|パス・閉路|グラフ上の経路のことをパスと呼び、同じ頂点を複数回通らないパスのことを単純パスと呼ぶ。スタートとゴールが同じパスの中で、同じ辺を二度と通らずなおかつ、ゴール時を除いて同じ頂点を通らない経路を閉路と呼ぶ|
|二部グラフ|隣接している頂点が同じ色にならないように、グラフの頂点を青と赤などの2色で塗分けることが可能なグラフを二部グラフという。二部グラフを用いると「長さが奇数である閉路が存在しなかったり、マッチング問題(9.9節)を容易に解くことが可能|
|最短経路|ある頂点からある頂点に向かうパスの内、通る辺の本数(重み付きグラフの場合は重みの総和)が最小となるものを最短経路と呼ぶ|
|木構造|連結な無向グラフの内、閉路が存在しないもの。どの様な木でも頂点をNとするとき辺の本数がN-1となる|

## 9.1 グラフの実装方法
### A61 Adjacent Vertices
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bi<br>
コンピュータ上でグラフを表現する方法には**隣接行列表現**と**隣接リスト表現**の二つがある

- 隣接行列表現  
辺があるかないかの情報をN×Nの二次元配列を用いて表現する方法で辺があるところに1、ない所に0を記入する  
![](images/9_%E9%9A%A3%E6%8E%A5%E8%A1%8C%E5%88%97.png)

- 隣接リスト表現  
各頂点に対して「隣接する頂点のリスト」だけを記録する方法。具体的には頂点vと隣接している頂点のリストをG[v]に記録していく  
![](images/9_%E9%9A%A3%E6%8E%A5%E3%83%AA%E3%82%B9%E3%83%88.png)

メモリ使用料の観点から、**隣接リスト**の方が優れているため、基本的には隣接リスト形式を採用する

```C++
#include <bits/stdc++.h>
using namespace std;
 

int main(){
    int N,M;
    cin >> N >> M;

    vector<set<int>> g(N + 1);
    for(int i = 0; i < M; i ++){
        int a,b;
        cin >> a >> b;
        g[a].insert(b);
        g[b].insert(a);
    }

    for(int i = 1; i <= N; i ++){
        cout << i << ": {";
        if(g[i].empty()){
            cout << "}" << endl;
            continue;
        }

        auto itr = g[i].begin();
        auto stop_itr = g[i].end();
        stop_itr --;
        while(itr != stop_itr){
            cout << *itr << ",";
            itr ++;
        }
        cout << *itr << "}" << endl;
    }

    return 0;
}
```
### B61 Influencer
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_eh
生徒を頂点、友人関係を辺として最大の次数の人を出力

```C++
#include <bits/stdc++.h>
using namespace std;
int main(){
    int N,M;
    cin >> N >> M;

    vector<set<int>> g(N + 1);

    for(int i = 0; i < M; i ++){
        int a,b;
        cin >> a >> b;
        g[a].insert(b);
        g[b].insert(a);
    }

    int max = 0,max_ind = 0;
    for(int i = 1; i <= N; i ++){
        if(max < g[i].size()){
            max = g[i].size();
            max_ind = i;
        }
    }

    cout << max_ind << endl;

    return 0;
}
```

## 9.2 深さ優先探索
### A62 Depth First Search ★3
問題文:https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_am

**深さ優先探索**とは進めるだけ進み、行き詰ったら一歩戻ってそこから別の分岐を進む探索方法である。Depth First Searchと呼ばれDFSと略される.<br>
実装としては再帰関数で実装することが可能


```C++
#include <bits/stdc++.h>
using namespace std;

void check_connect(vector<set<int>> &graphe ,set<int> &detect, int num){

    for(auto itr = graphe[num].begin(); itr != graphe[num].end(); itr++){
        if(detect.find(*itr) != detect.end()) continue;

        detect.insert(*itr);
        check_connect(graphe,detect,*itr);
    }

    return;
}

int main(){
    int N,M;
    cin >> N >> M;

    vector<set<int>> g(N + 1);

    for(int i = 0; i < M; i ++){
        int a,b;
        cin >> a >> b;
        g[a].insert(b);
        g[b].insert(a);
    }

    set<int> connect;
    connect.insert(1);
    check_connect(g,connect,1);

    if(connect.size() == N){
        cout << "The graph is connected." << endl;
    }
    else{
        cout << "The graph is not connected." << endl;
    }


    return 0;
}
```


### B62 Print a Path
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ei

深さ優先探索の目的の頂点までの経路を出力する問題<br>
頂点まで到達したらそれをさかのぼって記録していくような実装を作ればよい<br>
アドバイス:再帰関数で目的地まで辿りついたらtrueを返し、trueを返したモノから順にvectorに格納していけば、終点から始点までの順序を記録することが可能

```C++
#include <bits/stdc++.h>
using namespace std;

bool calc_path(vector<set<int>> &graphe ,vector<bool> &detect, vector<int> &path, int num, int target){
    for(auto itr = graphe[num].begin(); itr != graphe[num].end(); itr++){
        if(detect[*itr]) continue;
        detect[*itr] = true;

        if(*itr == target){
            path.push_back(*itr);
            return true;
        }

        if(calc_path(graphe,detect,path,*itr,target)){;
            path.push_back(*itr);
            return true;
        }
    }

    return false;
}

int main(){
    int N,M;
    cin >> N >> M;

    vector<set<int>> g(N + 1);

    for(int i = 0; i < M; i ++){
        int a,b;
        cin >> a >> b;
        g[a].insert(b);
        g[b].insert(a);
    }

    vector<int> path;
    vector<bool> connect(N+1,false);
    connect[1] = true;
    calc_path(g,connect,path,1,N);
    path.push_back(1);

    for(int i = path.size() - 1; i > 0; i --){
        cout << path[i] << " ";
    }
    cout << path.front() << endl;
    return 0;
}
```

## 9.3 幅優先探索
### A63 Shortest Path 1 ★3
問題文:https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_an

**幅優先探索**は先ほどと違い、スタートに近い順番に探索していくアルゴリズムである。<br>
たとえば頂点1からの最短経路長を求めたい場合、頂点1に0を書き込みその隣の頂点に1,1の頂点の隣に2...というように書き込んでいく

![](images/9_%E5%B9%85%E5%84%AA%E5%85%88%E6%8E%A2%E7%B4%A2.png)

#### 実装方法
幅優先探索は**queue(キュー)**を用いた方法が一般的
1. 頂点1からxまでの最短経路超をdist[i]=?で初期化
2. キューに1を追加して、dist[1]=0にする
3. キューが空になるまで以下の操作を繰り返す
   1. キューの要素posを取得
   2. その要素と隣接する全ての頂点xに対して,dist[x]=dist[pos]+1をして、xをキューに追加
   3. 先頭の要素posをキューから削除

```C++
#include <bits/stdc++.h>
using namespace std;


int main(){
    int N,M;
    cin >> N >> M;

    vector<set<int>> g(N + 1);

    for(int i = 0; i < M; i ++){
        int a,b;
        cin >> a >> b;
        g[a].insert(b);
        g[b].insert(a);
    }

    vector<int> dist(N + 1,-1);
    queue<int> queue;
    dist[1] = 0;
    queue.push(1);

    while(!queue.empty()){

        for(auto p : g[queue.front()]){
            if(dist[p] == -1){
                dist[p] = dist[queue.front()] + 1;
                queue.push(p);
            }
        }

        queue.pop();
    }


    for(int i = 1; i <= N; i ++){
        cout << dist[i] << endl;
    }
    
    return 0;
}
```

## B63 幅優先探索
問題文:https://atcoder.jp/contests/tessoku-book/tasks/abc007_3

幅優先探索を用いて迷路の最短経路を求める問題<br>
1. スタート地点の座標を0として、キューにその座標を入れる
2. キューが空になるまで以下の操作
   1. キューの先頭要素posを取得
   2. posの隣接4近傍を調べて、空白かつ距離が決まっていない場合、距離にpos+1を代入してその座標をキューに追加
   3. キューの先頭要素posを削除

このようにすることでスタート地点の座標からのある地点までの最短手数を全ての地点において求める事ができる

```C++
#include <bits/stdc++.h>
using namespace std;

int neighboor_y[4] = {-1,0,0,1};
int neighboor_x[4] = {0,-1,1,0};


int main(){
    int R,C;
    cin >> R >> C;

    int sy,sx;
    cin >> sy >> sx;

    int gy, gx;
    cin >> gy >> gx;

    vector<string> map(R);
    for(int i = 0; i < R; i ++) cin >> map[i];

    vector<vector<int>> dist(R,vector<int>(C,-1));
    queue<pair<int,int>> q;
    q.push(pair<int,int>(sy,sx));
    dist[sy - 1][sx - 1] = 0;

    while(!q.empty()){

        for(int k = 0; k < 4; k ++){
            int i = neighboor_y[k];
            int j = neighboor_x[k];
            
            if(q.front().first + i <= 0 && R < q.front().first + i) continue;
            if(q.front().second + j <= 0 && C < q.front().second + j) continue;

            if(map[q.front().first + i - 1][q.front().second + j - 1] == '.' 
                && dist[q.front().first + i - 1][q.front().second + j - 1] == -1){
                dist[q.front().first + i - 1][q.front().second + j - 1] = dist[q.front().first - 1][q.front().second - 1] + 1;
                q.push(pair<int,int>(q.front().first + i,q.front().second + j));
            }
        }
        q.pop();
    }

    cout << dist[gy - 1][gx - 1] << endl;

    return 0;
}
```

## 9.4 ダイクストラ法
### A64 Shortest Path 2 ★4
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bl

重み付き無向グラフに対する最短経路問題を解く方法に**ダイクストラ法**というアルゴリズムを用いる<br>

**手順**<br>
1. 未確定頂点の距離をcur[]={0,∞,∞,∞,∞,∞}で初期化
2. 未確定頂点のうち、現状一番小さい値である1をdist[1]に入力して確定する
3. 次に1と隣接する頂点2,4についてそれぞれcurを最小のものに更新(cur[]={0,15,∞,20,∞,∞})
4. 未確定頂点の内、距離が最小であるiをdist[i]=cur[i]として確定
5. 次にiと隣接する頂点についてそれぞれcurを最小のものに更新
6. 以降全ての連結した頂点について、4~5を繰り返す

![](images/9_%E3%83%80%E3%82%A4%E3%82%AF%E3%82%B9%E3%83%88%E3%83%A9%E6%B3%95.png)

このようにして解くことが可能だが、この実装だとcurの中から最小のものを探索する操作が $O(N) $であるため、全ての頂点について行うと計算量が $O(N^2) $となり遅い<br>

そこで、curの中で最小の頂点を高速で求めるために、**優先度付きキュー**を用いた実装が用いられる。<br>

**優先度付きキュー**とは要素一つ一つに優先度が割り当てられており、その優先度に従った順に取り出されるデータ構造であるため、距離を優先度として割り当てて更新していくことでcurを全て探索するよりも高速に処理を行う事が可能になる<br>

![](images/9_%E3%83%80%E3%82%A4%E3%82%AF%E3%82%B9%E3%83%88%E3%83%A9%E6%B3%95_priority_queue_1.png)
![](images/9_%E3%83%80%E3%82%A4%E3%82%AF%E3%82%B9%E3%83%88%E3%83%A9%E6%B3%95_priority_queue_2.png)

**ダイクストラ法の計算量**<br>
各頂点の次数を全て足すと2Mになるので、配列curが更新される回数はどんなに多くとも2Mである。したがって、優先度付きキューの追加も高々2M回しか行われないので、ダイクストラ法の計算量は $O(MlogM) $であると分かる<br>

ただし、ダイクストラ法は**長さが負の辺が存在する時には正しく動作しない**ので、代わりに**Bellman-Ford法**などを使用する必要がある。詳しくはコラム6を参照<br>

```C++
#include <bits/stdc++.h>
using namespace std;
#define INF INT32_MAX

int main(){
    int N,M;
    cin >> N >> M;


    vector<vector<pair<int,int>>> g(N+1);

    for(int i = 0; i < M; i ++){
        int A,B,C;
        cin >> A >> B >> C;
        g[A].push_back(pair<int,int>(B,C));
        g[B].push_back(pair<int,int>(A,C));
    }

    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> Q;

    vector<int> cur(N + 1,INF);
    vector<bool> decide(N + 1,false);
    cur[1] = 0;
    Q.push(pair<int,int>(cur[1],1));

    while(!Q.empty()){
        int pos = Q.top().second;
        Q.pop();

        // curが更新されると、優先度付きキューに同じポジションが重複して入力されている可能性があるので、
        // 確定している頂点についてはcontinue
        if(decide[pos]) continue;

        decide[pos] = true;

        for(int i = 0; i < g[pos].size(); i ++){
            if(decide[g[pos][i].first]) continue;
            int nex = g[pos][i].first;
            int weight = g[pos][i].second;

            if(cur[nex] > cur[pos] + weight){
                cur[nex] = cur[pos] + weight;
                Q.push(pair<int,int>(cur[nex],nex));
            }
        }
    }

    for(int i = 1; i <= N; i ++){
        if(cur[i] == INF) cout << -1 << endl;
        else cout << cur[i] << endl;
    }

    return 0;
}
```
### B64 Print a Path
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ek<br>

最短距離の次は最短経路を求める問題<br>
DPの問題でやったように先に最短距離を求めた後、さかのぼるようにして経路を取得していく。今回の場合全ての頂点で1からの最短距離が分かっているので、<br>
 $現在の頂点への最短距離 =　隣接頂点への最短距離 + その辺の距離 $<br>
の関係が成立するような経路を辿れば最短経路をさかのぼることができる。

```C++
#include <bits/stdc++.h>
using namespace std;
#define INF INT32_MAX

int main(){
    int N,M;
    cin >> N >> M;

    vector<vector<pair<int,int>>> graph(N + 1);

    for(int i = 0; i < M; i ++){
        int A,B,C;
        cin >> A >> B >> C;

        graph[A].push_back(pair<int,int>(B,C));
        graph[B].push_back(pair<int,int>(A,C));
    }

    priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> queue;
    vector<bool> kakutei(N + 1,false);
    vector<int> cur(N + 1,INF);
    cur[1] = 0;
    queue.push(pair<int,int>(cur[1],1));

    while(!queue.empty()){

        int pos = queue.top().second;
        int cost = queue.top().first;
        queue.pop();

        if(kakutei[pos]) continue;
        kakutei[pos] = true;

        for(int i = 0; i < graph[pos].size(); i ++){
            int cur_cost = cost + graph[pos][i].second;
            int next_pos = graph[pos][i].first;

            if(cur_cost < cur[next_pos]){
                cur[next_pos] = cur_cost;
                queue.push(pair<int,int>(cur[next_pos],next_pos));
            }
        }
    }

    bool condi = false;
    int curent_pos = N;
    vector<int> root;
    root.push_back(N);

    while(!condi){
        for(int j = 0; j < graph[curent_pos].size(); j ++){
            int cost = graph[curent_pos][j].second;
            int prev_pos = graph[curent_pos][j].first;

            if(cur[curent_pos] == cur[prev_pos] + cost){
                root.push_back(prev_pos);
                curent_pos = prev_pos;

                if(prev_pos == 1){
                    condi = true;
                }
                break;
            }
        }
    }

    for(int j = root.size() - 1; j > 0; j --){
        cout << root[j] << " ";
    }
    cout << root[0] << endl;
    
    return 0;
}
```

## 9.5 木に対する動的計画法
### A65 Road to Promotion ★4
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bm<br>

直属の上司が社長以外1人つく会社を考えた時に、各社員についてそれぞれ何名の部下がいるのかを出力する問題<br>
この時上司関係は木構造で表すことができるので、地位の低い順に動的計画法で部下の人数を求めて行くことで、DP問題のように解くことが可能

今回の場合、地位が高い順に入力されているので、番号が大きい方から計算していけばよい<br>

![](images/9_treeDP.png)

仮に地位順に入力されていない場合は**幅優先探索**を用いて、一番遠い社員から計算していくことで同じように計算可能(優先度付きキューなどで、距離の長い順に処理していくような実装をすればよさそう)

```C++
#include <bits/stdc++.h>
using namespace std;
#define INF INT32_MAX

int main(){
    int N;
    cin >> N;

    vector<vector<int>> tree(N + 1);

    for(int i = 2; i <= N; i ++){
        int A;
        cin >> A;
        tree[A].push_back(i);
    }

    vector<int> answer(N + 1,0);

    for(int i = N; i >= 1; i --){
        if(tree[i].empty()) {answer[i] = 0; continue;}

        for(int j = 0; j < tree[i].size(); j ++){
            answer[i] += answer[tree[i][j]] + 1;
        }
    }

    for(int i = 1; i < N; i ++){
        cout << answer[i] << " ";
    }
    cout << answer[N] << endl;
    
    return 0;
}
```

### B65 Road to Promotion Hard
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_el

まず番号の制約がないので、深さ優先探索や幅優先探索で一番末端の社員を見つけてから、階層を計算してあげる必要がある。<br>
今回は幅優先探索を使用して、社長からの距離を求め、距離の遠い順に処理を行うように優先度付きキューを用いた。<br>
部下がいない場合を階層0として、自分の部下の階層の最大値を求めていけば先ほどと同様動的計画法のように各社員の階層を求める事が可能

```C++
#include <bits/stdc++.h>
using namespace std;
#define INF INT32_MAX

int main(){
    int N,T;
    cin >> N >> T;

    vector<vector<int>> graph(N + 1);

    for(int i = 1; i < N; i ++){
        int A,B;
        cin >> A >> B;
        graph[A].push_back(B);
        graph[B].push_back(A);
    }

    vector<bool> kakutei(N + 1,false);
    vector<vector<int>> tree(N + 1);
    vector<int> hierarchy(N + 1,0);
    queue<int> Q;
    priority_queue<pair<int,int>,vector<pair<int,int>>,less<pair<int,int>>> pQ;
    Q.push(T);
    pQ.push(pair<int,int>(0,T));

    while(!Q.empty()){
        int num = Q.front();
        Q.pop();
        kakutei[num] = true;
        for(int i = 0; i < graph[num].size(); i ++){
            if(kakutei[graph[num][i]]) continue;

            tree[num].push_back(graph[num][i]);
            hierarchy[graph[num][i]] = hierarchy[num] + 1;
            Q.push(graph[num][i]);
            pQ.push(pair<int,int>(hierarchy[num] + 1, graph[num][i]));
        }
    }

    vector<int> answer(N + 1,0);
    while(!pQ.empty()){
        int pos = pQ.top().second;
        pQ.pop();
        if(tree[pos].empty()) continue;

        int max_hie = 0;

        for(int i = 0; i < tree[pos].size(); i ++){
            max_hie = max(max_hie, answer[tree[pos][i]]);
        }

        answer[pos] = max_hie + 1;
    }

    for(int i = 1; i < N; i ++){
        cout << answer[i] << " ";
    }
    cout << answer[N] << endl;
    
    return 0;
}
```

## 9.6 Union-Find 木
### Connect Query ★3
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bn

**Union-Find**はグループ分けを効率的に管理することができるデータ構造である。具体的には以下の2種類のクエリを高速に処理することが可能
- 統合クエリ：要素uを含むグループと要素vを含むグループを統合する
- 回答クエリ:要素uと要素vが同じグループにあるかを答える

![](images/9_Union-FInd.png)

Union-Findは以下の条件を満たすような**根付き木**の構造で扱われる
- 同一のグループに属する頂点の根は同じ
- 異なるグループに属する頂点の根は異なる

例えば以下の図のように{1,5,7}と{2,3,4,6}に分かれていた場合、Union-Findの構造はの例は以下ようになる
![](images/9_Union-Find_structure.png)

統合クエリの場合、二つのグループのどちらかの根をもう片方の根に繋げば統合ができる<br>
回答クエリの処理はある頂点xの根をroot(x)と表す時、要素uとvが同じ根かどうかを判定することで判断できる<br>
このようにUnion-Findの構造を用いることで二つのグループにの同一グループ判定と統合が簡単にできるようになる

Union-Findのrootの計算自体は以下の実装で可能

```C++
int root(int x){
    while(true){
        if(par[x] == -1) break;
        x = par[x];
    }
    return x;
}
```

しかし、この実装では頂点がN個ある場合に最悪距離がN-1となり $O(N) $の計算量になってしまう。<br>
そこで、Union-Findの計算量を減らすために、**頂点数の多いグループを上に持っていく**という工夫が必要になる。これを行う事で計算量が $O(N) $から $O(logN) $まで削減することが可能。この手法を**Union by Size**と呼ぶ。

![](images/9_Union_by_Size.png)

今回の回答でUnion-Findを実装した際には、直接vectorを用いて実装したが、クラスを用いて実装することをオススメする<br>
(次のB問ではクラスを用いた実装に挑戦しているのでそちらを参照)
```C++
#include <bits/stdc++.h>
using namespace std;
#define INF INT32_MAX

int root(vector<int> &par,int x){
    while(true){
        if (par[x] == -1) break;
        x = par[x];
    }
    return x;
}

void init(vector<int> &par,vector<int> &siz){
    for(int i = 0; i < par.size(); i ++){
        par[i] = -1;
        siz[i] = 1;
    }
    return;
}

void integrate(vector<int> &par, vector<int> &siz,int x1,int x2){
    int root_x1 = root(par,x1);
    int root_x2 = root(par,x2);
    if(root_x1 == root_x2) return;
    if(siz[root_x1] < siz[root_x2]){
        par[root_x1] = root_x2;
        siz[root_x2] = siz[root_x1] + siz[root_x2];
    }
    else{
        par[root_x2] = root_x1;
        siz[root_x1] = siz[root_x1] + siz[root_x2];     
    }
    return ;
}

int main(){
    int N,Q;
    cin >> N >> Q;

    vector<int> parent(N + 1);
    vector<int> siz(N + 1);
    init(parent,siz);

    struct Query{
        int q;
        int u;
        int v;
    };

    vector<struct Query> query(Q);
    for(int i = 0; i < Q; i ++){
        int q,u,v;
        cin >> q >> u >> v;
        query[i].q = q;
        query[i].u = u;
        query[i].v = v;

    }

    for(int i = 0; i < Q; i ++){
        int q,u,v;
        q = query[i].q;
        u = query[i].u;
        v = query[i].v;
        if(q == 1){
            integrate(parent,siz,u,v);
        }
        else{
            int root_u = root(parent,u);
            int root_v = root(parent,v);
            if(root_u == root_v) cout << "Yes" << endl;
            else cout << "No" << endl;
        }
    }
    
    return 0;
}
```

### B66 Typhoon
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_em

N本の駅とM本の路線があり、クエリからは運休の情報の入力か二つの駅が繋がっているのかを問われる問題<br>
二つの駅が繋がっているかについては、Union-Findの得意とするところだが、あくまでUnion-Findができることは、二つのグループの統合処理であるため、運休になった場合にその路線の繋がりを消すような事は難しい(rootを元に統合を行っているため、実際にどことどこの駅が繋がっているかの情報が保存されていないため、どの辺を消せば良いかが分からない)<br>
そのため、普通にやろうするとUnion-Findは使えないため、工夫が必要。
今回の場合最後のクエリが入力された時点の状態を初期状態と考えて、さかのぼる事を考える。このように考えると**運休した辺を消す処理**から**運休していた路線を復旧して繋ぎ直す(統合する)処理**へ解釈することができるため、このようにすればUnion-Findで処理ができる

```C++
#include <bits/stdc++.h>
using namespace std;

class Union_Find{
    vector<int> parent;
    vector<int> size;
    int num;

    public:
    Union_Find(int N){
        num = N;
        parent = vector<int>(N + 1, -1);
        size = vector<int>(N + 1,1);
    }

    void init(){
        for(int i = 0; i <= num; i ++){
            parent[i] = -1;
            size[i] = 1;
        }
    }

    int root(int x){
        while(true){
            if(parent[x] == -1) break;
            x = parent[x];
        }
        return x;
    }

    void integrate(int u,int v){
        int root_u = root(u);
        int root_v = root(v);
        if(root_u == root_v) return;
        if(size[root_u] < size[root_v]){
            parent[root_u] = root_v;
            size[root_v] = size[root_v] + size[root_u];
        }
        else{
            parent[root_v] = root_u;
            size[root_u] = size[root_v] + size[root_u];
        }
        return;
    }

    bool equal(int u,int v){
        return root(u) == root(v); 
    }

};

int main(){
    int N,M;
    cin >> N >> M;

    Union_Find UF(N);

    vector<pair<int,int>> route(M + 1);
    vector<bool> canceled(M + 1,false);
    for(int i = 1; i <= M; i ++){
        int A,B;
        cin >> A >> B;
        route[i] = pair<int,int>(A,B);
    }

    int Q;
    cin >> Q;
    struct Query{
        int q;
        int u;
        int v;
        int x;
    };


    vector<struct Query> query(Q);
    for(int i = 0; i < Q; i ++){
        cin >> query[i].q;
        if(query[i].q == 1){
            cin >> query[i].x;
            canceled[query[i].x] = true;
        }
        else{
            cin >> query[i].u >> query[i].v;
        }
    }

    for(int i = 1; i <= M; i ++){
        if(!canceled[i]) UF.integrate(route[i].first,route[i].second);
    }

    vector<string> answer;

    for(int i = Q - 1; i >= 0; i --){
        int q = query[i].q;

        if(q == 1){
            UF.integrate(route[query[i].x].first, route[query[i].x].second);
            canceled[query[i].x] = false;
        }
        else{
            if(UF.equal(query[i].u,query[i].v)) answer.push_back("Yes");
            else answer.push_back("No");
        }
    }

    for(int i = answer.size() - 1; i >= 0; i --){
        cout << answer[i] << endl;
    }


    return 0;
}
```

## 9.7 最小全域木問題
### A67 MST ★5
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bo

**全域木**とは、M個の辺の中からいくつか選んで作った全ての頂点が繋がっている木のこと。ただし、同じグラフであっても2通りの以上の全域木が考えられる

![](images/9_%E5%85%A8%E5%9F%9F%E6%9C%A8.png)

そこで、全域木の中でも「長さの合計」が最小となるものを**最小全域木**と呼びます。上の図だと右の木が最小全域木に該当する。
最小全域木は頂点を「駅」、辺を「路線の建設コスト」と考えるとイメージしやすい。最小コストですべての駅を繋ぐ方法が求める最小全域木である。

最小全域木は「短い辺から追加していく」単純な貪欲法によって、必ず正しい答えが出せることが知られている。<br>
この方法は**クラスカル法**と呼ばれており、配列のソートとUnion-Findを用いて実装することが可能。アルゴリズムの流れを以下に示す

![](images/9_%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%AB%E3%83%AB1.png)
![](images/9_%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%AB%E3%83%AB2.png)

Union-Findは以前の問題の回答から流用
※sortはラムダ式を使うと三番目のコストの要素でsortすることができる

```C++
#include <bits/stdc++.h>
using namespace std;

class Union_Find{
    vector<int> parent;
    vector<int> size;
    int num;

    public:
    Union_Find(int N){
        num = N;
        parent = vector<int>(N + 1, -1);
        size = vector<int>(N + 1,1);
    }

    void init(){
        for(int i = 0; i <= num; i ++){
            parent[i] = -1;
            size[i] = 1;
        }
    }

    int root(int x){
        while(true){
            if(parent[x] == -1) break;
            x = parent[x];
        }
        return x;
    }

    void integrate(int u,int v){
        int root_u = root(u);
        int root_v = root(v);
        if(root_u == root_v) return;
        if(size[root_u] < size[root_v]){
            parent[root_u] = root_v;
            size[root_v] = size[root_v] + size[root_u];
        }
        else{
            parent[root_v] = root_u;
            size[root_u] = size[root_v] + size[root_u];
        }
        return;
    }

    bool equal(int u,int v){
        return root(u) == root(v); 
    }

};

int main(){
    int N,M;
    cin >> N >> M;

    struct graph{
        int A,B,C;
    };

    vector<struct graph> graphs(M);

    for(int i = 0; i < M; i ++){
        cin >> graphs[i].A >> graphs[i].B >> graphs[i].C;
    }

    sort(graphs.begin(),graphs.end(),
         [](const struct graph &a,const struct graph &b){return a.C < b.C;});
        
    Union_Find UF(N);

    int count = 0;
    for(int i = 0; i < M; i ++){
        if(!UF.equal(graphs[i].A,graphs[i].B)){
            UF.integrate(graphs[i].A,graphs[i].B);
            count += graphs[i].C;
        }
    }

    cout << count << endl;

    return 0;
}
```

### B67 Max MST
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_en

A67では**最小**全域木を求めたが、今度は**最大**全域木の長さを求める問題<br>
A67のコードの中のsortの順序を降順に変えるだけで実装可能

```C++
#include <bits/stdc++.h>
using namespace std;

class Union_Find{
    vector<int> parent;
    vector<int> size;
    int num;

    public:
    Union_Find(int N){
        num = N;
        parent = vector<int>(N + 1, -1);
        size = vector<int>(N + 1,1);
    }

    void init(){
        for(int i = 0; i <= num; i ++){
            parent[i] = -1;
            size[i] = 1;
        }
    }

    int root(int x){
        while(true){
            if(parent[x] == -1) break;
            x = parent[x];
        }
        return x;
    }

    void integrate(int u,int v){
        int root_u = root(u);
        int root_v = root(v);
        if(root_u == root_v) return;
        if(size[root_u] < size[root_v]){
            parent[root_u] = root_v;
            size[root_v] = size[root_v] + size[root_u];
        }
        else{
            parent[root_v] = root_u;
            size[root_u] = size[root_v] + size[root_u];
        }
        return;
    }

    bool equal(int u,int v){
        return root(u) == root(v); 
    }

};

int main(){
    int N,M;
    cin >> N >> M;

    struct graph{
        int A,B,C;
    };

    vector<struct graph> graphs(M);

    for(int i = 0; i < M; i ++){
        cin >> graphs[i].A >> graphs[i].B >> graphs[i].C;
    }

    sort(graphs.begin(),graphs.end(),
         [](const struct graph &a,const struct graph &b){return a.C > b.C;});
        
    Union_Find UF(N);

    int count = 0;
    for(int i = 0; i < M; i ++){
        if(!UF.equal(graphs[i].A,graphs[i].B)){
            UF.integrate(graphs[i].A,graphs[i].B);
            count += graphs[i].C;
        }
    }

    cout << count << endl;

    return 0;
}
```

## 9.8 最大フロー問題
### A68 Maximum Flow ★6
問題文:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bp

**最大フロー問題**とは重み付き有向グラフで表されるパパイプラインにおいて、スタートからゴールまで流せる水の総量を最大化する問題<br>
最大フロー問題は「水の流れ」にとどまらず、実社会の様々な課題に応用することができる。
- 各ネットワークの通信料の上限が与えられた時、2つのコンピュータ間でより多くのデータを通信する方法を求める<br>
- 各交通手段の1日当たりの輸送能力が与えられた時、東京から大阪まで1日最大何人を輸送できるか(ゴールデンウィークなどの大型連休に重要)

最大フロー問題は以下の2つの条件を満たすように、各パイプの流量 $f_{i} $を求める問題として定式化できる

- 条件1:  $0 <= f_{i} <= C_{i} (i = 1,2,...,M) $
- 条件2: スタートとゴールを除く各頂点において、入る水量と出る水量は同じ

各辺に対して「流量/上限値」を書いた以下の図を使って表す<br>
スタートから出る水の量を総流量といい、その値を最大にする流し方を**最大フロー**という。この以下の図の場合、総流量は8である。

![](images/9_maximum_Flow1.png)

```C++
```

# 10章 総合問題

# 終章 さらに上達するには