# iOS to Windows LAN Share

iPhoneまたはiPadからショートカットで同一LAN内にあるWindows PCにWebサイトやファイルを共有するためのスクリプトです

## 1. PCのIPアドレスの固定
1. コマンドプロンプトを起動  
2. IPアドレスの確認  
```bash
ipconfig -all
```
3. [こことか](https://www.buffalo.jp/support/faq/detail/15257.html)を参考にIPアドレスを手動で設定 1-2で確認したものを入力してください

## 2. Node.jsのインストール
1. [こことか](https://medium-company.com/node-js%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E6%89%8B%E9%A0%86/)を参考にNode.jsをインストール  
  
## 3. リポジトリのクローン＆モジュールのインストール
1. 以下を実行
```bash
git clone https://github.com/masaki-krrn/EasyShare-ios2win-.git  
npm install express open
```
  
## 4. iPhoneショートカットの設定
1. [PCで開く](https://www.icloud.com/shortcuts/71b8ca2c4a31428cb14c0a40dd08ce51) 及び[ファイルをPCへ共有](https://www.icloud.com/shortcuts/b73b3bcd178a4710969978924372e05c)からショートカットを入手  
2. ショートカットアプリを開き、共有したショートカットの編集画面へ      
3. 「(ipアドレス)」のIPアドレスの部分を1.3で設定したものに変更
  
## 5. Node.jsのプロセスマネージャ（pm2）のインストール
1. インストール
```bash
npm install -g pm2  
npm install -g pm2-windows-startup
```
## 6. 検証（PCで開く）
1. プロセスを開始
```bash
pm2 start server.js
```
2. iPhoneでSafariを開き、共有ボタンから"PCで開く"ショートカットを実行      
3. WebサイトがWindows上で開かれるはずです     
  
## 7. 検証（ファイルをPCへ共有）
1.プロセスを開始
```bash
pm2 start server4UpFiles.js
```
2. iPhoneで写真アプリを開き、好きな写真を選択したのち共有ボタンから"ファイルをPCへ共有"ショートカットを実行  
3. `uploads`内に共有した画像ファイルが保存されています  
  
## 8. Windows起動と同時にサーバを起動する設定
1. 以下を実行
```bash
pm2 save  
pm2-startup install
```
  
## 9. 8で起動時にうまく立ち上がらない場合
1. `pm2_resurrect.bat`をタスクスケジューラでwindowsログオン時に叩くようにすることでなんとかできます  
  
## 10. HEICからPNGへの自動変換
1.  `Heic2png.py`をタスクスケジューラでログオン時に実行し、常駐させると、ディレクトリ内の.heicが.pngへ変換されます   
  
---


これで設定は完了です  
