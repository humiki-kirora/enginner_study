# Shell Scriptとは
シェルによる操作をまとめた手順書  
基本的に**コマンドをまとめて実行するためのスクリプト**と考えてよい

- 基本構成
- 変数
- if文
- for文
- よく使う例

# 基本構文
基本的には各シェルのコマンドを書くだけなので、CLI操作ができれば問題ない

## 基本構成
```
<コマンド1> <パラメータ>
<コマンド2> <パラメータ>
...
```

### 例
```shellscript
cd ~
mkdir test_dir
cd test_dir
git clone URL等
```

## 変数
変数には`$`をつけてアクセスする
```shellscript
NUM=5
STRING="hello world"
echo $NUM
echo $STRING
```

### 結果
```shellscript
5
hello world
```

## if文
```

```
