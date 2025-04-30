HoYoLAB 自動ログインスクリプト - 導入手順（構成ファイルと設定のみ）

[ 構成ファイル一覧 ]

- hoyolab.exe
  └─ 自動実行本体。HoYoLABのログインボーナスを取得するための実行ファイル。

- create_chrome_profile.bat
  └─ 初回実行時にChrome専用プロファイルを作成するためのバッチファイル。

- config.txt
  └─ Chromeプロファイルの場所や動作モード（ヘッドレスなど）を記述する設定ファイル。

- urls.txt
  └─ 取得対象のHoYoLABログインボーナスページのURLを1行ずつ記述。


[ 初回セットアップ手順 ]

1. Chromeプロファイルの作成（初回のみ）

   - create_chrome_profile.bat を実行
   - 起動したChrome上で HoYoLAB にログイン
   - ログイン後、Chromeを閉じる

   ※ ChromeSeleniumという名前で専用プロファイルが作成されます。
   （C:\Users\ユーザー名\AppData\Local\ChromeSelenium）

2. config.txt の編集

   以下の内容を記述します：

   user-data-dir=C:/Users/%USERNAME%/AppData/Local/ChromeSelenium
   profile-directory=Default
   headless=true

   ・user-data-dir は上記プロファイルのパス
   ・profile-directory は通常 "Default"
   ・headless は true にするとChrome非表示で動作します

   ※ %USERNAME% はWindowsの環境変数として自動展開されます。

3. urls.txt の編集

   HoYoLABのログインボーナスページURLを1行ずつ記述してください：

   例：
   https://act.hoyolab.com/bbs/event/signin/hkrpg/...
   https://act.hoyolab.com/bbs/event/signin-bh3/...
   https://act.hoyolab.com/bbs/event/signin/zzz/...
   https://act.hoyolab.com/ys/event/signin-sea-v3/...

   ※ 不要なURLは削除して構いません。


[ 実行方法 ]

- hoyolab.exe をダブルクリックして実行
- または、タスクスケジューラーに登録して毎日自動実行


[ 補足 ]

- 実行後、ログファイルが同じフォルダに "hoyolab_YYYYMMDD.log" 形式で出力されます。
- Chromeはバックグラウンドで起動・終了します。
