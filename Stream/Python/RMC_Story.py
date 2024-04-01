#!/usr/bin/python3

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Referer": "http://www.callofliberty.fr/"
}

print('#EXTM3U')
print('#EXT-X-STREAM-INF:RESOLUTION=848x477,FRAME-RATE=50.000000,BANDWIDTH=1667072,CODECS="avc1.64001f,mp4a.40.2",NAME="480@60"')

master_url = "http://s2.callofliberty.fr/direct/RMCSTORY/master.m3u8"
s = requests.Session()

def get_specific_line_online(url, line_number):
    response = s.get(url, headers=headers)
    if response.status_code == 200:
        lines = response.text.split('\n')
        if 1 <= line_number <= len(lines):
            return lines[line_number - 1]
        else:
            return None
    else:
        return None

chunks = get_specific_line_online(master_url, 3)

prefix = "http://s2.callofliberty.fr/HLS-AES/"
index = chunks.find(prefix)

if index != -1:
    shortchunks = chunks[index + len(prefix):]
else:
    shortchunks = chunks

print(shortchunks)
