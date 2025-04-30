# HoYoLAB Auto Login Tool

HoYoLAB（原神・崩壊シリーズなど）のログインボーナスを**自動取得**するWindows用ツールです。  
Google Chromeをバックグラウンドで起動し、事前にログイン済みの専用プロファイルを使って、最新の日付のログインボーナスをクリックします。

(開発中)
github actionsでログインボーナスを獲得
https://github.com/kuromame00x/hoyolab_Auto_Login_withGitActions
---

## 🧠 特徴

- HoYoLABが使用するタイムゾーン（UTC+8）で日付を判定し、**当日の「◯日目」を自動クリック**
- Chromeを**非表示（headless）**でバックグラウンド起動
- **複数ゲームのログインボーナスページを一括処理**
- **マウスやキーボード操作を奪わずに処理可能**
- Python環境不要（`.exe` 単体で動作）

---

## 📁 ディレクトリ構成

```
hoyolab_Auto_Login/
├── hoyolab_tool/
│   ├── config.txt                # Chromeプロファイルなどの設定
│   ├── urls.txt                  # 自動ログイン対象のHoYoLAB URLを記載（1行ずつ）
│   ├── create_chrome_profile.bat # 初回のみ使用。ChromeSeleniumプロファイル作成用
│   ├── hoyolab.exe               # 実行ファイル（PyInstallerで生成済）
├── src/
│   └── hoyolab.py                # .exe生成元のPythonスクリプト
├── README.md                     # このファイル
└── .gitignore                    # Git追跡除外ファイル
```

## 🛠 導入手順

### 1. Chrome専用プロファイルの作成（初回のみ）

- `create_chrome_profile.bat` を実行し、Chromeを起動  
- HoYoLAB にログインして閉じる  
  ※この操作でプロファイルフォルダ `C:/Users/ユーザー名/AppData/Local/ChromeSelenium` が作成され、ログイン情報が保存されます

---

### 2. `config.txt` を編集

```txt
user-data-dir=C:/Users/%USERNAME%/AppData/Local/ChromeSelenium
profile-directory=Default
headless=true
```

- `%USERNAME%` は自動展開されるためそのままでOK  
- `headless=true` にするとChrome非表示で起動（マウス操作などに干渉せずバックグラウンドで実行）

---

### 3. `urls.txt` に対象ページを記入

自動ログイン対象の HoYoLAB チェックインページURLを **1行ずつ** 記述してください。以下は記入例です。

```txt
https://act.hoyolab.com/bbs/event/signin/hkrpg/...
https://act.hoyolab.com/bbs/event/signin-bh3/...
https://act.hoyolab.com/bbs/event/signin/zzz/...
https://act.hoyolab.com/ys/event/signin-sea-v3/...
```

- 不要なタイトルのURLは削除してOK  
- スクリプトは各ページを**順番にタブで開いて処理**します

---

### 4. `.exe` を実行してログインボーナスを取得

- `hoyolab.exe` を **ダブルクリックで実行**するだけでOK  
- バックグラウンドでChromeが自動起動し、**最新の日付に自動クリック**します  
- ログイン状態が保存された専用プロファイルを使用するため、再ログインは不要です  
- `headless=true` 設定時は **ウィンドウを表示せず**に実行されるため、マウス操作に干渉しません

※処理ログは `hoyolab_YYYYMMDD.log` として同フォルダに自動保存されます

---
