以下に、**構成ファイルの説明と導入方法のみ**に絞った簡潔な取扱説明書を示します。  
`create_chrome_profile.bat` の利用と `config.txt` の設定方法に焦点を当てています。

---

# HoYoLAB 自動ログインスクリプト 取扱説明書（構成ファイルと導入方法）

## 📁 必要な構成ファイル

| ファイル名                  | 説明                                                                 |
|-----------------------------|----------------------------------------------------------------------|
| `hoyolab.exe`               | 自動実行本体。Chromeをバックグラウンドで起動しログインボーナスを取得します |
| `create_chrome_profile.bat`| Chromeの専用プロファイルを初回のみ作成するためのバッチファイル              |
| `config.txt`                | Chromeプロファイルの場所や実行設定を記述する設定ファイル                     |
| `urls.txt`                  | アクセスするHoYoLABのログインボーナスページURLを1行ずつ記述                  |

---

## 🛠 導入手順

### ① Chrome用の専用プロファイルを作成（初回のみ）

- `create_chrome_profile.bat` をダブルクリックで実行  
- Chromeが起動したら **HoYoLAB にログイン** してください（ログイン状態は保存されます）  
- ログイン後、Chromeは閉じて構いません

この操作で、プロファイルフォルダ `C:\Users\あなたのユーザー名\AppData\Local\ChromeSelenium` にログイン情報が保存されます。

---

### ② `config.txt` を編集

以下のように記述してください（必要に応じて `USERNAME` を書き換えます）：

```
user-data-dir=C:/Users/%USERNAME%/AppData/Local/ChromeSelenium
profile-directory=Default
headless=true
```

- `user-data-dir`: 手順①で作成されたChromeプロファイルの場所  
- `profile-directory`: 通常は `Default` で問題ありません  
- `headless`: `true` にするとChromeを非表示で動作させます（ウィンドウを開かず実行）

※ `%USERNAME%` は自動で展開されるため、そのままでも動作します。

---

### ③ `urls.txt` に対象URLを記入

例えば以下のように、1行ごとに対象ページのURLを記述します：

```
https://act.hoyolab.com/bbs/event/signin/hkrpg/...
https://act.hoyolab.com/bbs/event/signin-bh3/...
https://act.hoyolab.com/bbs/event/signin/zzz/...
https://act.hoyolab.com/ys/event/signin-sea-v3/...
```

不要なタイトルは削除して構いません。

---

以上で初期設定は完了です。`hoyolab.exe` をダブルクリックするか、タスクスケジューラーから定期実行することで、自動でログインボーナスを取得します。