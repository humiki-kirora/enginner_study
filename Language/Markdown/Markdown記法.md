# Markdown記法
見出しの装飾や強調等の文字修飾を簡単にできる記法  
会議の議事録やメモ作成を効率化できるので覚えておくと便利

# 文法チートシート
- [見出し](https://github.com/humiki-kirora/enginner_study/blob/main/Language/Markdown/Markdown%E8%A8%98%E6%B3%95.md#%E8%A6%8B%E5%87%BA%E3%81%97)
- [箇条書き](https://github.com/humiki-kirora/enginner_study/blob/main/Language/Markdown/Markdown%E8%A8%98%E6%B3%95.md#%E7%AE%87%E6%9D%A1%E6%9B%B8%E3%81%8D-)
- [番号付きリスト](https://github.com/humiki-kirora/enginner_study/blob/main/Language/Markdown/Markdown%E8%A8%98%E6%B3%95.md#%E7%95%AA%E5%8F%B7%E4%BB%98%E3%81%8D%E3%83%AA%E3%82%B9%E3%83%881)
- [引用](https://github.com/humiki-kirora/enginner_study/blob/main/Language/Markdown/Markdown%E8%A8%98%E6%B3%95.md#%E5%BC%95%E7%94%A8)
- [コード](https://github.com/humiki-kirora/enginner_study/blob/main/Language/Markdown/Markdown%E8%A8%98%E6%B3%95.md#%E3%82%B3%E3%83%BC%E3%83%89)
- [チェックボックス](https://github.com/humiki-kirora/enginner_study/blob/main/Language/Markdown/Markdown%E8%A8%98%E6%B3%95.md#%E3%83%81%E3%82%A7%E3%83%83%E3%82%AF%E3%83%9C%E3%83%83%E3%82%AF%E3%82%B9)
- [リンク](https://github.com/humiki-kirora/enginner_study/blob/main/Language/Markdown/Markdown%E8%A8%98%E6%B3%95.md#%E3%83%AA%E3%83%B3%E3%82%AF)
- [画像](https://github.com/humiki-kirora/enginner_study/blob/main/Language/Markdown/Markdown%E8%A8%98%E6%B3%95.md#%E7%94%BB%E5%83%8F)


## 見出し(#)

```
# 見出し1
## 見出し2
### 見出し3
```

# 見出し1
## 見出し2
### 見出し3

## 箇条書き(-)
```
- A
  - a
  - b
- B
```
- A
  - a
  - b
- B


## 番号付きリスト(1.)
```
1. A
   1. a
   2. b
2. B
```
1. A
   1. a
   2. b
2. B  
   
## 引用(>)

```
> 文章
> テスト
>> 二重引用も  
>> 可能
```
> 文章  
> テスト
>> 二重引用も  
>> 可能

## コード(```)
```
$```
 コード
$```
```
```
コード
```

## チェックボックス([])

```
- [x] チェック1 //x
- [ ] チェック2 //半角スペース
```
- [x] チェック1
- [ ] チェック2

## 強調
```
#斜体(*,_)
通常 *斜体* 
通常 _斜体_

#太字(**,__)
通常 **太字** 
通常 __太字__

#複合(***,___)
通常 ***複合*** 
通常 ___複合___
```
通常 *強調*  
通常 _強調_  
通常 **太字**   
通常 __太字__  
通常 ***複合***  
通常 ___複合___

## 水平線()
```
# *,-,_を3つ以上連続(間にスペースがあっても良い)
* * *
- - -
_ _ _
```
1行目
***
2行目
- - - 
3行目
_ _ _

## リンク
```
[タイトル](URL)

#定義参照リンク
[タイトル][参照]
[参照]:URL
```
[このページ](https://github.com/humiki-kirora/enginner_study/blob/main/Language/Markdown/Markdown%E8%A8%98%E6%B3%95.md#%E3%83%AA%E3%83%B3%E3%82%AF)

[参照リンク][url]  

[url]: https://github.com/humiki-kirora/enginner_study/blob/main/Language/Markdown/Markdown%E8%A8%98%E6%B3%95.md#%E3%83%AA%E3%83%B3%E3%82%AF

## 画像
```
![画像タイトル](URL)
or
![画像タイトル](パス)
```
![Lenna](image/Lenna.png)

