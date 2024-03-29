開始日 2023/08/01  
読了日 2023/ * / *  
著者 斎藤康毅 2016年9月28日初版

# 目次
- [1章 Python入門]()
- [2章 パーセプトロン]()
- [3章 ニューラルネットワーク]()
- [4章 ニューラルネットワークの学習]()
- [5章 誤差逆伝搬法]()
- [6章 学習に関するテクニック]()
- [7章 畳み込みニューラルネットワーク]()
- [8章 ディープラーニング]()
- [付録A SOftmax-with-Loss レイヤの計算グラフ]()


# 1章 Python入門
## 1.1 Pythonとは
シンプルで読みやすく覚えやすいプログラミング言語。無料で使用でき、手間のかかるコンパイルが必要ないため、気軽に利用できる。また可読性の高いコードを書くこともできると同時にパフォーマンスの高いコードを書くことも可能。
Numpyやscipyなどの数値計算や統計処理に特化したライブラリが用意されているため、コンピュータサイエンスの分野では一番多く使われている。ディープラーニングの分野においてもtensorflowやpytorchといった有名なフレームワークがありディープラーニングを行う上で最適である。

## 1.2 pythonのインストール
ここはよくある情報なので割愛

## 1.3 Pythonインタプリタ
pythonの基本的な内容なので割愛

## 1.4~1.6 pythonスクリプトファイル
pythonの基本的な内容なので割愛

# 2章 パーセプトロン
## 2.1 パーセプトロンとは
複数の信号を入力として受け取り、重みを付けて線形結合して一つの信号を出力する<br>
出力としては、バイアスというものを閾値として、0か1かを返すようなものになっている。<br>
例えば、入力として二つの入力x1x2がある時、yは以下のように定義される

$y = \begin{cases} 0 &\text{if } x_1w_1 + x_2w_2 \leqq θ \\ 1 &\text{if } x_1w_1 + x_2w_2 > θ \end{cases}$

![](https://cdn.apar.jp/wp-content/uploads/2019/05/ogp-perceptron.png)

$θ$はバイアスで$w_1,w_2$は重みを示しており、それぞれの入力に対して固有の重みをかけることにより、入力に対する出力をコントロールする。重みが大きいほど、その入力が重要であることが分かる<br>

## 2.2 単純な論理回路
### 2.2.1 ANDゲート
パーセプトロンを使った簡単な問題を考えてみる。
ここでは論理回路を題材として、最初にANDゲートについて考えてみる

ANDゲートは真理値表は以下の通りである
|$x_1$|$x_2$|$y$|
|---|---|---|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|

このANDゲートをパーセプトロンで表現する。ここで行う作業はこの真理値表を満たすように$w_1,w_2,θ$の値を適切に決める事である。<br>
$(w_1,w_2,θ) = (0.5,0.5,0.7)$の時は真理値表通りに機能する。<br>
他にも$(1.0,1.0,1.0)$の時なども同様に動作する

### 2.2.2 NANDゲートとORゲート
続いてNANDゲートとORゲートについても考えてみる<br>
NANDゲートの真理値表は以下の通り
|$x_1$|$x_2$|$y$|
|---|---|---|
|0|0|1|
|0|1|1|
|1|0|1|
|1|1|0|

この場合、$(w_1,w_2,θ) = (-0.5,-0.5,-0.7)$の時に条件を満たしている<br>
ANDゲートのパラメータの符号を全て反転すれば、NANDゲートを実現できる<br>

続いてORゲートについても考えてみる。真理値表は以下の通りである。
|$x_1$|$x_2$|$y$|
|---|---|---|
|0|0|0|
|0|1|1|
|1|0|1|
|1|1|1|

この場合、$(w_1,w_2,θ) = (0.5,0.5,0.2)$の時に条件を満たす<br>
この通りパーセプトロンを使えばAND、NAND、ORゲートという論理回路表を表現できることが分かる。ここで重要なのが全て同じ構造であるという事で、重みとバイアスのパラメータを調整するだけで様々ANDやNANDやORを同じ構造で表現することができるのである<br>

## 2.3　パーセプトロンの実装
### 2.3.1 簡単な実装
pythonでの各ゲートの実装は以下の通りになる。
```python
def AND(x1,x2):
    w1,w2,theta=0.5,0.5,0.7
    return x1 * w1 + w2 * x2 > theta

def NAND(x1,x2):
    w1,w2,theta=-0.5,-0.5,-0.7
    return x1 * w1 + w2 * x2 > theta

def OR(x1,x2):
    w1,w2,theta=0.5,0.5,0.2
    return x1 * w1 + w2 * x2 > theta
```
### 2.3.2 重みとバイアスの導入
先のゲートの実装は素直で分かりやすいが、これ以降の事を考えて別の実装方式へと修正する。これに伴い、閾値$θ$を**バイアス**$b$という表現に修正し、以下の式で表現する

$y = \begin{cases} 0 &\text{if } x_1w_1 + x_2w_2 + b \leqq 0 \\ 1 &\text{if } x_1w_1 + x_2w_2 + b > 0 \end{cases}$

バイアス$b$はようは閾値を左項に移動したもので、閾値の符号が反転しているものである。

これを元に先ほどの実装を修正すると、以下のようになる
```python

```