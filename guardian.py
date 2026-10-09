import subprocess
import os

def check_system():
    print("[+] 正在執行系統守護巡檢...")
    # 檢查 Git 狀態
    git_status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if git_status.stdout.strip():
        print("[!] 發現未提交的變更，正在自動同步...")
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "chore: auto-guardian sync state"])
        subprocess.run(["git", "push", "origin", "main"])
    print("[+] 系統守護巡檢完畢，運行一切正常。")

if __name__ == "__main__":
    check_system()
