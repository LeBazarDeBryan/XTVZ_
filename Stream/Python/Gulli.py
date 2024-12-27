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
                f'#EXT-X-STREAM-INF:BANDWIDTH=2907102,AVERAGE-BANDWIDTH=2087002,RESOLUTION=1024x576,FRAME-RATE=25.000,CODECS="avc1.64001F,mp4a.40.2",SUBTITLES="subtitles",AUDIO="audio_0"\n'
                f"{stream_url.replace('hlsfmp4_short_q2hyb21h_gulli_sd_index.m3u8', 'hlsfmp4_short_q2hyb21h_gulli_sd_index_1.m3u8')}\n"
                f'#EXT-X-STREAM-INF:BANDWIDTH=1653102,AVERAGE-BANDWIDTH=1207002,RESOLUTION=1024x576,FRAME-RATE=25.000,CODECS="avc1.64001F,mp4a.40.2",SUBTITLES="subtitles",AUDIO="audio_0"\n'
                f"{stream_url.replace('hlsfmp4_short_q2hyb21h_gulli_sd_index.m3u8', 'hlsfmp4_short_q2hyb21h_gulli_sd_index_2.m3u8')}\n"
                f'#EXT-X-STREAM-INF:BANDWIDTH=869321,AVERAGE-BANDWIDTH=656967,RESOLUTION=640x360,FRAME-RATE=25.000,CODECS="avc1.42C01E,mp4a.40.2",SUBTITLES="subtitles",AUDIO="audio_0"\n'
                f"{stream_url.replace('hlsfmp4_short_q2hyb21h_gulli_sd_index.m3u8', 'hlsfmp4_short_q2hyb21h_gulli_sd_index_3.m3u8')}\n"
                f'''#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_0",CHANNELS="2",NAME="LV",LANGUAGE="fra",DEFAULT=YES,AUTOSELECT=YES,URI="{stream_url.replace('hlsfmp4_short_q2hyb21h_gulli_sd_index.m3u8', 'hlsfmp4_short_q2hyb21h_gulli_sd_index_4_0.m3u8')}"\n'''
                f'''#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_0",CHANNELS="2",NAME="OV",LANGUAGE="qaa",DEFAULT=NO,AUTOSELECT=NO,URI="{stream_url.replace('hlsfmp4_short_q2hyb21h_gulli_sd_index.m3u8', 'hlsfmp4_short_q2hyb21h_gulli_sd_index_5_0.m3u8')}"\n'''
                f'''#EXT-X-MEDIA:TYPE=AUDIO,GROUP-ID="audio_0",CHANNELS="2",NAME="AD",LANGUAGE="qad",CHARACTERISTICS="public.accessibility.describes-video",DEFAULT=NO,AUTOSELECT=NO,URI="{stream_url.replace('hlsfmp4_short_q2hyb21h_gulli_sd_index.m3u8', 'hlsfmp4_short_q2hyb21h_gulli_sd_index_6_0.m3u8')}"\n'''
                f'''#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subtitles",NAME="fra",DEFAULT=YES,AUTOSELECT=YES,FORCED=NO,LANGUAGE="fra",URI="{stream_url.replace('hlsfmp4_short_q2hyb21h_gulli_sd_index.m3u8', 'hlsfmp4_short_q2hyb21h_gulli_sd_index_4_0.m3u8')}"\n'''
                f'''#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subtitles",NAME="fra",DEFAULT=YES,AUTOSELECT=YES,FORCED=NO,LANGUAGE="fra",URI="{stream_url.replace('hlsfmp4_short_q2hyb21h_gulli_sd_index.m3u8', 'hlsfmp4_short_q2hyb21h_gulli_sd_index_7_0.m3u8')}"\n'''
                f'''#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subtitles",NAME="fra_hoh",CHARACTERISTICS="public.accessibility.transcribes-spoken-dialog,public.accessibility.describes-music-and-sound",DEFAULT=NO,AUTOSELECT=NO,FORCED=NO,LANGUAGE="fra",URI="{stream_url.replace('hlsfmp4_short_q2hyb21h_gulli_sd_index.m3u8', 'hlsfmp4_short_q2hyb21h_gulli_sd_index_8_0.m3u8')}"'''
            )
            return m3u8_content
        else:
            print("https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Images/Offline.mp4")
            print("\n")
            print("#Error: Streamlink stdout:", result.stdout.strip())
            return None

    except Exception as e:
        print("https://raw.githubusercontent.com/LeBazarDeBryan/XTVZ_/main/Images/Offline.mp4")
        print("\n")
        print(f"#Error: {e}")
        return None

m3u8_content = generate_m3u8_content("https://www.m6.fr/gulli/direct")
if m3u8_content:
    print(m3u8_content)
