# Qtのダイアログについての覚書
GUIにおいて、ファイルを入力する際に表示する選択画面を**ダイアログ**といい、
ダイアログを使用することで、必要なファイルのパスを探索することができる  
主に**QFileDialog**の使い方を説明するが、他にも色を選択する**QColorDialog**等もあるので必要になったら追記する予定

# 使い方　例：メニューバーからファイルを選択する
```C++
//メニューバーを押したときのシグナル
void MainWindow::on_image_open_triggered()
{
    QFileDialog dialog;

    /* オプション */

    if(dialog.exec() == QFileDialog::Accepted){
        //選択したファイルのパスを取得
        QStringList filePaths = dialog.selectedFiles();

        /*必要な処理*/
    }

}
```
## オプションについて
- setWindowTitle()
表示するダイアログのタイトルを設定する  
```C++
dialog.setWindowTitle("Select Directory");
```
- setFileMode
選択するファイルを設定することができる
  - AnyFile:任意の種類のファイルを選択(デフォルト)
  - ExistiongFIle:既存のファイルのみを選択
  - Directory:ディレクトリのみ選択

- setOption

- setFilter


