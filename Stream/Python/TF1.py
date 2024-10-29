import subprocess
import os

def generate_m3u8_content(streamlink_url):
    try:
        tf1_user = os.environ.get("TF1_USER")
        tf1_password = os.environ.get("TF1_PASSWORD")

        if not tf1_user or not tf1_password:
            print("Error: TF1_USER or TF1_PASSWORD environment variable is not set.")
            return None

        result = subprocess.run(
            [
                "streamlink",
                "--tf1-purge-credentials",
                f"--tf1-email={tf1_user}",
                f"--tf1-password={tf1_password}",
                streamlink_url,
                "best",
                "--stream-url"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )

        stream_url = result.stdout.strip()

        m3u8_content = (
            "#EXTM3U\n"
            "#EXT-X-VERSION:3\n"
            "#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000\n"
            f"{stream_url}\n"
        )
        
        return m3u8_content

    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None

m3u8_content = generate_m3u8_content("https://www.tf1.fr/tf1/direct")
if m3u8_content:
    print(m3u8_content)
