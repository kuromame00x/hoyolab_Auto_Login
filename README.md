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

## 4. タスクスケジューラーで毎日自動実行する
Windowsの「タスクスケジューラー」に登録することで、毎日決まった時間に自動実行することが可能です。


4-1. Windowsキーを押して「タスクスケジューラー」と検索し起動

4-2. 右側の「基本タスクの作成」をクリック

4-3. 名前を「HoYoLAB Auto Login」などに設定し、[次へ]

4-4.「毎日」を選択して [次へ]

4-5. 実行時間を「朝7時〜9時の間（日本時間）」などに設定して [次へ]

4-6.「プログラムの開始」を選んで [次へ]

4-7.「プログラム/スクリプト」に`hoyolab.exe`のパスを指定
※hoyolab.exeを右クリック、パスのコピー

4-8. [完了] を押して登録完了

---

## 5. 時刻通りに実行できなかった場合の設定

タスクスケジューラーでは、**指定した時刻にPCがスリープ中、起動していない、または他の理由で実行に失敗**した場合でも、後から自動で実行するよう設定できます。

### ✅ 推奨設定方法

5-1. `タスクスケジューラー` を開き、作成済みの `hoyoverseデイリーログイン` タスクを右クリック → 「プロパティ」を開く
5-2. 「**設定**」タブを開き、以下の項目にチェックを入れます：

| オプション                                       | 推奨状態 |
|--------------------------------------------------|-----------|
| ✅ タスクを要求時に実行する                        | ✔️        |
| ✅ スケジュールされた時刻にタスクが開始できなかった場合、すぐにタスクを実行する | ✔️        |
| ✅ タスクを停止するまでの時間                     | 1 時間など |
| ✅ 要求時に実行中のタスクがスケジュールされている場合、タスクを強制的に停止する | ✔️        |

5-3. 最後に「OK」で保存
