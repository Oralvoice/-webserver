# 説明
webサーバー(Amazon EC2)にあるプログラムです。<br>
app.pyはオーラルボイスからCloud Storage for Firebaseにアップロードした音声ファイル(wav)を取得する。<br>
取得した音声ファイルから評価する画像(メルスペクトログラム)を作成する。<br>
作成した画像をCloud Storage for Firebaseにアップロードしてオーラルボイスにダウンロードできるようにする。<br>

# 実行環境
Amazon Linux 2 AMI （x86） <br>
Python 3.7.9 <br>
librosa 0.80 <br>
matplotlib 3.3.2 <br>
numpy 1.19.2 <br>
Flask 1.1.2 <br>
firebase-admin 4.4.0 <br>

# インストール方法
以下をEC2 Instance Connectで実行する。
pip3 install librosa <br>
pip3 install matplotlib <br>
pip3 install numpy <br>
pip3 install firebase-admin <br>
pip3 install flask <br>

# 処理の流れ
Ⅰ. EC2 Instance Connectで仮想環境を構築する(調べてください)。<br>

Ⅱ. source Oralvoice/bin/activateで仮想環境に入る。(Oralvoiceは仮想環境名)<br>

Ⅲ. gistにapp.pyとoral-voice-14555-firebase-adminsdk-9d2a4-895b1df1a3.json(新しく生成した秘密鍵)をアップロードしてをクローンする。<br>

Ⅳ. app.pyの22行目を使用するバケットの名前に変更する。<br>

Ⅴ. 「cd ディレクトリの名前」でクローンしたgistのディレクトリに移動する。<br>

Ⅵ. python3 app.pyで実行する。<br>

Ⅶ. app.pyを実行すると、androidからCloud Storage for firebaseにtest.wavという名前でアップロードしたファイルを取得してuser.wavでダウンロードする。<br>

Ⅷ. user.wavをロードして評価する画像(user.png)を作成し、Cloud Storage for firebaseにtest.pngという名前でアップロードする。<br>
