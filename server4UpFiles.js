const express = require('express');
const multer = require('multer');
const fs = require('fs');
const app = express();

// multerの設定
var storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, 'uploads/')// アップロード先のディレクトリ
    },
    filename: function (req, file, cb) {
        cb(null, Date.now() + '-' + file.originalname)// ファイル名をタイムスタンプでユニークにする
    }
});

var upload = multer({ storage: storage });

// ファイルアップロードを処理するPOSTエンドポイント
app.post('/upload', upload.array('file'), (req, res) => {
    if (!req.file) {
        res.status(400).send('No file uploaded.');
        return;
    }

    // アップロードされたファイル情報をレスポンスとして送信
    res.send({ filename: req.file.filename });
});

// サーバ起動
app.listen(3000, () => console.log('Server started on port 3000'));
