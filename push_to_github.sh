echo "=== 開始同步最新專案狀態至 GitHub 遠端備份 == /"
git push origin main || echo "若尚未設定遠端，請先執行 git remote add origin <您的倉庫網址>"
echo "=== 雲端備份同步完成 ==="
