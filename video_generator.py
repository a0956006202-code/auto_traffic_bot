import os
import subprocess
import datetime

def generate_real_video():
    now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = os.path.expanduser('~/auto_traffic_bot/output')
    os.makedirs(output_dir, exist_ok=True)
    
    video_name = f'real_empire_video_{now}.mp4'
    output_path = os.path.join(output_dir, video_name)
    
    print(f"[*] 正在渲染高品質標準短影音：{video_name} ...")
    
    # 使用 FFmpeg 製作 1080x1920 (TikTok/Reels 尺寸)、藍底漸層、帶有動態文字與標準 H.264/AAC 編碼的真實影片 (長度 10 秒)
    cmd = [
        'ffmpeg', '-y',
        '-f', 'lavfi', '-i', 'color=c=navy:s=1080x1920:d=10',
        '-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo',
        '-vf', "drawtext=text='EMPIRE TRAFFIC BOT':fontcolor=white:fontsize=64:x=(w-text_w)/2:y=(h-text_h)/2-100,"
               "drawtext=text='24/7 Autonomous Monetization':fontcolor=yellow:fontsize=40:x=(w-text_w)/2:y=(h-text_h)/2+50,"
               "drawtext=text='Account: 700-0902544':fontcolor=cyan:fontsize=36:x=(w-text_w)/2:y=(h-text_h)/2+150",
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-c:a', 'aac',
        '-shortest',
        output_path
    ]
    
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"[+] 成功產出真實短影音：{output_path}")
    else:
        print(f"[-] 渲染失敗：{result.stderr.decode('utf-8')}")

if __name__ == '__main__':
    generate_real_video()
