import subprocess
import os

def generate_m3u8_content(streamlink_url):
    try:
        tf1_user = os.environ.get("TF1_USER")
        tf1_password = os.environ.get("TF1_PASSWORD")

        if not tf1_user or not tf1_password:
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
                "#EXT-X-VERSION:3\n"
                "#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000\n"
                f"{stream_url.replace('index_1.m3u8', 'index.m3u8')}\n"
            )
            return m3u8_content
        else:
            print("Error: Streamlink stderr:", result.stderr.strip())
            print("Error: Streamlink stdout:", result.stdout.strip())
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

m3u8_content = generate_m3u8_content("https://www.tf1.fr/lci/direct")
if m3u8_content:
    print(m3u8_content)
