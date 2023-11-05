# WSLで現在のブランチ名を表示したい

WSLを使用している際に現在のブランチを確認するのにいちいち`git status`を実行するのは正直面倒なので、レポジトリに移動した際に現在ブランチ名が一緒に表示されるようにしたい

# 方法
.bashrcの以下の部分を修正
`$(echo$(__git_ps1))`を入れることで現在ブランチを表示することが可能になる
```bash
if [ "$color_prompt" = yes ]; then
    #PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]$(echo$(__git_ps1))\[\033[00m\]$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$(__git_ps1)\$ '
fi
```
その後、`.bashrc`を反映させる
```
source ~/.bashrc
```
## 結果
```
user@user:~/git_repository$
↓
user@user:~/git_repository(main)$  
```
簡単に出来て便利なのでお得