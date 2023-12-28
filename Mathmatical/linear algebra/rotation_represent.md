<!-- omit in toc -->
# 回転行列の表現方法

<!-- omit in toc -->
# 目次
- [回転行列表現とは](#回転行列表現とは)
  - [回転行列から回転角への戻し方](#回転行列から回転角への戻し方)
- [回転行列の代替表現](#回転行列の代替表現)
  - [オイラー角](#オイラー角)
    - [ジンバルロック問題](#ジンバルロック問題)
  - [四元数(quaternion)](#四元数quaternion)
    - [四元数に関連する定義](#四元数に関連する定義)
    - [四元数の性質](#四元数の性質)
    - [回転行列表現](#回転行列表現)
    - [回転の合成](#回転の合成)
  - [オイラー角表現と四元数の変換](#オイラー角表現と四元数の変換)
- [まとめ](#まとめ)


# 回転行列表現とは
2次元や3次元空間において物体の向きや姿勢を表現するために使用される行列であり、2Dの場合は2×2の行列、3×3の行列で表現される

$$
R = \begin{pmatrix}
r_{11} & r_{12} & r_{13} \\ 
r_{21} & r_{22} & r_{23} \\ 
r_{31} & r_{32} & r_{33} \\ 
\end{pmatrix}
$$

良くある回転行列としては以下のような回転行列が思い浮かぶだろう

例えば各軸周りに $\theta$ 度回転させる行列は以下の通りである

$$
R_x = \begin{pmatrix}
1 & 0 & 0 \\ 
0 & \cos\theta & -\sin\theta \\ 
0 & \sin\theta & \cos\theta \\ 
\end{pmatrix}
$$


$$
R_y = \begin{pmatrix}
\cos\theta  & 0 & \sin\theta \\ 
0 & 1  & 0  \\ 
-\sin\theta & 0 & \cos\theta \\ 
\end{pmatrix}
$$


$$
R_z = \begin{pmatrix}
\cos\theta  & -\sin\theta  & 0 \\ 
\sin\theta & \cos\theta & 0 \\ 
0 & 0 & 1\\ 
\end{pmatrix}
$$

更に言えば、任意の回転角を表現する回転行列 $R_{zyx}$ は以下のように表す事ができる

$$
R_{zyx} = R_zR_yR_x = \begin{pmatrix}
\cos\theta_{z}\cos\theta_{y}  & \cos\theta_{z}\sin\theta_{y}\sin\theta_{x} - \sin\theta_{z}\cos\theta_{x}  & \cos\theta_{z}\sin\theta_{y}\cos\theta_{x} + \sin\theta_{z}\sin\theta_{x} \\
\sin\theta_{z}\cos\theta_{y}  & \sin\theta_{z}\sin\theta_{y}\sin\theta_{x} + \cos\theta_{z}\cos\theta_{x}  & \sin\theta_{z}\sin\theta_{y}\cos\theta_{x} - \cos\theta_{z}\sin\theta_{x} \\
-\sin\theta_{y} & \cos\theta_{y}\sin\theta_{x} & \cos\theta_{y}\cos\theta_{x} \\ 
\end{pmatrix}
\cdots(1)
$$

※ 結果は同じだが回転行列をかける順番を変えると式が異なる。そのためこの形式だと回転行列の書き方が6種類存在する

## 回転行列から回転角への戻し方
(1)の回転行列から回転角を抽出したい時は以下の手順を取る
- $r_{20}$ の要素は $-\sin\theta_{y}$ なので $\theta_{y}$ が求まる
- $r_{21}$ の式に $\theta_{y}$


# 回転行列の代替表現
## オイラー角


### ジンバルロック問題

## 四元数(quaternion)
複素数を用いて3次元回転行列を表現する方法を **四元数(quaternion)** というものがある<br>
具体的には以下の形で表される数を四元数という

$$
q = a + bi + cj + dk \\
$$

ただし、以下の条件を満たす
$$
i^2 = j^2 = k^2 = -1, \\
ij = k,jk = i, ki = j\\
ji = -k,kj=-i,ik=-j
$$

四元数を使う事のメリットは以下の点で優れている
- 数学的に美しい
- 3次元空間の中での回転を簡単に記述できる

### 四元数に関連する定義
- ノルム: $||q|| = \sqrt{a^2 + b^2 + c^2 + d^2}$
- 共役な四元数： $\overline{q} = a - bi - cj - dk$
- 逆数: $q^{-1}q = qq^{-1} = 1 となる q^{-1}$
  - 具体的には $q^{-1} = \frac{\overline{q}}{||q||^{2}}$

### 四元数の性質
- 積に関しては交換法則が成立しない
  - 四元数の条件から分かる
- ただし、結合法則は成立する
  - $q_1(q_2q_3) = (q_1q_2)q_3$ が成立する
- 積の共役は共役の積
  - $\overline{q_1q_2} = \overline{q_2}\space\overline{q_1}$ が成立する
  - (ドモルガンみてぇ)

※証明は後で勉強します

### 回転行列表現
回転軸と回転角度を決める事で回転を制御することができる

例えば、
回転軸の方向ベクトル: $\vec{u} = (u_x,u_y,u_z)$
回転角: $\theta$ <br>
がある時、この時の回転に対応する四元数は以下のように定める

$$
q = \cos(\frac{\theta}{2})+(u_xi + u_yj + u_zk)\sin(\frac{\theta}{2})
$$

この時以下の定理が成り立つ

> ベクトル $\vec{a} = (a_x,a_y,a_z)$ と四元数 $a_xi + a_yj + a_zk$ を同一視する。この時、ベクトル $\vec{a}$ を、 $q$ が定める回転によって回転させると $b = q\vec{a}\overline{q}$ が成り立つ

例題)
> 点A:(3,0,0)を $y=x z=0$ で表される軸周りに $180\degree$ 回転させた時の点Bの位置を求めよ

点Aをベクトル表記して四元数で表すと $3i$<br>
回転軸の方向ベクトルは $(\frac{1}{\sqrt{2}},\frac{1}{\sqrt{2}},0)$ なので対応する四元数は

$$
q = \cos(90\degree)+(\frac{1}{\sqrt{2}}i + \frac{1}{\sqrt{2}}j)\sin(90\degree) = \frac{1}{\sqrt{2}}(i+j)
$$

このことから移動後の点Bの四元数は

$$
b = \frac{1}{\sqrt{2}}(i+j) 3i \frac{1}{\sqrt{2}}(-i-j) = \frac{1}{\sqrt{2}}(i+j)(\frac{3}{\sqrt{2}} - \frac{3}{\sqrt{2}}k) = \frac{1}{\sqrt{2}}(\frac{3}{\sqrt{2}}i + \frac{3}{\sqrt{2}}j + \frac{3}{\sqrt{2}}j - \frac{3}{\sqrt{2}}i) = 3j 
$$

したがって、**点B:(0,3,0)**

### 回転の合成
四元数の回転の式に更に回転 $p$ を適用して点cまで回転させる事を考えた時、式は以下のようになる

$$
c = p(q\vec{a}\overline{q})\overline{p}
$$

この時、共役の積の性質と結合法則を使うと以下のように表すことができ、 $qp$ の四元数で表される回転を一回作用させたものとして計算することができる

$$
c = qp\vec{a}\overline{pq}
$$

## オイラー角表現と四元数の変換



# まとめ