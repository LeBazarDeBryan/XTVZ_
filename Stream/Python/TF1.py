import subprocess
import os

def generate_m3u8_content(streamlink_url):
    try:
        tf1_user = os.environ.get("TF1_USER")
        tf1_password = os.environ.get("TF1_PASSWORD")

        if not tf1_user or not tf1_password:
            print("https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Images/Offline.mp4")
            print("\n")
            print("Error: TF1_USER or TF1_PASSWORD environment variable is NOT set.")
            return None

        result = subprocess.run(
            [
                "streamlink",
                "--tf1-purge-credentials",
                f"--tf1-email={tf1_user}",
                f"--tf1-password={tf1_password}",
                streamlink_url,
                "--stream-url"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            stream_url = result.stdout.strip()

            m3u8_content = (
                "#EXTM3U\n"
                "#EXT-X-VERSION:6\n"
                "#EXT-X-INDEPENDENT-SEGMENTS"
                f'#EXT-X-STREAM-INF:BANDWIDTH=3165091,AVERAGE-BANDWIDTH=2856368,RESOLUTION=1280x720,FRAME-RATE=25.000,CODECS="avc1.4D401F,mp4a.40.2",AUDIO="audio_0"\n'
                f"{stream_url.replace('index.m3u8', 'index_1.m3u8')}\n"
                f'#EXT-X-STREAM-INF:BANDWIDTH=2179491,AVERAGE-BANDWIDTH=1976368,RESOLUTION=1024x576,FRAME-RATE=25.000,CODECS="avc1.4D401F,mp4a.40.2",AUDIO="audio_0"\n'
                f"{stream_url.replace('index.m3u8', 'index_2.m3u8')}\n"
                f'#EXT-X-STREAM-INF:BANDWIDTH=1563522,AVERAGE-BANDWIDTH=1426404,RESOLUTION=1024x576,FRAME-RATE=25.000,CODECS="avc1.4D401F,mp4a.40.2",AUDIO="audio_0"\n'
                f"{stream_url.replace('index.m3u8', 'index_3.m3u8')}\n"
                f'#EXT-X-STREAM-INF:BANDWIDTH=1070722,AVERAGE-BANDWIDTH=986404,RESOLUTION=640x360,FRAME-RATE=25.000,CODECS="avc1.42C01E,mp4a.40.2",AUDIO="audio_0"\n'
                f"{stream_url.replace('index.m3u8', 'index_4.m3u8')}\n"
                f'#EXT-X-STREAM-INF:BANDWIDTH=577922,AVERAGE-BANDWIDTH=546404,RESOLUTION=416x234,FRAME-RATE=25.000,CODECS="avc1.42C00D,mp4a.40.2",AUDIO="audio_0"\n'
                f"{stream_url.replace('index.m3u8', 'index_5.m3u8')}\n"
                f'''#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_0",CHANNELS="2",NAME="fra",LANGUAGE="fra",DEFAULT=YES,AUTOSELECT=YES,URI="{stream_url.replace('index.m3u8', 'index_13_0.m3u8')}"\n'''
            )
            return m3u8_content
        else:
            print("https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Images/Offline.mp4")
            print("\n")
            print("Error: Streamlink: stdout:", result.stdout.strip())
            return None

    except Exception as e:
        print("https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Images/Offline.mp4")
        print("\n")
        print(f"Error: {e}")
        return None

m3u8_content = generate_m3u8_content("https://www.tf1.fr/tf1/direct")
if m3u8_content:
    print(m3u8_content)
