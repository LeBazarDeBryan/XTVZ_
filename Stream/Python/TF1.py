import subprocess
import os

def generate_m3u8(streamlink_url):
    try:
        tf1_user = os.environ.get("TF1_USER")
        tf1_password = os.environ.get("TF1_PASSWORD")

        if not tf1_user or not tf1_password:
            print("Error: TF1_USER or TF1_PASSWORD environment variable is not set.")
            return
        
        result = subprocess.run(
            ["streamlink", "--tf1-purge-credentials", "--tf1-email=$TF1_USER", "--tf1-password=$TF1_PASSWORD", streamlink_url, "best", "--stream-url"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        
        stream_url = result.stdout.strip()

        with open(output_filename, "w") as file:
            file.write("#EXTM3U\n")
            file.write("#EXT-X-VERSION:3\n")
            file.write("#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000\n")
            file.write(f"{stream_url}\n")

    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

generate_m3u8("https://www.tf1.fr/tf1/direct")
