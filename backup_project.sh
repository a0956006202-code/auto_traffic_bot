#!/bin/bash
BACKUP_DIR=~/backup_$(date +%Y%m%d_%H%M%S)
echo "[+] 正在備份 auto_traffic_bot 專案..."
mkdir -p $BACKUP_DIR
cp -r ~/auto_traffic_bot $BACKUP_DIR/
echo "[+] 專案已成功備份至: $BACKUP_DIR"
