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
                "#EXT-X-INDEPENDENT-SEGMENTS\n"
                f"{stream_url}"
            )
            return m3u8_content
        else:
            print("https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Images/Offline.mp4")
            print("\n")
            print("#Error: Streamlink: stdout:", result.stdout.strip())
            return None

    except Exception as e:
        print("https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Images/Offline.mp4")
        print("\n")
        print(f"#Error: {e}")
        return None

m3u8_content = generate_m3u8_content("https://www.dailymotion.com/video/x2lefik")
if m3u8_content:
    print(m3u8_content)
