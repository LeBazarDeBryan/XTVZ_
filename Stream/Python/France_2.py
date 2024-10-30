import subprocess

def generate_m3u8_content(streamlink_url):
    try:
        result = subprocess.run(
            [
                "streamlink",
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
                "#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000\n"
                f"{stream_url}"
            )
            return m3u8_content
        else:
            print("#EXTM3U")
            print("#EXT-X-VERSION:6")
            print("#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000")
            print("https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Images/Offline.mp4")
            print("\n")
            print("Error: Streamlink: stdout:", result.stdout.strip())
            return None

    except Exception as e:
        print("#EXTM3U")
        print("#EXT-X-VERSION:6")
        print("#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000")
        print("https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Images/Offline.mp4")
        print("\n")
        print(f"Error: {e}")
        return None

m3u8_content = generate_m3u8_content("https://www.france.tv/france-2/direct.html")
if m3u8_content:
    print(m3u8_content)
