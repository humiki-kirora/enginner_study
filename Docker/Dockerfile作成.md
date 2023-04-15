# Dockerfile
- [Dockerfileとは]()
- [コマンド集]()
- [作成作業の流れ]()

# Dockerfileとは
Docker imagesを生成するための構文  
Dockerfileを共有することで誰でも同じ作業環境を簡単に構築できるようになる

```
docker image build -t イメージ名[:タグ名] [Dockerfileが配置されているディレクトリパス]
```

# コマンド集

## FROM
[Docker Hub](https://hub.docker.com/)で公開されているイメージをベースに利用
```Docker
FROM <イメージ>
FROM <イメージ>:<タグ>
```

## MAINTAINER
作成者情報を入力
```Docker
MAINTAINER <名前> 
```
## LABEL
metaデータを追加する
```Docker
LABEL <key>=<value> 
```
## RUN
コマンドの実行。基本的にベースイメージで使用するコマンド
```Docker
RUN <コマンド>
RUN ["実行バイナリ","パラメータ1"] 
```
`apt-get`などを使用する際には`-y`で自動的にインストールできるようにする

## CMD
コンテナ実行時の実行コマンド  
Dockerfile内で一度だけ指定可能。`docker run`時に実行されるコマンドを指定する。`docker run`時にコマンドが指定された場合、そちらが優先される
```Docker
CMD <コマンド>
CMD ["実行バイナリ", "パラメータ１", "パラメータ２"]
```
## ENTRYPOINT
コンテナ実行時の実行コマンド
Dockerfile内で一度だけ指定可能。`docker run`時に実行されるコマンドを指定する.`docker run`時にコマンドを指定しても、こちらのコマンドが優先される
```Docker
ENTRYPOINT <コマンド>
ENTRYPOINT ["実行バイナリ", "パラメータ１", "パラメータ２"]
```

## EXPOSE
ポートの解放
```Docker
EXPOSE <port> [<port>...]
```

## VOLUME
指定したディレクトリをマウントする
```Docker
VOLUME ["/data"]
```

## ADD
FileやDirectoryを追加
```Docker
ADD <ファイル> <送信先>
```

## COPY
FileやDirectoryをコピー
```Docker
COPY <ソース> <送信先>
```

## USER
実行ユーザの指定
```Docker
USER <ユーザ名>
```

## WORKDIR
作業ディレクトリ指定
```Docker
WORKDIR <ディレクトリパス>
```

## ENV
環境変数を設定する
```Docker
ENV <key>=<value>
```

## ARG
Dockerfile内での変数の定義
```Docker
ARG USER=user
ARG UID
```

# 作成作業の流れ
大まかな手順について具体的な話な作業を踏まえて説明

1. ベースイメージの決定  
`FROM`コマンドで[Docker Hub](https://hub.docker.com/)で公開されているイメージをベースに作業する  
今回は`Ubuntu:latest`を利用する
```Docker
FROM ubuntu:latest
```

2. ユーザ名、パスワード、環境変数等の定義を決める
```Docker
MAINTAINER me
ARG USER=builder
ARG UID
ARG GID
ARG

 
```
3. apt-getの更新、必要なパッケージのインストール