import subprocess

def generate_m3u8(streamlink_url, output_filename="stream.m3u8"):
    try:
        result = subprocess.run(
            ["streamlink", "--tf1-purge-credentials", "--tf1-email=%email%", "--tf1-password=%password%", streamlink_url, "best", "--stream-url"],
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

generate_m3u8("https://example.com/live/stream")
