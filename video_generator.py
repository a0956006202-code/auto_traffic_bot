# ==========================================
# 100% 零成本自動化流量帝國 - 實體影片渲染模組
# ==========================================

import os
import subprocess
import datetime

def generate_sample_video():
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.expanduser("~/auto_traffic_bot/output")
    download_dir = "/sdcard/Download"
    
    os.makedirs(output_dir, exist_ok=True)
    video_filename = f"auto_video_{now}.mp4"
    video_path = os.path.join(output_dir, video_filename)
    
    # 使用 ffmpeg 生成一個 5 秒的簡易示範短影音 (黑底加上時間標記)
    cmd = [
        "ffmpeg", "-y",
        "-f", "lavfi", "-i", f"color=c=black:s=1080x1920:d=5",
        "-vf", f"drawtext=text='Auto Empire {now}':fontcolor=white:fontsize=48:x=(w-text_w)/2:y=(h-text_h)/2",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        video_path
    ]
    
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"[+] 成功生成實體影片: {video_path}")
        
        # 同步搬移至 Download 資料夾供相冊查看
        if os.path.exists(download_dir):
            os.system(f"cp {video_path} {download_dir}/")
            print(f"[+] 已同步將影片導出至: {download_dir}/{video_filename}")
    except Exception as e:
        print(f"[-] 影片渲染提示: {e}")

if __name__ == "__main__":
    generate_sample_video()
