from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta, timezone
import subprocess
import time
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(sys.executable if getattr(sys, 'frozen', False) else __file__))

def kill_chrome_profile_processes(identifier="ChromeSelenium"):
    cmd = f'wmic process where "CommandLine like \'%%{identifier}%%\' and name=\'chrome.exe\'" get ProcessId'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    pids = [line.strip() for line in result.stdout.strip().splitlines() if line.strip().isdigit()]
    for pid in pids:
        subprocess.run(f'taskkill /PID {pid} /F', shell=True)

def load_urls(path="urls.txt"):
    with open(os.path.join(BASE_DIR, path), "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def load_config(path="config.txt"):
    config = {}
    with open(os.path.join(BASE_DIR, path), "r", encoding="utf-8") as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                config[key.strip()] = os.path.expandvars(value.strip())
    return config

URLS = load_urls()
conf = load_config()

date_str = datetime.now().strftime("%Y%m%d")
log_path = os.path.join(BASE_DIR, f"hoyolab_{date_str}.log")
sys.stdout = open(log_path, "a", encoding="utf-8")
sys.stderr = sys.stdout

print(f"\n=== 実行開始: {datetime.now()} ===\n", flush=True)
print("スクリプト開始", flush=True)

kill_chrome_profile_processes("ChromeSelenium")

today = (datetime.now(timezone.utc) + timedelta(hours=8)).day
target_text = f"{today}日目"
print(f"今日のターゲット: {target_text}", flush=True)

options = Options()
options.add_argument(f"--user-data-dir={conf.get('user-data-dir')}")
options.add_argument(f"--profile-directory={conf.get('profile-directory')}")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
if conf.get("headless", "").lower() == "true":
    options.add_argument("--headless")  # ← --headless=chrome は避ける


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(URLS[0])
for url in URLS[1:]:
    driver.execute_script(f"window.open('{url}');")

tabs = driver.window_handles

for i, tab in enumerate(tabs):
    driver.switch_to.window(tab)
    print(f"\nタブ{i+1}に切り替え: {URLS[i]}", flush=True)
    time.sleep(3)

    elements = driver.find_elements(By.XPATH, "//span | //div")
    found = False
    for el in elements:
        try:
            if el.text.strip() == target_text:
                print("一致する要素発見", flush=True)
                parent = el.find_element(By.XPATH, "..")
                parent.click()
                print(f"{target_text} のボーナスをクリックしました（{URLS[i]}）", flush=True)
                found = True
                break
        except StaleElementReferenceException:
            continue

    if not found:
        print(f"{target_text} の要素が見つかりませんでした（{URLS[i]}）", flush=True)

    time.sleep(1)

driver.quit()
print("スクリプト終了", flush=True)

kill_chrome_profile_processes("ChromeSelenium")
sys.stdout.close()
sys.exit(0)
