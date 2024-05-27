# iOS to Windows LAN Share

iPhoneまたはiPadからショートカットで同一LAN内にあるWindows PCにWebサイトやファイルを共有するためのスクリプトです。

## 1. PCのIPアドレスの固定
1.1. Windows左下の検索窓に「cmd」と入力してコマンドプロンプトを開きます。  
1.2. 「ipconfig -all」と入力し、エンター。IPアドレス関連の情報が出てきます。  
1.3. [こことか](https://www.buffalo.jp/support/faq/detail/15257.html)を参考にIPアドレスを手動で設定します。1.2で確認したものを入力してください。

## 2. Node.jsのインストール
2.1. [こことか](https://medium-company.com/node-js%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%89%8B%E9%A0%86/)を参考にNode.jsをインストールします。

## 3. リポジトリのクローン＆モジュールのインストール
3.1. 
3.2. クローンしたディレクトリでコマンドプロンプトを起動します。  
3.3. `npm install express open`を入力し、エンター。モジュールがインストールされます。`node_modules`というフォルダができていればOKです。

## 4. iPhoneショートカットの設定
4.0. [ショートカットリンク(PCで開く)](https://www.icloud.com/shortcuts/71b8ca2c4a31428cb14c0a40dd08ce51) [ショートカットリンク(ファイルをPCへ共有)](https://www.icloud.com/shortcuts/b73b3bcd178a4710969978924372e05c)を開きます。  
4.1. ショートカットアプリを開き、共有したショートカットの編集画面へ。  
4.2. 「(ipアドレス)」のIPアドレスの部分を1.3で設定したものに変更します。

## 5. Node.jsのプロセスマネージャ（pm2）のインストール
5.1. コマンドプロンプトを起動。  
5.2. ```npm install -g pm2```でインストール。  
5.3. `npm install -g pm2-windows-startup`も実行。

## 6. 検証（PCで開く）
6.1. コマンドプロンプトを起動。  
6.2. `pm2 start server.js`と入力。
6.3. iPhoneでSafariを開き、共有ボタンから"PCで開く"ショートカットを実行。  
6.4. WebサイトがWindows上で開かれるはずです。  

## 7. 検証（ファイルをPCへ共有）
7.1. コマンドプロンプトを起動。  
7.2. `pm2 start server4UpFiles.js`と入力。
7.3. iPhoneで写真アプリを開き、好きな写真を選択したのち共有ボタンから"ファイルをPCへ共有"ショートカットを実行。  
7.4. `uploads`内に共有した画像ファイルが保存されています。

## 7. Windows起動と同時にサーバを起動する設定
7.1. `pm2 save`を入力。  
7.2. `pm2-startup install`を入力。これでWindows起動時に自動でサーバが立ち上がります。

## 8. 7で起動時にうまく立ち上がらない場合
8.1. `pm2_resurrect.bat`をタスクスケジューラでwindowsログオン時に叩くようにすることでなんとかできます。

## 9. HEICからPNGへの自動変換
9.1.  `Heic2png.py`をタスクスケジューラでログオン時に実行し、常駐させると、ディレクトリ内の.heicが.pngへ変換されます。

---


これで設定は完了です。
