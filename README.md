# HoYoLAB Auto Login Tool

HoYoLAB（原神・崩壊シリーズなど）のログインボーナスを**自動取得**するWindows用ツールです。  
Google Chromeをバックグラウンドで起動し、事前にログイン済みの専用プロファイルを使って、最新の日付のログインボーナスをクリックします。

---

## 🧠 特徴

- HoYoLABが使用するタイムゾーン（UTC+8）で日付を判定し、**当日の「◯日目」を自動クリック**
- Chromeを**非表示（headless）**でバックグラウンド起動
- **複数ゲームのログインボーナスページを一括処理**
- **マウスやキーボード操作を奪わずに処理可能**
- Python環境不要（`.exe` 単体で動作）

---

## 📁 ディレクトリ構成

hoyolab_Auto_Login/
├── hoyolab_tool/
│   ├── config.txt                # Chromeプロファイルなどの設定
│   ├── urls.txt                  # 自動ログイン対象のHoYoLAB URLを記載（1行ずつ）
│   ├── create_chrome_profile.bat# 初回のみ使用。ChromeSeleniumプロファイル作成用
│   └── hoyolab.exe              # 実行ファイル（PyInstallerで生成済）
├── src/
│   └── hoyolab.py               # .exe生成元のPythonスクリプト（透明性確保のため公開）
├── README.md                    # このファイル
└── .gitignore                   # Git追跡除外ファイル


---

## 🛠️ 導入手順

### 1. Chrome専用プロファイルの作成（初回のみ）

- `create_chrome_profile.bat` を実行し、Chromeを起動
- HoYoLABにログインして閉じる  
  ※この操作でプロファイルフォルダ `C:/Users/ユーザー名/AppData/Local/ChromeSelenium` が作成され、ログイン情報が保存されます。

---

### 2. `config.txt` を編集

```txt
user-data-dir=C:/Users/%USERNAME%/AppData/Local/ChromeSelenium
profile-directory=Default
headless=true

以下は画像の内容をもとに、**`README.md` にそのまま使えるMarkdown形式**で整形し直したものです。手順3以降が崩れないよう、番号・インデント・コードブロックも修正済みです。

---

## 3. `urls.txt` に対象ページを記入

自動ログイン対象の HoYoLAB チェックインページURLを 1 行ずつ記述してください。以下は記入例です。

```
https://act.hoyolab.com/bbs/event/signin/hkrpg/...
https://act.hoyolab.com/bbs/event/signin-bh3/...
https://act.hoyolab.com/bbs/event/signin/zzz/...
https://act.hoyolab.com/ys/event/signin-sea-v3/...
```

- 不要なタイトルのURLは削除してOKです  
- スクリプトは各ページを順番にタブで開いて処理します

---

これで手順全体の構成が視認性よく維持されます。`README.md` に直接貼り付けて問題ありません。
