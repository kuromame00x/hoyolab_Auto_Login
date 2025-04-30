@echo off
setlocal

:: ユーザーのAppData\LocalにChromeSeleniumプロファイルを作成
set "PROFILE_DIR=%LOCALAPPDATA%\ChromeSelenium"

:: Chrome実行ファイルのパス（自動的に探すか固定指定）
set "CHROME_PATH=%ProgramFiles%\Google\Chrome\Application\chrome.exe"
if not exist "%CHROME_PATH%" set "CHROME_PATH=%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"

:: Chromeが見つからなければ終了
if not exist "%CHROME_PATH%" (
    echo Chromeが見つかりませんでした。
    pause
    exit /b
)

:: Chromeを独立プロファイルで起動（Defaultプロファイルが作成される）
start "" "%CHROME_PATH%" --user-data-dir="%PROFILE_DIR%" --profile-directory="Default"

echo ChromeSelenium プロファイルが起動しました。HoYoLAB にログインしてください。
pause
