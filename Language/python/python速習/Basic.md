最終更新:2023/10/31

<!-- omit in toc -->
# python速習
様々な本を読む際にpythonの紹介があるが、内容が重複しているのでこちらに上手いことまとめる<br>
仮想環境の構築などについては割愛　(どこかににまとめようと思う)

<!-- omit in toc -->
# 目次
- [空白によるフォーマット](#空白によるフォーマット)
- [モジュール](#モジュール)
- [関数](#関数)
- [文字列](#文字列)
- [例外](#例外)
- [リスト](#リスト)
- [タプル](#タプル)
- [辞書](#辞書)
  - [defaultdictクラス](#defaultdictクラス)
- [Counterクラス](#counterクラス)
- [集合](#集合)
- [実行順制御](#実行順制御)
- [真偽](#真偽)
- [ソート](#ソート)
- [リスト内包表記](#リスト内包表記)
- [自動テストとアサート](#自動テストとアサート)
- [オブジェクト指向プログラミング](#オブジェクト指向プログラミング)
- [イテレータとジェネレータ](#イテレータとジェネレータ)
- [乱数](#乱数)
- [正規表現](#正規表現)
- [関数型プログラミング](#関数型プログラミング)
- [zipと引数展開](#zipと引数展開)
- [argsとkwargs](#argsとkwargs)
- [型アノテーション](#型アノテーション)
  - [型アノテーションの書き方](#型アノテーションの書き方)
- [あとがき](#あとがき)

[Top]: #目次

# 空白によるフォーマット
多くの言語は波かっこ{}でコードブロックを作成するが、pythonではインデントで管
理する.以下のコードのようにfor文はインデントごとにスコープが生成される
```python
print("i loop start")
for i in range(5):
    print("j loop start")
    for j in range(5):
        print(i + j)
    print("j loop end")
print("i loop end")    
```

基本的に一行につき一つの文で管理されるが、()や[]内のでは折り返しが許される。また、\を付ければ折り返すことも可能
```python
# ok
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

value = (1 + 2 + 3 +
         4 + 5 + 6)

value = 1 + 2　\
        + 3
```

[Topに戻る][Top]

# モジュール
pythonはデフォルトでは大した機能はないので、importで別のモジュールから機能をロードする必要がある
```python
# 基本的なimport
import cv2
img = cv2.imread(str)

# モジュール名が長ったらしい場合にはasで省略可能
import matplotlib.pyplot as plt
plt.show()

# モジュールから一部の関数やクラスだけ持ってくる場合
from cv2 import imread
# from cv2 import * # ワイルドカードも可能
img = imread(str)
```
fromで不用意に全部持ってくると自分で作成した変数名と被ってしまうこともあるので、必要な機能だけを持ってくるのが望ましい

[Topに戻る][Top]

# 関数
関数はdefで定義することができる

```python
# 基本的な形
def sum(x,y):
    return x + y

# 関数を引数に代入することも可能
def run(func)
    return func(1,2)
func = sum
a = run(func) # 1 + 2

# デフォルト値を設定することで省略可能
def print_name(name:str="my name"):
    ptint(name)
print_name() # デフォルト値のmy nameが表示
print_name("your name") # 当然普通に設定可能

# 引数名を指定して入力することもできる(便利)
def full_name(first:str="nothing",last:str="something")
    print(first + " " + last)
print(last="last") # nothing lastが表示 (lastの引数だけ変更して表示される)
```

[Topに戻る][Top]

# 文字列
文字列はシングルクォーテーション(')かダブルクォーテーション(")で囲む事で定義
```python
# 定義
single = 's data'
double = "d data"

# 特殊文字はバックスラッシュ
tab = "\t" # これはtab記号の一文字
not_tab = r"\t" # 正規表現などでバックスラッシュを一文字として扱いたいときはrを付ける

# fを付けることで文字列を代入することが可能 (全部結果は同じ)
format = f"{single} {double}" # f文字を使った代入
format = single + " " + double # 単純な連結
format = "{} {}".format(single,double) # formatを使った代入
```

[Topに戻る][Top]

# 例外
実行時にエラーが起こり、例外が出た時に通常処理が中断されるが、tryとexceptで処理を継続することが可能

```python
try:
    print(0/0) #ゼロ割
except ZeroDivisionError:
    print("cannot divide by zero")
```

[Topに戻る][Top]

# リスト
pythonで最も基本的なデータ構造で、単純な順序ありコレクション

```python
# 宣言
int_list = [1,2,3]
val_list = ["str",0.1,True] # 型が異なるものも入れられる
list_list = [int_list,val_list,[]] # リストの中にリストを入れる事も可能

# リストの情報を出す関数例
length = len(int_list) # リストの長さ
sums = sum(int_list) # 数値リストのみ合計

x = [[1,2,3,4,5],
     [5,4,3,2,1]
     [0,9,8,7,6]
     [6,7,8,9,0]
     [0,0,0,0,0]]

#　要素の取り出し
print(x[1,0]) # 4
print(x[0,1]) # 2
print(x[:,0]) # [1,5,0,6,0] ※1列目を全て表示することも可能
print(x[:2,:]) # 0~1行目の内容
print(x[1:,:]) # 1~行目の内容を表示
print(x[0,::2]) # [1,3,5]  ※0行目のリストを、0列目を起点に2つ飛ばしで全て表示する
print(x[0,-3]) # 3 ※最後から3つ目の要素を参照
print(x[0,1:-1]) # [2,3,4] ※最初と最後以外の要素を表示

# 含まれるかの判定
1 in x[0,:] # True
0 in x[1,:] # False

# listの同士の連結
a = [1,2,3]
a.extend([4,5,6]) # a = [1,2,3,4,5,6]
b = a + [4,5,6] # aを変更したくなければこのような形でも可能

# 要素の追加
a = [1,2,3]
a.append(0) # [1,2,3,0]

#　リストの展開
a = [1,2,3]
b,c = a[:2] #b=1 c=2
```

[Topに戻る][Top]

# タプル
リストに似ているが要素を変更できないという制限がある。
```python
# 基本的なタプルの宣言
a = (1,2)
b = [1,2]

# 要素の変更
a[0] = 1 # TypeError
b[0] = 1 # リストは可能

# 関数から複数の値を返す時はタプルになる
def func(x,y):
    return x + y, x * y

a = func(1,2) # a =(3,2)
a,b = func(1,2) # a = 3 b = 2として受け取ることも可能

# 値の交換
x,y = (1,2)
x,y = (y,x) # x=2 y=1というように使える
```

[Topに戻る][Top]

# 辞書
辞書も基本的なデータ構造の一つであり、**キー**と**値**を関連付けて格納する
```python
# 宣言・初期化
empty_dict = {}
empty_dict = dict()
grade = {"Joel":80,"Tim":95}

# 呼び出し
joel_value = grade["Joel"] # 80
tim_value = grade.get("Tim") # getを使っても呼び出せる
kate_value =  grade.get("Kate") # 登録されていない人がいる場合、getはNoneを返す([]で参照するとKeyError)

# キーの探索
"Joel" in grade # True
"som" in grade # False

# 値の代入
grade["Joel"] = 90 # キーがある場合は値が上書き
grade["Kate"] = 70 # キーがない場合は新規に追加される
len(grade) # 3
```

## defaultdictクラス
単語の出現回数を数えるタスクを想定した時に基本的には初期値0として1を加算していく処理になるが、未知の単語が出た際には初期値がないので、以下のいづれかの手順で登録してあげる必要がある
```python
word_counts = {...}
docment = ["etc",...]

for word in docment:

    # if文で分岐
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

    # try,exceptで検出
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

    # getを使う
    prev_count = word_counts.get(word,0) # ない場合は0を登録
    word_counts[word] = prev_count + 1
```

ただし、どれもスマートとはいえない。そこで**defaultdictクラス**を使う事で綺麗に書くことが可能<br>defaultdictクラスは最初にキーがない場合の際の初期値を決めることができる辞書型となっているため、今回の場合0を設定しておく事で余分な分岐を減らす事ができる
```python
from collections import defaultdict #importが必要
word_counts = defaultdict(int) # int()は0を返す
docment = ["etc",...]

for word in docment:
    word_counts[word] += 1 # 未知の単語が来ても自動的に0を設定して同様にカウントできる
```

初期値にはリストや辞書なども設定可能
```python
from collections import defaultdict #importが必要

dd_list = defaultdict(list) # list()=[]
dd_list[2].append(1) # dd_listには{2,[1]}が登録される

dd_dict = defaultdict(dict) # dict()={}
dd_dict["Joel"]["City"] = "seattle" # dd_dictには{"Joel":{"City":"seattle}}が登録される

dd_pair = defaultdict(lambda:[0,0])　#関数なども設定できる (lamdbaは無名関数の設定方法。この場合[0,0]のリストを返す関数)
dd_pair[2][1] = 1 # dd_pairには{2:[0,1]}が登録される
```

[Topに戻る][Top]

# Counterクラス
一続きの値をdefaultdictと同様のキーと出現数に展開するクラス
```python
from collections import Counter
c = Counter([0,1,2,0]) # c={0:2,1:1,2:1}となる
```
先ほどのdefaultdictの問題はこれ一つで解決可能
```python
word_counts = Counter(docment)
# 出現回数の多い順に要素を返すmost_commonメソッドが用意されている
for word,count in word_counts.most_common(10): #Top10を表示
    print(word:count) #　キーとその出現回数を表示
```

[Topに戻る][Top]


# 集合
集合は値を重複せずに格納するコレクション
```python
# 宣言・初期化
s = {1,2,4,5,1} # {}で囲む
s = set() # 要素を0にする場合

# 要素の追加
s.add(1) # 1を追加
s.add(2) # 2を追加
s.add(2) # この2は追加されない
len(s) # 2

# 要素の判定
2 in s # True
3 in s # False
```
setを使う利点はin演算子が非常に高速で動作する点と重複の無い集まりを得る事ができる点である。高速化などを考えた時には活用してみると良い
[Topに戻る][Top]

# 実行順制御
if文やfor文などの基本的な制御方法について記述
```python
#if文
if l > 2:
    print("l > 2")
elif l > 3: #else if の略
    print("l > 3")
else:
    print("l < 2")

# if-then-elseを一行にまとめる事も可能
parity = "even" if x % 2 == 0 else "odd"

#while文
x = 0
while x < 10:
    print(f"{x}")
    x += 1

#for文
for x in range(10):
    print(f"{x}")

# continueやbreakなども可能
for x in range(10): # 0,1,2,4が表示されて終る
    if x == 3:
        continue # 残りの行を飛ばして最初に戻る
    elif x == 5:
        break #ループを抜ける
    else:
        print(x)
```
[Topに戻る][Top]

# 真偽
pythonのboolはTrueとFalseで管理される。また値が指定されていない変数はNoneとして扱われる
```python
# ex
a = 1 < 2 # True
b = True == False # False

x = None
assert x is None # xがNoneかどうかを判定できる(== Noneでもok)

# これは真偽判定の際は全てFalse扱いされる
# [False, None, [], {}, "", set(), 0, 0.0] 
# 何か0以外の値が設定されていれば全てTrue

# 以下のような書き方が可能(sがTrueならs[0]を代入 sがFalseなら""を代入)
# first_char = s[0] if not s else ""　と同じ 
first_char = s and s[0]

```
[Topに戻る][Top]

# ソート
リストにはsortを行う関数が用意されている。デフォルトでは昇順にソートが行われる
```python
x = [4,1,-2,-3]
y = sorted(x) # yにソート結果を代入 xはそのまま
x.sort() # x自体をsort

# 降順に並べたいときは、reverse=Trueにする
x.sort(reverse = True) # [4,1,-2,-3]

# 関数を適用した結果でsortしたい場合はkeyを指定する
x.sort(key = abs) # [1,-2,-3,4]
```
[Topに戻る][Top]

# リスト内包表記
リストから一部の要素を取り出したり、値を変更しながら別のリストを再構成する必要がある時に便利
```python
# 例
even_numbers = [x for x in range(5) if x % 2 == 0] # [0,2,4]
squares = [x * x for x in range(5)] # [0,1,4,9,16]
even_sq = [x * x for x in even_numbers] #[0,4,16]

# 辞書や集合にも使える
sq_dict = {x : x * x for x in range(5)} # {0:0,1:1,2:4...}
sq_set = {x * x for x in [1,-1]} #{1}

# リストの値が必要ない場合はアンダースコアを置く
zeros = [0 for _ in range(5)]

#　複数のfor文を併用することも可能
pairs = [(x,y) for x in range(10) for y in range(10)]
# 以下の文と同義
# pairs = []
# for x in range(10):
#     for y in range(10):
#         pairs.append((x,y))
```
[Topに戻る][Top]

# 自動テストとアサート
コードの不具合をテストするために、assertを使って自動的にテストを行う事が良くある。こうした確認を随時行う事でコードの正しさをチェックできる
```python
def smallest_value(xs)
    return min(xs)

assert smallest_value([10,20,5,40]) == 5 # 5以外の値が帰ってくる場合は関数が間違っているのが分かる
```
[Topに戻る][Top]

# オブジェクト指向プログラミング
pythonでもクラスの概念があり、データと操作関数をカプセル化することができる
```python
# 基本的な例
class Counter:

    # メンバー変数
    x = None

    # コンストラクタ
    # __init__はコンストラクタ用のメソッド名
    # ちなみにpythonでは__~__という関数名はdunderメソッドといい、特殊な動作を表す
    def __init__(self,init = 0):
        self.x = init
    
    # __repr__はprintした時に呼び出される文字列メソッド
    def __repr__(self):
        return f"Counter(x={self.x})"

    def add(self):
        self.x += 1

counter = Counter()
print(counter)
counter.add()
print(counter)

# クラスは親クラスから継承する事も可能
class BackCounter(Counter):

    # コンストラクタをオーバーライド
    def __init__(self,init = 0):
        # superはCounterクラスの初期化処理を明示的に呼び出し
        super().__init__(init)
    
    def __repr__(self):
        return f"BackCounter(x={self.x})"
    
    # 新しいメソッドを追加
    def back(self):
        self.x -= 1

bcounter = BackCounter()
print(bcounter)　# BackCounter(x=0)
bcounter.back()
print(bcounter)  # BackCounter(x=-1)
```
[Topに戻る][Top]

# イテレータとジェネレータ
リストによって特定のインデックスの要素を取得できるのは良いが、これが大量の要素数になるとメモリの消費量が多くなってしまう。
一度に一つの要素が必要であれば、全てをメモリに保存する必要はないため、実行時にのみ遅延的に要素を生成する**ジェネレーター**を用いることでメモリの問題を解決可能
```python
# 基本例
def generate_range(n):
    i = 0
    while i < n:
        yield i # yield:iを返した後一時中断して、二回目以降に呼び出される時はここから始まる
        i += 1

for i in generate_range(10):
    print(i)

# ()とfor内包表記でジェネレータをそのまま生成することも可能
# [0,2,4,6,...,18]
evens_below_20 = (i for i in range(20) if i % 2 == 0)
for i in evens_below_20:
    print(i)

# ジェネレータはforかnextで呼び出されるまで値が生成されない(遅延実行)
data = (i for i in range(20)) # この段階では何も生成されていない
print(next(data)) # 0が生成
for i in data:
    print(i) # 1~19が生成

# 要素とインデックスの両方が必要な時はenumerate関数が有効
# 1:1 2:3 3:5 ...
odds = (i for i in range(20) if i % 2 != 0)
for i,num in enumerate(odds):
    print(i,num)

```
[Topに戻る][Top]

# 乱数
**random**モジュールを用いて乱数の生成が可能
```python
# 基本的な使い方
import random
random.seed(10) # 乱数のシード点を固定

# random():0~1までの一様乱数の生成
randoms = [random.random() for _ in range(4)]
print(randoms)
# [0.5714025946899135, 0.4288890546751146, 0.5780913011344704, 0.20609823213950174]

# randrange():指定した範囲の整数を取り出す
rangerandoms = [random.randrange(1,10) for _ in range(10)]
print(rangerandoms)
# [1, 7, 8, 1, 4, 8, 8, 5, 3, 1]

# shuffle():リストの中身をシャッフルする
samples = [i for i in range(10)]
print(samples)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(samples)
print(samples)
# [5, 2, 7, 1, 8, 4, 3, 6, 0, 9]

# choice():リストから一つの要素をランダムに取り出す
print(random.choice(samples))
# 9

# sample():リストからいくつかの値を重複なしで取り出す
print(random.sample(samples))
# [0, 6, 7, 4, 9, 1]
# 重複ありなら、複数回choice()実行すれば良い
```
[Topに戻る][Top]

# 正規表現
正規表現を用いる事で、テキスト検索を効率的に行う事が可能
実際使いこなすにはかなり複雑なため、ここでは一例を紹介するにとどめる
```python
import re

# 以下全てTrue
re_exsample = [
    not re.match("a","cat"), # aとcatの完全一致を判定
    re.search("a","cat"), # catからaを探索
    not re.search("c","dog"), # dogからcを探索
    3 == len(re.split("[ab]","carbs")), # carbsをaかbで分割すると、要素はc,r,sの3つ
    "R-D-" == re.sub("[0-9]","-","R2D2") # R2D2から0~9までの数字を-に置換
]

```
[Topに戻る][Top]

# 関数型プログラミング
説明は一旦割愛

※理由
(partial,map,reduce,filterなどの関数があるが、これはpython的ではなく避けるべきであるため、その他のリスト内包表記やforループ、その他のpython的機能に置き換える事を推奨する)
[Topに戻る][Top]

# zipと引数展開
複数のリストを同時に処理したい時に**zip**が便利。更に**引数展開**と組み合わせて使う事で別の要素ごとに後から分離することも可能
```python
# 基本的な使い方
list1 = ["a","b","c"]
list2 = [1,2,3]
pair = [ pair for pair in zip(list1,list2)] # [("a",1),("b",2),("c",3)]となる

# リストの長さが違う場合は一番短いリストに合わせられる
list1 = ["a","b","c","d","e"]
list2 = [1,2,3]
pair = [ pair for pair in zip(list1,list2)] # [("a",1),("b",2),("c",3)]で同じ

# *を付ける事で引数展開ができ、個々のペアがそれぞれzip関数の引数として渡されることでunzipも可能
char,num = zip(*pair) # zip(("a",1),("b",2),("c",3))と等価
print(char,num)
#('a', 'b', 'c') (1, 2, 3)

# 引数展開はあらゆる関数に適用可能
def add(a,b):
    return a + b

add(1,2) #ok
add([1,2]) #ng 引数が1つしかない判定
add(*[1,2]) #ok 1,2の形で入力される

```
[Topに戻る][Top]

# argsとkwargs
任意個数の引数をとれる関数を生成したい時に使う

```python
# 例:
def doubler(f): # 関数fを引数にして、関数fをxに適用した値を2倍する関数gを返す関数
    def g(x):
        return f(x) * 2
    return g

# 成功例
def func1(x):
    return x + 1 

g = doubler(func1)
print(g(1)) # (1 + 1) * 2 = 4

# 失敗例
def func2(x,y):
    return x + y

g = doubler(func2)
#print(g(1,2)) # gは引数を1つしか取れないのでダメ

# 改善案:argsとkwargsを使用する
# *は引数展開
def magic(*args,**kwargs):
    print("名前無し引数",args)
    print("名前あり引数",kwargs)

magic(1,2,key="word",key2="word2")
# 名前無し引数 (1, 2)
# 名前あり引数 {'key': 'word', 'key2': 'word2'}

def doubler(f):
    #どの様な引数をgに与えてもfを実行することが可能。
    #渡された引数がfの引数と一致していれば自動的に実行される
    def g(*args,**kwargs): 
        return f(*args,**kwargs) * 2
    return g

g = doubler(func2)
print(g(1,2))
```
あらゆる関数をこれで書くことが可能だが、基本的に関数の引数は種類が明確になっている方が読みやすいので、こういった他の手段がない場合にのみ使う事を推奨
[Topに戻る][Top]

# 型アノテーション
pythonは動的型付け言語であるため、明示的に型を指定する必要はない。
が、型アノテーションを行う事で以下の利点がある。
1. 型付けしている事で、その引数が何を示しているのかの情報がすぐに得られる
2. コード実行前に型エラーを知らせる外部ツール(mypy等)を使う事で実行前に間違いを見つける事ができる
3. 型を考慮することでよりクリーンな関数とインターフェースの設計をもたらす
4. 型を使用するとエディタの自動補完機能などの処理を支援したり、型エラーの警告を表示できる

```python
# 利点1:後者の方が関数の使い方についての情報が多く分かりやすい
def dot_product(x,y) :
    return dot(x,y)

def dot_product(x:Vector, y:Vector) -> float:
    return dot(x,y)

# 利点2は省略

# 利点3:operation関数は4種の型を入力可能だが、前者の書き方だと分かりにくく、高確率で誤った使い方をされる。
from typing import Union
def secretly_ugly_function(value,operation):
    pass

def ugly_function(value: int,
                  operation: Union[str,int,float,bool]) -> int:
    pass

# 利点4:VScodeの推定
from typing import List
def f(xs:List[int]):
    xs.append(1) 
    #この時型アノテーションがついていると、VSCodeがappendやclearなどのリストのメソッドを補完してくれる
```
## 型アノテーションの書き方
intやfloatなどはそのまま書くことができるが、Listなどは**typing**モジュールが必要
```python
from typing import List

# これだとfloat出ないリストも入力できてしまう
def sum(xs:list) -> float:
    pass

def sum(xs:List[float]) -> float:
    pass

# typingはList以外にも色々使える
from typing import Dict,Iterable,Tuple
counts: Dict[str:int] = {"data":1}
evens: Iterable[int] = (i for i in range(10) if i % 2 == 0)
triple:Tuple[int,float,int] = (1,4.2,3) #要素ごとに型を指定

# インラインの型ヒントの提供にも有用
from typing import Operation
values:List[int] = []
best_so_far:Operation[float] = None #Noneかfloatのみを許容する



```
[Topに戻る][Top]

# あとがき
より詳しくpythonを知りたければ、以下のサイトを参照
- [公式チュートリアル](https://docs.python.org/ja/3/tutorial/)
- [Ipythonの入門](https://ipython.readthedocs.io/en/stable/interactive/index.html)
- [mypyのドキュメント](https://mypy.readthedocs.io/en/stable/)

[Topに戻る][Top]
