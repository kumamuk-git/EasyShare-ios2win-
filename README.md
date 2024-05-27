# iOS to Windows LAN Share

iPhoneまたはiPadからショートカットで同一LAN内にあるWindows PCにWebサイトやファイルを共有するためのスクリプトです。

## 1. PCのIPアドレスの固定
1.1. Windows左下の検索窓に「cmd」と入力してコマンドプロンプトを開きます。  
1.2. 「ipconfig -all」と入力し、エンター。IPアドレス関連の情報が出てきます。  
1.3. [こことか](https://www.buffalo.jp/support/faq/detail/15257.html)を参考にIPアドレスを手動で設定します。1.2で確認したものを入力してください。

## 2. Node.jsのインストール
2.1. [こことか](https://medium-company.com/node-js%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%89%8B%E9%A0%86/)を参考にNode.jsをインストールします。

## 3. `server.js`の配置＆モジュールのインストール
3.1. お好きな場所に`server.js`を配置します。  
3.2. `server.js`が配置されたディレクトリでコマンドプロンプトを起動します。  
3.3. `npm install express open`を入力し、エンター。モジュールがインストールされます。`node_modules`というフォルダができていればOKです。

## 4. iPhoneショートカットの設定
4.0. [ショートカットリンク](https://www.icloud.com/shortcuts/f9d65a724bb14ed08ed655ff13f70081)を開きます。  
4.1. ショートカットアプリを開き、共有したショートカットの編集画面へ。  
4.2. 「http://(ipアドレス):8080/の内容を取得」のIPアドレスの部分を1.3で設定したものに変更します。

## 5. Node.jsのプロセスマネージャ（pm2）のインストール
5.1. コマンドプロンプトを起動。  
5.2. `npm install -g pm2`でインストール。  
5.3. `npm install -g pm2-windows-startup`も実行。

## 6. 検証
6.1. 3.2と同様の方法でコマンドプロンプトを起動。  
6.2. `pm2 start server.js`と入力。  
6.3. iPhoneでSafariを開き、共有ボタンからショートカットを実行。  
6.4. WebサイトがWindows上で開かれるはずです。  

## 7. Windows起動と同時にサーバを起動する設定
7.1. `pm2 save`を入力し、エンター。  
7.2. `pm2-startup install`を入力し、エンター。これでWindows起動時に自動でサーバが立ち上がります。

## 8. 7で起動時にうまく立ち上がらない場合
8.1. `pm2_resurrect.bat`をタスクスケジューラでwindows起動時に叩くようにすることでなんとかできます。

---

これで設定は完了です。
